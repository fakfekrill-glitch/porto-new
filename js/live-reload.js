/**
 * CYBERPUNK 2077 - CLIENT LIVE REFRESH & HOT RELOAD ENGINE (v2.077)
 * Listens for Server-Sent Events (SSE) from live_server.py.
 * Automatically refreshes browser when any file changes, preserving scroll position.
 */

(function () {
  'use strict';

  // Only enable on localhost / 127.0.0.1 or non-production
  const isLocal = window.location.hostname === 'localhost' || 
                  window.location.hostname === '127.0.0.1' || 
                  window.location.hostname.startsWith('192.168.') ||
                  window.location.hostname.startsWith('10.');

  if (!isLocal) return;

  // Restore Scroll Position after live reload
  const savedScroll = sessionStorage.getItem('cp_live_scroll_y');
  if (savedScroll !== null) {
    sessionStorage.removeItem('cp_live_scroll_y');
    window.addEventListener('DOMContentLoaded', () => {
      setTimeout(() => {
        window.scrollTo({ top: parseInt(savedScroll, 10), behavior: 'instant' });
      }, 50);
    });
  }

  let eventSource = null;
  let reconnectTimer = null;
  let isReloading = false;

  function connectLiveReload() {
    if (eventSource) {
      try { eventSource.close(); } catch (_) {}
    }

    try {
      eventSource = new EventSource('/__live_reload_stream');

      eventSource.onopen = function () {
        console.log(
          '%c[⚡ CYBER LIVE RELOAD]%c Neural Stream Connected & Standby',
          'color: #00F0FF; font-weight: bold; background: #080C14; padding: 2px 6px; border: 1px solid #00F0FF;',
          'color: #FCEE0A; font-family: monospace;'
        );
        if (reconnectTimer) {
          clearTimeout(reconnectTimer);
          reconnectTimer = null;
        }
      };

      eventSource.onmessage = function (e) {
        if (e.data === 'reload' && !isReloading) {
          isReloading = true;
          sessionStorage.setItem('cp_live_scroll_y', window.scrollY || window.pageYOffset || 0);

          // Visual Cyber Toast if available
          if (typeof window.showCyberToast === 'function') {
            window.showCyberToast('⚡ LIVE UPDATE: File berubah, merefresh browser...', 'cyan');
          } else if (typeof window.showAdminToast === 'function') {
            window.showAdminToast('⚡ LIVE UPDATE: File berubah, merefresh browser...', 'cyan');
          }

          setTimeout(() => {
            window.location.reload();
          }, 150);
        }
      };

      eventSource.onerror = function () {
        // Server might be restarting, retry silently
        if (eventSource) {
          eventSource.close();
          eventSource = null;
        }
        if (!reconnectTimer) {
          reconnectTimer = setTimeout(connectLiveReload, 2000);
        }
      };
    } catch (err) {
      // EventSource not supported or blocked
      console.debug('[LIVE_RELOAD] Not available:', err.message);
    }
  }

  // Initialize connection
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', connectLiveReload);
  } else {
    connectLiveReload();
  }
})();
