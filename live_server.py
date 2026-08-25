#!/usr/bin/env python3
"""
CYBERPUNK 2077 PORTFOLIO - ZERO-LATENCY LIVE RELOAD SERVER (v2.077)
Features:
- Real-time Server-Sent Events (SSE) stream for hot-refreshing browsers
- Zero browser caching (no-cache headers on all assets)
- Multi-threaded file watcher tracking recursive directory mtime
- Zero external dependencies (Pure Python 3 standard library)
- Cyberpunk 2077 Neon Console UI & Telemetry
"""

import sys
import os
import time
import threading
import queue
from http.server import SimpleHTTPRequestHandler
import socketserver
import urllib.parse

PORT = 3000
if len(sys.argv) > 1:
    try:
        PORT = int(sys.argv[1])
    except ValueError:
        PORT = 3000

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IGNORE_DIRS = {'.git', '__pycache__', '.system_generated', 'node_modules', '.idea', '.vscode'}
WATCH_EXTENSIONS = {'.html', '.css', '.js', '.json', '.png', '.jpg', '.jpeg', '.webp', '.svg', '.gif', '.md'}

# Client queues for SSE
clients = []
clients_lock = threading.Lock()

def get_file_mtimes():
    """Recursively collect modification timestamps for all watched files."""
    mtimes = {}
    for root, dirs, files in os.walk(BASE_DIR):
        dirs[:] = [d for d in dirs if d not in IGNORE_DIRS]
        for f in files:
            ext = os.path.splitext(f)[1].lower()
            if ext in WATCH_EXTENSIONS:
                full_path = os.path.join(root, f)
                try:
                    mtimes[full_path] = os.path.getmtime(full_path)
                except OSError:
                    pass
    return mtimes

def watch_directory_loop():
    """Background thread to detect file changes and notify SSE clients."""
    last_mtimes = get_file_mtimes()
    
    while True:
        time.sleep(0.35)
        current_mtimes = get_file_mtimes()
        changed_files = []

        for path, mtime in current_mtimes.items():
            if path not in last_mtimes or mtime > last_mtimes[path]:
                changed_files.append(os.path.relpath(path, BASE_DIR))

        for path in last_mtimes:
            if path not in current_mtimes:
                changed_files.append(os.path.relpath(path, BASE_DIR))

        if changed_files:
            last_mtimes = current_mtimes
            changed_display = ', '.join(changed_files[:3])
            if len(changed_files) > 3:
                changed_display += f' (+{len(changed_files) - 3} lainnya)'

            print(f"\033[93m[⚡ LIVE RELOAD]\033[0m Perubahan terdeteksi: \033[96m{changed_display}\033[0m -> Merefresh browser!")

            with clients_lock:
                dead_clients = []
                for q in clients:
                    try:
                        q.put_nowait('reload')
                    except Exception:
                        dead_clients.append(q)
                for q in dead_clients:
                    if q in clients:
                        clients.remove(q)

class CyberLiveRequestHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=BASE_DIR, **kwargs)

    def log_message(self, format, *args):
        # Suppress spammy log for SSE stream requests
        if args and len(args) > 0 and '/__live_reload_stream' in str(args[0]):
            return
        # Cyberpunk style logging for standard requests
        status_str = str(args[1]) if len(args) > 1 else '200'
        if status_str.startswith('2'):
            color = '\033[92m'
        elif status_str.startswith('3'):
            color = '\033[96m'
        else:
            color = '\033[91m'
        print(f"\033[90m[{time.strftime('%H:%M:%S')}]\033[0m {color}{status_str}\033[0m {args[0]}")

    def end_headers(self):
        # Add No-Cache headers to prevent browser from caching stale files during dev
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        self.send_header('Access-Control-Allow-Origin', '*')
        super().end_headers()

    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)

        # Handle SSE Live Reload Stream
        if parsed.path == '/__live_reload_stream':
            self.send_response(200)
            self.send_header('Content-Type', 'text/event-stream')
            self.send_header('Cache-Control', 'no-cache, no-transform')
            self.send_header('Connection', 'keep-alive')
            self.send_header('X-Accel-Buffering', 'no')
            self.end_headers()

            q = queue.Queue()
            with clients_lock:
                clients.append(q)

            try:
                # Send initial handshake heartbeat
                self.wfile.write(b"retry: 1000\ndata: connected\n\n")
                self.wfile.flush()

                while True:
                    try:
                        msg = q.get(timeout=15.0)
                        self.wfile.write(f"data: {msg}\n\n".encode('utf-8'))
                        self.wfile.flush()
                    except queue.Empty:
                        # Keep-alive ping
                        self.wfile.write(b": ping\n\n")
                        self.wfile.flush()
            except (BrokenPipeError, ConnectionResetError, OSError):
                pass
            finally:
                with clients_lock:
                    if q in clients:
                        clients.remove(q)
            return

        # Default static file serving
        return super().do_GET()

class ThreadingTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    allow_reuse_address = True
    daemon_threads = True

def main():
    # Start File Watcher Thread
    watcher_thread = threading.Thread(target=watch_directory_loop, daemon=True)
    watcher_thread.start()

    banner = (
        "\033[93m╔═════════════════════════════════════════════════════════════════════════════╗\n"
        "║   ⚡ CYBERPUNK 2077 - ZERO-LATENCY LIVE RELOAD SERVER (v2.077)               ║\n"
        "╠═════════════════════════════════════════════════════════════════════════════╣\n"
        f"║  🌐 Portofolio Utama : \033[96mhttp://localhost:{PORT}\033[93m                                      ║\n"
        f"║  🔒 Admin Command Deck: \033[96mhttp://localhost:{PORT}/admin.html\033[93m                           ║\n"
        "║  ⚡ Live Hot Reload  : \033[92mAKTIF & STANDBY\033[93m (Auto-refresh saat file diedit)         ║\n"
        "║  🛡️ Cache Bypass     : \033[92mAKTIF\033[93m (No-Cache headers terpasang)                     ║\n"
        "╚═════════════════════════════════════════════════════════════════════════════╝\033[0m"
    )

    print(banner)
    print("\033[90m[INFO] Tekan Ctrl + C di terminal untuk menghentikan server.\033[0m\n")

    try:
        with ThreadingTCPServer(('0.0.0.0', PORT), CyberLiveRequestHandler) as httpd:
            httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n\033[91m[TERMINAL] Server dihentikan oleh pengguna. Sampai jumpa di Night City!\033[0m")
        sys.exit(0)
    except OSError as e:
        if e.errno == 98: # Address already in use
            print(f"\033[91m[ERROR] Port {PORT} sedang digunakan oleh proses lain!\033[0m")
            print(f"Gunakan perintah: python3 live_server.py {PORT + 1} atau matikan server lama.")
        else:
            print(f"\033[91m[ERROR]\033[0m {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()
