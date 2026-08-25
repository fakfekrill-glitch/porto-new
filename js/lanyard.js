/**
 * CYBERPUNK 2077 - LANYARD DISCORD RICH PRESENCE ENGINE (v2.077)
 * Connects to Lanyard WebSocket & REST API for Discord User ID: 582206666431266816
 * Shows Discord avatar & presence completely separate from portfolio profile image.
 * Real-time media player (YouTube Music, Spotify, YouTube, etc.) with live timeline bar.
 */

class CyberLanyard {
  constructor() {
    this.userId = "582206666431266816";
    this.ws = null;
    this.heartbeatInterval = null;
    this.pollInterval = null;
    this.timelineTimer = null;
    this.currentData = null;
    this.activeActivity = null;

    this.init();
  }

  init() {
    // 1. Initial REST fetch for instant display without waiting for WS handshake
    this.fetchRestData();

    // 2. Connect WebSocket for 0-latency live updates
    this.connectWebSocket();

    // 3. Fallback Polling every 10 seconds
    this.pollInterval = setInterval(() => {
      if (!this.ws || this.ws.readyState !== WebSocket.OPEN) {
        this.fetchRestData();
      }
    }, 10000);

    // 4. Live Timeline updater every 500ms
    this.timelineTimer = setInterval(() => {
      this.updateTimelineTick();
    }, 500);
  }

  // REST API Fetch
  async fetchRestData() {
    try {
      const res = await fetch(`https://api.lanyard.rest/v1/users/${this.userId}`);
      const json = await res.json();
      if (json && json.success && json.data) {
        this.handlePresenceUpdate(json.data);
      }
    } catch (err) {
      console.warn("[LANYARD] REST fetch warning:", err.message);
    }
  }

  // WebSocket Connection
  connectWebSocket() {
    try {
      this.ws = new WebSocket("wss://api.lanyard.rest/socket");

      this.ws.onopen = () => {
        // Connected
      };

      this.ws.onmessage = (event) => {
        try {
          const message = JSON.parse(event.data);
          const { op, t, d } = message;

          switch (op) {
            case 1: // Hello -> Setup Heartbeat & Initialize
              const interval = d.heartbeat_interval;
              if (this.heartbeatInterval) clearInterval(this.heartbeatInterval);
              this.heartbeatInterval = setInterval(() => {
                if (this.ws && this.ws.readyState === WebSocket.OPEN) {
                  this.ws.send(JSON.stringify({ op: 3 }));
                }
              }, interval);

              // Subscribe to user presence
              this.ws.send(
                JSON.stringify({
                  op: 2,
                  d: {
                    subscribe_to_id: this.userId
                  }
                })
              );
              break;

            case 0: // Event Dispatch
              if (t === "INIT_STATE" || t === "PRESENCE_UPDATE") {
                this.handlePresenceUpdate(d);
              }
              break;
          }
        } catch (err) {
          console.warn("[LANYARD] WS Message error:", err);
        }
      };

      this.ws.onerror = () => {
        // Handled by onclose
      };

      this.ws.onclose = () => {
        if (this.heartbeatInterval) clearInterval(this.heartbeatInterval);
        // Reconnect after 5 seconds
        setTimeout(() => this.connectWebSocket(), 5000);
      };
    } catch (err) {
      console.warn("[LANYARD] WS Connection error:", err);
    }
  }

  // Asset URL Resolver
  resolveAssetUrl(assetKey, applicationId) {
    if (!assetKey) return null;
    if (assetKey.startsWith("mp:")) {
      return `https://media.discordapp.net/${assetKey.slice(3)}`;
    }
    if (assetKey.startsWith("spotify:")) {
      return `https://i.scdn.co/image/${assetKey.slice(8)}`;
    }
    if (assetKey.startsWith("http://") || assetKey.startsWith("https://")) {
      return assetKey;
    }
    if (applicationId) {
      return `https://cdn.discordapp.com/app-assets/${applicationId}/${assetKey}.png`;
    }
    return null;
  }

  // Presence State Handler
  handlePresenceUpdate(data) {
    this.currentData = data;

    // Extract Primary Activity (Spotify or Rich Presence Activities)
    let primaryActivity = null;

    if (data.listening_to_spotify && data.spotify) {
      primaryActivity = {
        type: 'spotify',
        platform: 'Spotify',
        platformIcon: '🎵',
        title: data.spotify.song,
        artist: data.spotify.artist,
        album: data.spotify.album,
        image: data.spotify.album_art_url,
        url: data.spotify.track_id ? `https://open.spotify.com/track/${data.spotify.track_id}` : 'https://open.spotify.com',
        timestamps: data.spotify.timestamps,
        isPlaying: true
      };
    } else if (data.activities && data.activities.length > 0) {
      const meaningfulActivities = data.activities.filter((a) => a.type !== 4);
      const act = meaningfulActivities.length > 0 ? meaningfulActivities[0] : data.activities[0];

      if (act) {
        let platformName = act.name || 'Discord Activity';
        let platformIcon = '⚡';
        let isMusicOrVideo = false;

        const lowerName = platformName.toLowerCase();
        if (lowerName.includes('youtube music')) {
          platformIcon = '🎧';
          isMusicOrVideo = true;
        } else if (lowerName.includes('youtube')) {
          platformIcon = '📺';
          isMusicOrVideo = true;
        } else if (lowerName.includes('spotify')) {
          platformIcon = '🎵';
          isMusicOrVideo = true;
        } else if (lowerName.includes('code') || lowerName.includes('studio')) {
          platformIcon = '💻';
        } else if (act.type === 0) {
          platformIcon = '🎮';
        } else if (act.type === 2) {
          platformIcon = '🎧';
          isMusicOrVideo = true;
        } else if (act.type === 3) {
          platformIcon = '🎬';
          isMusicOrVideo = true;
        }

        let imageUrl = null;
        if (act.assets && act.assets.large_image) {
          imageUrl = this.resolveAssetUrl(act.assets.large_image, act.application_id);
        } else if (act.assets && act.assets.small_image) {
          imageUrl = this.resolveAssetUrl(act.assets.small_image, act.application_id);
        }

        let targetUrl = act.details_url || act.state_url;
        if (!targetUrl && act.assets && act.assets.large_url) {
          targetUrl = act.assets.large_url;
        }

        primaryActivity = {
          type: 'activity',
          platform: platformName,
          platformIcon,
          title: act.details || act.name || 'Aktivitas Discord',
          artist: act.state || (act.assets && act.assets.large_text) || '',
          image: imageUrl,
          url: targetUrl || '#',
          timestamps: act.timestamps || null,
          isPlaying: isMusicOrVideo || act.type === 2
        };
      }
    }

    this.activeActivity = primaryActivity;
    this.renderActivityWidget(primaryActivity, data);
  }

  // Render Activity Widget in Hero Section
  renderActivityWidget(activity, data) {
    let widget = document.getElementById('discord-live-widget');
    if (!widget) {
      const heroContent = document.querySelector('.hero-content');
      if (!heroContent) return;

      widget = document.createElement('div');
      widget.id = 'discord-live-widget';
      widget.className = 'cyber-activity-widget';

      const heroActions = document.querySelector('.hero-actions');
      if (heroActions) {
        heroContent.insertBefore(widget, heroActions);
      } else {
        heroContent.appendChild(widget);
      }
    }

    const discordUser = data.discord_user || {};
    const displayName = discordUser.global_name || discordUser.display_name || discordUser.username || 'Pushy Meong';
    const username = discordUser.username || 'pushygamertag27';
    const status = data.discord_status || 'offline';

    // Discord Avatar URL
    let discordAvatar = 'https://assets-global.website-files.com/6257adef93867e50d84d30e2/636e0a6a49cf127bf92de1e2_icon_clyde_blurple_RGB.png';
    if (discordUser.id && discordUser.avatar) {
      discordAvatar = `https://cdn.discordapp.com/avatars/${discordUser.id}/${discordUser.avatar}.${discordUser.avatar.startsWith('a_') ? 'gif' : 'png'}?size=128`;
    }

    let statusPill = `<span class="activity-status-pill status-${status}">● ${status.toUpperCase()}</span>`;

    if (!activity) {
      // Idle State: Displays Discord Profile & Avatar + Idle Notice
      widget.innerHTML = `
        <div class="activity-discord-profile-row">
          <div class="activity-discord-avatar-wrap">
            <img src="${discordAvatar}" alt="${displayName}" class="activity-discord-avatar-img" />
            <span class="activity-discord-status-dot status-${status}"></span>
          </div>
          <div class="activity-discord-user-info">
            <div class="activity-discord-name">${displayName}</div>
            <div class="activity-discord-handle">@${username}</div>
          </div>
          <div style="margin-left: auto;">
            ${statusPill}
          </div>
        </div>

        <div class="activity-idle-body">
          <div class="activity-idle-icon">⚡</div>
          <div class="activity-idle-text">
            <div style="color: #FFF; font-family: var(--font-display); font-size: 0.95rem;">DISCORD NEURAL LINK: CONNECTED</div>
            <div style="color: var(--text-muted); font-size: 0.8rem; font-family: var(--font-mono);">Tidak ada musik atau video yang sedang diputar saat ini.</div>
          </div>
        </div>
      `;
      return;
    }

    // Active Media State: Displays Discord Profile + Media Player Card
    const fallbackImage = `data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><rect width="100" height="100" fill="%230F131D"/><text x="50" y="55" fill="%2300F0FF" font-size="30" text-anchor="middle" dominant-baseline="middle">🎵</text></svg>`;
    const mediaImg = activity.image || fallbackImage;

    const isLink = activity.url && activity.url !== '#';
    const linkTarget = isLink ? `href="${activity.url}" target="_blank" rel="noopener noreferrer"` : '';
    const clickHint = isLink ? 'title="Klik untuk membuka link langsung ↗"' : '';

    widget.innerHTML = `
      <!-- 1. DISCORD PROFILE ROW (Separate from Portfolio Avatar) -->
      <div class="activity-discord-profile-row">
        <div class="activity-discord-avatar-wrap">
          <img src="${discordAvatar}" alt="${displayName}" class="activity-discord-avatar-img" />
          <span class="activity-discord-status-dot status-${status}"></span>
        </div>
        <div class="activity-discord-user-info">
          <div class="activity-discord-name">${displayName}</div>
          <div class="activity-discord-handle">@${username}</div>
        </div>
        <div style="margin-left: auto; display: flex; gap: 8px; align-items: center;">
          ${activity.isPlaying ? `
            <div class="cyber-equalizer-bars">
              <span class="bar bar-1"></span>
              <span class="bar bar-2"></span>
              <span class="bar bar-3"></span>
              <span class="bar bar-4"></span>
            </div>
          ` : ''}
          ${statusPill}
        </div>
      </div>

      <!-- 2. NOW PLAYING / STREAMING MEDIA CARD -->
      <div class="activity-media-card">
        <div class="activity-platform-badge-row">
          <span class="activity-platform-tag">${activity.platformIcon} ${activity.platform.toUpperCase()}</span>
          <span class="activity-live-status-tag">● LIVE STREAM</span>
        </div>

        <div class="activity-body">
          <!-- Clickable Thumbnail / Album Art -->
          <a ${linkTarget} ${clickHint} class="activity-media-box">
            <img src="${mediaImg}" alt="${activity.title}" />
            ${isLink ? `<div class="activity-media-hover-overlay"><span>↗</span></div>` : ''}
          </a>

          <!-- Track & Media Info -->
          <div class="activity-info">
            <div class="activity-track-title">
              ${isLink ? `<a ${linkTarget} ${clickHint} class="activity-title-link">${activity.title}</a>` : `<span>${activity.title}</span>`}
            </div>
            
            ${activity.artist ? `<div class="activity-track-artist">${activity.artist}</div>` : ''}

            <!-- Real-Time Timeline Progress Bar -->
            <div class="activity-timeline-container" id="activity-timeline-box" style="${activity.timestamps ? 'display: block;' : 'display: none;'}">
              <div class="activity-progress-bar">
                <div class="activity-progress-fill" id="activity-progress-fill" style="width: 0%;"></div>
              </div>
              <div class="activity-timestamps">
                <span id="activity-time-current">00:00</span>
                <span id="activity-time-total">00:00</span>
              </div>
            </div>
          </div>
        </div>

        ${isLink ? `
          <div class="activity-footer-action">
            <a ${linkTarget} class="activity-direct-btn">
              <span>${activity.platformIcon} BUKA DI ${activity.platform.toUpperCase()}</span>
              <span>↗</span>
            </a>
          </div>
        ` : ''}
      </div>
    `;

    // Immediately trigger timeline update
    this.updateTimelineTick();
  }

  // Format Milliseconds to MM:SS
  formatTime(ms) {
    if (!ms || isNaN(ms) || ms < 0) return "00:00";
    const totalSeconds = Math.floor(ms / 1000);
    const minutes = Math.floor(totalSeconds / 60);
    const seconds = totalSeconds % 60;
    return `${String(minutes).padStart(2, '0')}:${String(seconds).padStart(2, '0')}`;
  }

  // Real-time Timeline Progress Tick
  updateTimelineTick() {
    if (!this.activeActivity || !this.activeActivity.timestamps) return;

    const timestamps = this.activeActivity.timestamps;
    const progressFill = document.getElementById('activity-progress-fill');
    const timeCurrent = document.getElementById('activity-time-current');
    const timeTotal = document.getElementById('activity-time-total');

    if (!progressFill || !timeCurrent || !timeTotal) return;

    const now = Date.now();
    const start = timestamps.start;
    const end = timestamps.end;

    if (start && end) {
      const totalDuration = end - start;
      const currentElapsed = Math.min(Math.max(now - start, 0), totalDuration);
      const percentage = Math.min(Math.max((currentElapsed / totalDuration) * 100, 0), 100);

      progressFill.style.width = `${percentage}%`;
      timeCurrent.textContent = this.formatTime(currentElapsed);
      timeTotal.textContent = this.formatTime(totalDuration);
    } else if (start && !end) {
      const currentElapsed = Math.max(now - start, 0);
      progressFill.style.width = `100%`;
      timeCurrent.textContent = this.formatTime(currentElapsed);
      timeTotal.textContent = `LIVE`;
    }
  }
}

// Instantiate on DOM Ready
document.addEventListener('DOMContentLoaded', () => {
  window.cyberLanyard = new CyberLanyard();
});
