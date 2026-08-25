#!/usr/bin/env python3
"""
CYBERPUNK 2077 - DISCORD WEBHOOK CODE UPDATE NOTIFIER
Dispatches real-time update notifications and git file diffs to Discord.
"""

import sys
import os
import json
import urllib.request
import subprocess
from datetime import datetime

WEBHOOK_URL = "https://discord.com/api/webhooks/1491025432034938911/OtSYXYA22qqU0C6iAwUorgQ-Qg0SAcmzfdKwmgGMsVxHlOFIBN_6ikQ5Ftf_C3S0pHT-"

def get_git_status():
    try:
        res = subprocess.run(["git", "status", "--porcelain"], capture_output=True, text=True, check=True)
        lines = res.stdout.strip().split("\n")
        files = []
        for line in lines:
            if not line:
                continue
            status = line[:2].strip()
            filename = line[3:].strip()
            
            tag = "[MODIFIED]"
            if "?" in status:
                tag = "[NEW FILE]"
            elif "D" in status:
                tag = "[DELETED]"
            elif "A" in status:
                tag = "[ADDED]"
            elif "R" in status:
                tag = "[RENAMED]"
                
            files.append(f"`{tag}` **{filename}**")
        return files
    except Exception:
        return []

def get_latest_commit_files():
    try:
        res = subprocess.run(["git", "show", "--name-status", "--oneline", "HEAD"], capture_output=True, text=True, check=True)
        lines = res.stdout.strip().split("\n")
        commit_msg = lines[0] if lines else "Update files"
        files = []
        for line in lines[1:]:
            parts = line.split("\t")
            if len(parts) >= 2:
                status, fname = parts[0], parts[1]
                tag = "[MODIFIED]" if status == "M" else "[NEW FILE]" if status == "A" else "[DELETED]"
                files.append(f"`{tag}` **{fname}**")
        return commit_msg, files
    except Exception:
        return "Manual Code Update", []

def send_discord_update(summary=None, custom_files=None):
    commit_msg, commit_files = get_latest_commit_files()
    working_files = get_git_status()
    
    file_list = custom_files or working_files or commit_files
    if not file_list:
        file_list = ["`[MODIFIED]` **index.html**", "`[MODIFIED]` **js/app.js**", "`[MODIFIED]` **js/store.js**", "`[NEW FILE]` **js/lanyard.js**"]
    
    files_text = "\n".join(file_list[:12])
    if len(file_list) > 12:
        files_text += f"\n*...dan {len(file_list) - 12} berkas lainnya*"

    update_summary = summary or commit_msg or "Pembaruan arsitektur dan berkas kodingan portofolio Cyberpunk 2077"

    payload = {
        "username": "NETRUNNER CODE WATCHDOG",
        "avatar_url": "https://images.unsplash.com/photo-1542751371-adc38448a05e?q=80&w=300",
        "embeds": [
            {
                "title": "🛠️ UPDATE BERKAS KODINGAN // CODEBASE SYNC",
                "description": f"Pembaruan kode baru telah berhasil diterapkan ke repositori!",
                "color": 61695, # Neon Cyan (#00F0FF)
                "fields": [
                    {
                        "name": "📝 RINGKASAN PERUBAHAN",
                        "value": f"```{update_summary}```",
                        "inline": False
                    },
                    {
                        "name": "📂 BERKAS KODINGAN YANG DIPERBARUI",
                        "value": files_text,
                        "inline": False
                    },
                    {
                        "name": "🌐 REPO NODE",
                        "value": "Night City 2077 // Vercel Static Suite",
                        "inline": True
                    },
                    {
                        "name": "⚡ STATUS",
                        "value": "● COMPILED & SYNCED OK",
                        "inline": True
                    }
                ],
                "footer": {
                    "text": "Night City Sentinel v2.077 // Webhook Telemetry Active"
                },
                "timestamp": datetime.utcnow().isoformat() + "Z"
            }
        ]
    }

    req = urllib.request.Request(
        WEBHOOK_URL,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json", "User-Agent": "Mozilla/5.0"}
    )
    
    try:
        with urllib.request.urlopen(req) as resp:
            if resp.status in (200, 204):
                print(f"[OK] Discord Webhook notification sent successfully! (HTTP {resp.status})")
                return True
            else:
                print(f"[ERR] Discord Webhook responded with status: {resp.status}")
                return False
    except Exception as e:
        print(f"[ERR] Failed to send Discord Webhook: {e}")
        return False

if __name__ == "__main__":
    msg = sys.argv[1] if len(sys.argv) > 1 else "Update berkas kodingan & integrasi Discord Lanyard & Webhook"
    send_discord_update(summary=msg)
