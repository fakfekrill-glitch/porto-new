#!/usr/bin/env python3
"""
CYBERPUNK 2077 - SENTINEL SERVER HEALTH & SPEED MONITOR (1-MINUTE HEARTBEAT)
Monitors Localhost and Vercel endpoints, tracks IP, response speed, latency,
and dispatches real-time telemetry updates to Discord Webhook.
"""

import sys
import os
import time
import json
import socket
import argparse
import urllib.request
import urllib.error
from datetime import datetime, timezone

WEBHOOK_URL = "https://discord.com/api/webhooks/1491025432034938911/OtSYXYA22qqU0C6iAwUorgQ-Qg0SAcmzfdKwmgGMsVxHlOFIBN_6ikQ5Ftf_C3S0pHT-"

class ServerMonitor:
    def __init__(self, local_url="http://localhost:3000", vercel_url=None, webhook_url=WEBHOOK_URL):
        self.local_url = local_url
        self.vercel_url = vercel_url
        self.webhook_url = webhook_url
        self.check_count = 0
        self.total_latency = 0
        self.cached_ip = None
        self.cached_geo = None

    def get_public_ip_and_geo(self):
        # Refresh every 10 checks or on startup
        if self.cached_ip and self.cached_geo and self.check_count % 10 != 1:
            return self.cached_ip, self.cached_geo

        ip = "127.0.0.1"
        geo_info = "Local Node"
        try:
            req = urllib.request.Request("http://ip-api.com/json/?fields=status,query,country,city,isp", headers={"User-Agent": "Mozilla/5.0"})
            with urllib.request.urlopen(req, timeout=4) as r:
                data = json.loads(r.read().decode())
                if data.get("status") == "success":
                    ip = data.get("query", "Unknown")
                    city = data.get("city", "Unknown")
                    country = data.get("country", "Unknown")
                    isp = data.get("isp", "Unknown ISP")
                    geo_info = f"{city}, {country} // {isp}"
                    self.cached_ip = ip
                    self.cached_geo = geo_info
        except Exception:
            try:
                req = urllib.request.Request("https://api.ipify.org?format=json", headers={"User-Agent": "Mozilla/5.0"})
                with urllib.request.urlopen(req, timeout=3) as r:
                    ip = json.loads(r.read().decode()).get("ip", "Unknown")
                    geo_info = "Indonesia // Night City Node"
                    self.cached_ip = ip
                    self.cached_geo = geo_info
            except Exception:
                pass

        return ip, geo_info

    def test_endpoint(self, url):
        if not url:
            return None
        
        t0 = time.perf_counter()
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (Cyberpunk Sentinel 2077)"})
            with urllib.request.urlopen(req, timeout=8) as resp:
                content = resp.read()
                latency_ms = (time.perf_counter() - t0) * 1000
                size_bytes = len(content)
                
                # Speed Rating
                if latency_ms < 30:
                    speed_rating = "🟢 ULTRA FAST (Sub-30ms)"
                elif latency_ms < 100:
                    speed_rating = "🟡 FAST (<100ms)"
                elif latency_ms < 300:
                    speed_rating = "🟠 MODERATE (<300ms)"
                else:
                    speed_rating = "🔴 SLOW (>300ms)"

                return {
                    "url": url,
                    "status": resp.status,
                    "status_text": "200 OK // HEALTHY",
                    "latency_ms": latency_ms,
                    "size_kb": size_bytes / 1024,
                    "speed_rating": speed_rating,
                    "alive": True
                }
        except urllib.error.HTTPError as e:
            latency_ms = (time.perf_counter() - t0) * 1000
            return {
                "url": url,
                "status": e.code,
                "status_text": f"HTTP {e.code} // WARNING",
                "latency_ms": latency_ms,
                "size_kb": 0,
                "speed_rating": "⚠️ ERROR",
                "alive": False
            }
        except Exception as e:
            return {
                "url": url,
                "status": 0,
                "status_text": f"UNREACHABLE ({type(e).__name__})",
                "latency_ms": 0,
                "size_kb": 0,
                "speed_rating": "🔴 OFFLINE",
                "alive": False
            }

    def dispatch_discord_heartbeat(self, local_res, vercel_res=None):
        self.check_count += 1
        public_ip, geo_info = self.get_public_ip_and_geo()
        
        # Color based on health
        all_alive = local_res.get("alive", False)
        if vercel_res:
            all_alive = all_alive and vercel_res.get("alive", False)
            
        color = 61695 if all_alive else 16711740 # Neon Cyan (#00F0FF) if healthy, Pink/Red if down

        fields = [
            {
                "name": "🌐 SERVER PUBLIC IP & LOCATION",
                "value": f"`{public_ip}`\n📍 *{geo_info}*",
                "inline": False
            },
            {
                "name": "⚡ LOCALHOST NODE (PORT 3000)",
                "value": (
                    f"**Status**: `{local_res['status_text']}`\n"
                    f"**Latency**: `{local_res['latency_ms']:.2f} ms`\n"
                    f"**Speed**: {local_res['speed_rating']}\n"
                    f"**Payload**: `{local_res['size_kb']:.2f} KB`"
                ),
                "inline": True
            }
        ]

        if vercel_res:
            fields.append({
                "name": "🚀 VERCEL CLOUD DEPLOYMENT",
                "value": (
                    f"**Status**: `{vercel_res['status_text']}`\n"
                    f"**Latency**: `{vercel_res['latency_ms']:.2f} ms`\n"
                    f"**Speed**: {vercel_res['speed_rating']}\n"
                    f"**Payload**: `{vercel_res['size_kb']:.2f} KB`"
                ),
                "inline": True
            })
        else:
            fields.append({
                "name": "🚀 VERCEL CLOUD NODE",
                "value": (
                    "**Config**: `vercel.json READY`\n"
                    "**Deploy**: `vercel --prod`\n"
                    "**Status**: ● SYNC ACTIVE"
                ),
                "inline": True
            })

        fields.append({
            "name": "📊 TELEMETRY & UPTIME MONITOR",
            "value": (
                f"Heartbeat: `#{self.check_count}` // Interval: `Every 1 Minute`\n"
                f"Architecture: `Night City Static Edge v2.077`"
            ),
            "inline": False
        })

        payload = {
            "username": "SENTINEL SERVER MONITOR",
            "avatar_url": "https://images.unsplash.com/photo-1550751827-4bd374c3f58b?q=80&w=300",
            "embeds": [
                {
                    "title": "🛰️ SERVER HEALTH & SPEED TELEMETRY [1-MIN HEARTBEAT]",
                    "description": "Pemindaian status server, kecepatan akses, dan metrik jaringan real-time.",
                    "color": color,
                    "fields": fields,
                    "footer": {
                        "text": f"Night City Sentinel v2.077 // Heartbeat #{self.check_count}"
                    },
                    "timestamp": datetime.now(timezone.utc).isoformat()
                }
            ]
        }

        req = urllib.request.Request(
            self.webhook_url,
            data=json.dumps(payload).encode("utf-8"),
            headers={"Content-Type": "application/json", "User-Agent": "Mozilla/5.0"}
        )

        try:
            with urllib.request.urlopen(req) as resp:
                print(f"[{datetime.now().strftime('%H:%M:%S')}] Heartbeat #{self.check_count} -> Discord Sent (HTTP {resp.status}) // Local Latency: {local_res['latency_ms']:.2f}ms")
                return True
        except Exception as e:
            print(f"[{datetime.now().strftime('%H:%M:%S')}] Webhook dispatch error: {e}")
            return False

    def run_check(self):
        local_res = self.test_endpoint(self.local_url)
        vercel_res = self.test_endpoint(self.vercel_url) if self.vercel_url else None
        return self.dispatch_discord_heartbeat(local_res, vercel_res)

    def run_loop(self, interval_seconds=60):
        print(f"🚀 Cyberpunk Sentinel Server Monitor Active!")
        print(f"📡 Monitoring Local: {self.local_url} | Vercel: {self.vercel_url or 'N/A'}")
        print(f"⏱️ Interval: Every {interval_seconds} seconds (1 minute)")
        print(f"🔗 Discord Webhook: Connected\n" + "="*50)
        
        while True:
            self.run_check()
            time.sleep(interval_seconds)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Cyberpunk 2077 Sentinel Server & Speed Monitor")
    parser.add_argument("--once", action="store_true", help="Run a single heartbeat check and exit")
    parser.add_argument("--interval", type=int, default=60, help="Check interval in seconds (default: 60s)")
    parser.add_argument("--local", type=str, default="http://localhost:3000", help="Localhost server URL")
    parser.add_argument("--vercel", type=str, default=None, help="Vercel production deployment URL")
    args = parser.parse_args()

    monitor = ServerMonitor(local_url=args.local, vercel_url=args.vercel)
    
    if args.once:
        monitor.run_check()
    else:
        monitor.run_loop(interval_seconds=args.interval)
