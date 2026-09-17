/**
 * CYBERPUNK 2077 PORTFOLIO SYSTEM - MAIN APPLICATION ENGINE (PUBLIC SUITE)
 * Night City Protocol v2.077
 */

document.addEventListener('DOMContentLoaded', () => {
  // Initialize Core Systems
  initUI();
  initTelemetryClock();
  initContactForm();
  initAudioControls();
  initFilters();
  initCardTilts();
  initTerminal();

  // Initial UI Render from Store
  renderAllUI();
});

// Toast System
window.showCyberToast = function (message, type = 'yellow') {
  const container = document.getElementById('toast-container');
  if (!container) return;

  const toast = document.createElement('div');
  toast.className = `cyber-toast ${type === 'cyan' ? 'toast-cyan' : type === 'pink' ? 'toast-pink' : ''}`;
  
  let icon = '⚡';
  if (type === 'cyan') icon = '🛡️';
  if (type === 'pink') icon = '⚠️';

  toast.innerHTML = `<span>${icon}</span> <div>${message}</div>`;
  container.appendChild(toast);

  setTimeout(() => {
    toast.style.opacity = '0';
    toast.style.transform = 'translateX(100%)';
    toast.style.transition = 'all 0.3s ease';
    setTimeout(() => toast.remove(), 300);
  }, 4000);
};

// Render All Components
function renderAllUI() {
  window.renderProfileUI();
  window.renderArsenalUI('all');
  window.renderProjectsUI();
  window.renderCertificatesUI('all');
  window.renderDocumentationUI();
}

// Helper sanitizers for Public UI
const esc = (s) => (window.cyberSecurity ? window.cyberSecurity.escapeHTML(s) : String(s || ''));
const safeUrl = (u) => (window.cyberSecurity ? window.cyberSecurity.sanitizeURL(u) : u || '#');

// 1. PROFILE UI RENDER
window.renderProfileUI = function () {
  const profile = window.cyberStore.getProfile();
  
  const nameEl = document.getElementById('hero-display-name');
  if (nameEl) {
    const cleanName = esc(profile.name);
    nameEl.innerHTML = `<span>[V]</span> ${cleanName}`;
    nameEl.setAttribute('data-text', `[V] ${cleanName}`);
  }

  const roleEl = document.getElementById('hero-display-role');
  if (roleEl) {
    roleEl.innerHTML = `<span class="typing-text">${esc(profile.title)}</span><span class="typing-cursor"></span>`;
  }

  const bioEl = document.getElementById('hero-display-bio');
  if (bioEl) {
    bioEl.textContent = profile.bio || '';
  }
  
  const avatarImg = document.getElementById('profile-avatar-img');
  if (avatarImg && profile.avatar) {
    avatarImg.src = safeUrl(profile.avatar);
  }

  // Update Contact Info
  if (profile.steam) {
    const steamLink = document.getElementById('contact-steam-link');
    const steamVal = document.getElementById('contact-steam-val');
    const steamTarget = profile.steam.startsWith('http') ? profile.steam : `https://steamcommunity.com/id/${profile.steam}`;
    if (steamLink) steamLink.href = safeUrl(steamTarget);
    if (steamVal) {
      const parts = profile.steam.split('/').filter(Boolean);
      steamVal.textContent = parts[parts.length - 1] || profile.steam;
    }
  }

  if (profile.instagram) {
    const igLink = document.getElementById('contact-instagram-link');
    const igVal = document.getElementById('contact-instagram-val');
    const igTarget = profile.instagram.startsWith('http') ? profile.instagram : `https://instagram.com/${profile.instagram.replace('@', '')}`;
    if (igLink) igLink.href = safeUrl(igTarget);
    if (igVal) {
      const parts = profile.instagram.split('/').filter(Boolean);
      const handle = parts[parts.length - 1] || profile.instagram;
      igVal.textContent = handle.startsWith('@') ? handle : `@${handle}`;
    }
  }

  if (profile.facebook) {
    const fbLink = document.getElementById('contact-facebook-link');
    const fbVal = document.getElementById('contact-facebook-val');
    const fbTarget = profile.facebook.startsWith('http') ? profile.facebook : `https://facebook.com/${profile.facebook}`;
    if (fbLink) fbLink.href = safeUrl(fbTarget);
    if (fbVal) {
      const parts = profile.facebook.split('/').filter(Boolean);
      fbVal.textContent = parts[parts.length - 1] || 'facebook.com';
    }
  }

  if (profile.email) {
    const emailLink = document.getElementById('contact-email-link');
    const emailVal = document.getElementById('contact-email-val');
    if (emailLink) emailLink.href = `mailto:${encodeURIComponent(profile.email)}`;
    if (emailVal) emailVal.textContent = profile.email;
  }

  if (profile.discord) {
    const discordVal = document.getElementById('contact-discord-val');
    if (discordVal) discordVal.textContent = profile.discord;
  }

  if (profile.github) {
    const ghLink = document.getElementById('contact-github-link');
    if (ghLink) ghLink.href = safeUrl(profile.github);
  }
};

// 2. TECH ARSENAL & TOOLS RENDER
window.renderArsenalUI = function (filter = 'all') {
  const arsenalGrid = document.getElementById('arsenal-grid-container');
  if (!arsenalGrid) return;

  const arsenal = window.cyberStore.getArsenal();
  const filtered = filter === 'all' ? arsenal : arsenal.filter((item) => item.category === filter);

  arsenalGrid.innerHTML = filtered
    .map(
      (tech) => `
    <div class="tech-card" data-tilt>
      <div class="tech-card-header">
        <div class="tech-icon-box">${esc(tech.icon)}</div>
        <span class="tech-category-tag">${esc(tech.categoryLabel)}</span>
      </div>
      <div>
        <h3 class="tech-name">${esc(tech.name)}</h3>
        <p class="tech-desc">${esc(tech.desc)}</p>
      </div>
      <div>
        <div class="tech-proficiency-bar">
          <div class="tech-proficiency-fill" style="width: ${Math.min(100, Math.max(0, Number(tech.proficiency) || 0))}%;"></div>
        </div>
        <div class="tech-proficiency-meta">
          <span>PROFICIENCY // ${esc(tech.level)}</span>
          <span>${Math.min(100, Math.max(0, Number(tech.proficiency) || 0))}%</span>
        </div>
      </div>
    </div>
  `
    )
    .join('');

  // Re-attach sounds
  document.querySelectorAll('.tech-card').forEach((card) => {
    card.addEventListener('mouseenter', () => window.cyberAudio && window.cyberAudio.playHover());
  });
};

// 3. EKSPLORASI & KEAHLIAN RENDER
window.renderProjectsUI = function () {
  const container = document.getElementById('projects-grid-container');
  if (!container) return;

  const projects = window.cyberStore.getProjects();
  container.innerHTML = projects
    .map(
      (proj) => {
        const cleanId = esc(proj.id);
        const cleanTitle = esc(proj.title);
        const cleanDesc = esc(proj.desc);
        const cleanCat = esc(proj.categoryLabel);
        const cleanCode = esc(proj.code);
        const cleanImg = safeUrl(proj.image);
        const cleanDemo = safeUrl(proj.demoUrl);
        const cleanRepo = safeUrl(proj.repoUrl);
        const tagBadges = (proj.tags || []).map((tag) => `<span class="card-tag">${esc(tag)}</span>`).join('');

        return `
    <div class="exploration-card" data-tilt>
      <div class="card-media-wrapper" onclick="window.openProjectById('${cleanId}')" style="cursor: pointer;">
        <img src="${cleanImg}" alt="${cleanTitle}" loading="lazy" />
        <span class="card-hud-badge">${cleanCat}</span>
        <span class="card-code-badge">${cleanCode}</span>
      </div>
      <div class="card-content">
        <h3 class="card-title">${cleanTitle}</h3>
        <p class="card-desc">${cleanDesc}</p>
        <div class="card-tags">
          ${tagBadges}
        </div>
        <div class="card-footer-actions">
          <button class="cyber-btn cyber-btn-cyan cyber-btn-sm" onclick="window.openProjectById('${cleanId}')">
            DEEP-DIVE HUD
          </button>
          <div class="card-links">
            <a href="${cleanDemo}" target="_blank" rel="noopener noreferrer" class="card-link-btn" title="Live Preview">
              ⚡ DEMO
            </a>
            <a href="${cleanRepo}" target="_blank" rel="noopener noreferrer" class="card-link-btn" title="Source Repo">
              💾 CODE
            </a>
          </div>
        </div>
      </div>
    </div>
  `;
      }
    )
    .join('');
};

window.openProjectById = function (id) {
  const proj = window.cyberStore.getProjects().find((p) => p.id === id);
  if (proj) {
    window.cyberModals.openProjectModal(proj);
  }
};

// 4. PRESTASI & SERTIFIKAT RENDER
window.renderCertificatesUI = function (filter = 'all') {
  const container = document.getElementById('certificates-grid-container');
  if (!container) return;

  const certs = window.cyberStore.getCertificates();
  const filtered = filter === 'all' ? certs : certs.filter((c) => c.category === filter);

  if (filtered.length === 0) {
    container.innerHTML = `
      <div style="grid-column: 1/-1; padding: 40px; text-align: center; font-family: var(--font-mono); color: var(--text-muted); border: 1px dashed var(--border-subtle);">
        [DATA_STREAM_EMPTY] BELUM ADA DOKUMEN PRESTASI DENGAN FILTER INI.
      </div>
    `;
    return;
  }

  container.innerHTML = filtered
    .map(
      (cert) => {
        const cleanId = esc(cert.id);
        const cleanTitle = esc(cert.title);
        const cleanIssuer = esc(cert.issuer);
        const cleanDate = esc(cert.date);
        const cleanCredId = esc(cert.credentialId || 'ID_VERIFIED');
        const cleanImg = safeUrl(cert.image);

        return `
    <div class="cert-card" data-tilt>
      <div class="cert-media-preview" onclick="window.openCertLightbox('${cleanId}')">
        <img src="${cleanImg}" alt="${cleanTitle}" loading="lazy" />
        <span class="cert-verified-stamp">✓ VERIFIED_ICE</span>
      </div>
      <div class="cert-content">
        <div class="cert-issuer">${cleanIssuer}</div>
        <h3 class="cert-title">${cleanTitle}</h3>
        <div class="cert-meta">
          <span>${cleanDate}</span>
          <span>${cleanCredId}</span>
        </div>
      </div>
    </div>
  `;
      }
    )
    .join('');
};

window.openCertLightbox = function (id) {
  const cert = window.cyberStore.getCertificates().find((c) => c.id === id);
  if (cert) {
    window.cyberModals.openLightbox(cert, 'cert');
  }
};

// 5. DOKUMENTASI & BUKTI (GALLERY) RENDER
window.renderDocumentationUI = function () {
  const container = document.getElementById('documentation-grid-container');
  if (!container) return;

  const docs = window.cyberStore.getDocumentation();
  if (docs.length === 0) {
    container.innerHTML = `
      <div style="grid-column: 1/-1; padding: 40px; text-align: center; font-family: var(--font-mono); color: var(--text-muted); border: 1px dashed var(--border-subtle);">
        [GALLERY_EMPTY] BELUM ADA FOTO DOKUMENTASI.
      </div>
    `;
    return;
  }

  container.innerHTML = docs
    .map(
      (doc) => {
        const cleanId = esc(doc.id);
        const cleanTitle = esc(doc.title);
        const cleanTag = esc(doc.tag);
        const cleanDate = esc(doc.date);
        const cleanImg = safeUrl(doc.image);

        return `
    <div class="gallery-item" onclick="window.openDocLightbox('${cleanId}')" data-tilt>
      <img src="${cleanImg}" alt="${cleanTitle}" loading="lazy" />
      <div class="gallery-overlay">
        <span class="gallery-tag">${cleanTag}</span>
        <div class="gallery-caption">${cleanTitle}</div>
        <div class="gallery-date">${cleanDate}</div>
      </div>
    </div>
  `;
      }
    )
    .join('');
};

window.openDocLightbox = function (id) {
  const doc = window.cyberStore.getDocumentation().find((d) => d.id === id);
  if (doc) {
    window.cyberModals.openLightbox(doc, 'gallery');
  }
};

// FILTERS SYSTEM
function initFilters() {
  // Arsenal filter buttons
  document.querySelectorAll('#arsenal-filters .filter-btn').forEach((btn) => {
    btn.addEventListener('click', () => {
      if (window.cyberAudio) window.cyberAudio.playClick();
      document.querySelectorAll('#arsenal-filters .filter-btn').forEach((b) => b.classList.remove('active'));
      btn.classList.add('active');
      const cat = btn.getAttribute('data-filter');
      window.renderArsenalUI(cat);
    });
  });

  // Certificate filter buttons
  document.querySelectorAll('#cert-filters .filter-btn').forEach((btn) => {
    btn.addEventListener('click', () => {
      if (window.cyberAudio) window.cyberAudio.playClick();
      document.querySelectorAll('#cert-filters .filter-btn').forEach((b) => b.classList.remove('active'));
      btn.classList.add('active');
      const cat = btn.getAttribute('data-filter');
      window.renderCertificatesUI(cat);
    });
  });
}

// CONTACT FORM DISPATCH (DISCORD WEBHOOK INTEGRATION)
function initContactForm() {
  const form = document.getElementById('cyber-contact-form');
  if (!form) return;

  const DISCORD_WEBHOOK_URL = 'https://discord.com/api/webhooks/1491025432034938911/OtSYXYA22qqU0C6iAwUorgQ-Qg0SAcmzfdKwmgGMsVxHlOFIBN_6ikQ5Ftf_C3S0pHT-';

  form.addEventListener('submit', async (e) => {
    e.preventDefault();
    const name = document.getElementById('contact-name').value.trim();
    const email = document.getElementById('contact-email').value.trim();
    const subject = document.getElementById('contact-subject').value.trim();
    const message = document.getElementById('contact-message').value.trim();

    if (window.cyberAudio) window.cyberAudio.playScan();

    const submitBtn = form.querySelector('button[type="submit"]');
    const originalText = submitBtn.innerHTML;
    submitBtn.innerHTML = `<span>⚡ TRANSMITTING TO DISCORD...</span>`;
    submitBtn.disabled = true;

    try {
      const payload = {
        username: "NETRUNNER TRANSMISSION DISPATCH",
        avatar_url: "https://images.unsplash.com/photo-1542751371-adc38448a05e?q=80&w=300",
        embeds: [
          {
            title: "⚡ PESAN MASUK BARU // CONTACT ME",
            description: `Sebuah pesan transmisi baru telah dikirimkan melalui formulir portofolio publik!`,
            color: 16576010, // Neon Cyber Yellow (#FCEE0A)
            fields: [
              {
                name: "👤 NAMA PENGIRIM / CALLSIGN",
                value: `**${name}**`,
                inline: true
              },
              {
                name: "✉️ EMAIL PENGIRIM",
                value: `\`${email}\``,
                inline: true
              },
              {
                name: "📡 SUBJEK / TOPIK",
                value: subject || "No Subject",
                inline: false
              },
              {
                name: "📝 ISI PESAN",
                value: `\`\`\`${message}\`\`\``,
                inline: false
              }
            ],
            footer: {
              text: "Night City Node v2.077 // Encrypted Transmission"
            },
            timestamp: new Date().toISOString()
          }
        ]
      };

      const response = await fetch(DISCORD_WEBHOOK_URL, {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify(payload)
      });

      if (response.ok || response.status === 204) {
        if (window.cyberAudio) window.cyberAudio.playSuccess();
        window.showCyberToast(`TRANSMISI TERKIRIM DARI [${name.toUpperCase()}] KE DISCORD // SUKSES!`, "cyan");
        form.reset();
      } else {
        throw new Error(`Discord Webhook error (status: ${response.status})`);
      }
    } catch (err) {
      console.error("Webhook dispatch error:", err);
      if (window.cyberAudio) window.cyberAudio.playGlitch();
      window.showCyberToast("GAGAL MENGIRIM KE DISCORD: " + err.message, "pink");
    } finally {
      submitBtn.innerHTML = originalText;
      submitBtn.disabled = false;
    }
  });
}

// TELEMETRY LIVE CLOCK
function initTelemetryClock() {
  const clockEl = document.getElementById('telemetry-clock');
  const fpsEl = document.getElementById('telemetry-fps');
  if (!clockEl) return;

  setInterval(() => {
    const now = new Date();
    const timeStr = now.toTimeString().split(' ')[0] + '.' + String(now.getMilliseconds()).padStart(3, '0').slice(0, 2);
    clockEl.textContent = `NIGHT_CITY_TIME: ${timeStr} GMT+7`;
  }, 100);

  // Simulated FPS Counter
  if (fpsEl) {
    let lastTime = performance.now();
    let frame = 0;
    function updateFps() {
      frame++;
      const now = performance.now();
      if (now >= lastTime + 1000) {
        fpsEl.textContent = `SYS.FPS: ${frame} // LATENCY: 12ms`;
        frame = 0;
        lastTime = now;
      }
      requestAnimationFrame(updateFps);
    }
    requestAnimationFrame(updateFps);
  }
}

// AUDIO CONTROLS
function initAudioControls() {
  const audioBtn = document.getElementById('audio-toggle-btn');
  if (!audioBtn) return;

  audioBtn.addEventListener('click', () => {
    const isMuted = window.cyberAudio.toggleMute();
    if (isMuted) {
      audioBtn.innerHTML = `🔇 <span>MUTED</span>`;
      audioBtn.classList.remove('active');
      window.showCyberToast("AUDIO SYNTHESIZER: MUTED", "pink");
    } else {
      audioBtn.innerHTML = `🔊 <span>AUDIO: ON</span>`;
      audioBtn.classList.add('active');
      if (window.cyberAudio) window.cyberAudio.playSuccess();
      window.showCyberToast("AUDIO SYNTHESIZER: ONLINE & ACTIVE", "cyan");
    }
  });

  // Sound triggers on interactive links & buttons
  document.querySelectorAll('a, button, input, textarea, select').forEach((el) => {
    el.addEventListener('mouseenter', () => window.cyberAudio && window.cyberAudio.playHover());
    el.addEventListener('focus', () => window.cyberAudio && window.cyberAudio.playHover());
  });
}

// 3D CARD TILT ON MOUSEMOVE
function initCardTilts() {
  document.addEventListener('mousemove', (e) => {
    document.querySelectorAll('[data-tilt]').forEach((card) => {
      const rect = card.getBoundingClientRect();
      const x = e.clientX - rect.left;
      const y = e.clientY - rect.top;

      if (x >= 0 && x <= rect.width && y >= 0 && y <= rect.height) {
        const centerX = rect.width / 2;
        const centerY = rect.height / 2;
        const rotateX = ((y - centerY) / centerY) * -6;
        const rotateY = ((x - centerX) / centerX) * 6;

        card.style.transform = `perspective(1000px) rotateX(${rotateX}deg) rotateY(${rotateY}deg) translateY(-4px)`;
      } else {
        card.style.transform = '';
      }
    });
  });
}

// GENERAL UI & NAVBAR SCROLL
function initUI() {
  const navbar = document.querySelector('.cyber-navbar');
  const mobileBtn = document.getElementById('mobile-menu-toggle');
  const navLinks = document.querySelector('.nav-links');

  window.addEventListener('scroll', () => {
    if (window.scrollY > 40) {
      navbar.classList.add('scrolled');
    } else {
      navbar.classList.remove('scrolled');
    }

    // Scrollspy active class
    const sections = document.querySelectorAll('section');
    const scrollPos = window.scrollY + 200;

    sections.forEach((sec) => {
      if (scrollPos >= sec.offsetTop && scrollPos < sec.offsetTop + sec.offsetHeight) {
        const id = sec.getAttribute('id');
        document.querySelectorAll('.nav-item a').forEach((a) => {
          a.classList.remove('active');
          if (a.getAttribute('href') === `#${id}`) {
            a.classList.add('active');
          }
        });
      }
    });
  });

  if (mobileBtn && navLinks) {
    mobileBtn.addEventListener('click', () => {
      if (window.cyberAudio) window.cyberAudio.playClick();
      navLinks.classList.toggle('mobile-open');
    });

    document.querySelectorAll('.nav-links a').forEach((link) => {
      link.addEventListener('click', () => {
        navLinks.classList.remove('mobile-open');
      });
    });
  }
}

// INTERACTIVE CYBER TERMINAL
function initTerminal() {
  const termBtn = document.getElementById('open-terminal-btn');
  const termInput = document.getElementById('terminal-command-input');
  const termOutput = document.getElementById('terminal-output-body');

  if (termBtn) {
    termBtn.addEventListener('click', () => {
      window.cyberModals.openModal('modal-cyber-terminal');
      if (termInput) termInput.focus();
    });
  }

  // Press '~' or '`' to toggle terminal
  window.addEventListener('keydown', (e) => {
    if (e.key === '`' || e.key === '~') {
      e.preventDefault();
      const termModal = document.getElementById('modal-cyber-terminal');
      if (termModal.classList.contains('active')) {
        window.cyberModals.closeModal('modal-cyber-terminal');
      } else {
        window.cyberModals.openModal('modal-cyber-terminal');
        if (termInput) termInput.focus();
      }
    }
  });

  if (termInput && termOutput) {
    termInput.addEventListener('keydown', (e) => {
      if (e.key === 'Enter') {
        const cmd = termInput.value.trim().toLowerCase();
        termInput.value = '';
        executeTerminalCommand(cmd, termOutput);
      }
    });
  }
}

function executeTerminalCommand(cmd, outputEl) {
  if (window.cyberAudio) window.cyberAudio.playScan();
  const line = document.createElement('div');
  line.style.marginBottom = '6px';
  line.innerHTML = `<span style="color: var(--cp-yellow);">> ${cmd}</span>`;
  outputEl.appendChild(line);

  const resLine = document.createElement('div');
  resLine.style.marginBottom = '12px';
  resLine.style.color = '#FFF';

  switch (cmd) {
    case 'help':
      resLine.innerHTML = `
        <span style="color: var(--cp-cyan);">AVAILABLE COMMANDS:</span><br/>
        - <b style="color: var(--cp-yellow);">skills</b>: Menampilkan daftar teknologi & level mastery<br/>
        - <b style="color: var(--cp-yellow);">projects</b>: Membuka log misi & eksplorasi<br/>
        - <b style="color: var(--cp-yellow);">certs</b>: Melihat data sertifikat terverifikasi<br/>
        - <b style="color: var(--cp-yellow);">contact</b>: Informasi saluran transmisi kontak<br/>
        - <b style="color: var(--cp-yellow);">bio</b>: Menampilkan profil bio Netrunner<br/>
        - <b style="color: var(--cp-yellow);">clear</b>: Membersihkan riwayat terminal<br/>
        - <b style="color: var(--cp-yellow);">sound</b>: Toggle audio synthesizer ON/OFF
      `;
      break;
    case 'skills':
      const skills = window.cyberStore.getArsenal().map((s) => `${s.name} (${s.proficiency}%)`).join(', ');
      resLine.innerHTML = `<span style="color: var(--cp-cyan);">TECH ARSENAL:</span> ${skills}`;
      break;
    case 'projects':
      const projs = window.cyberStore.getProjects().map((p) => `[${p.code}] ${p.title}`).join('<br/>');
      resLine.innerHTML = `<span style="color: var(--cp-cyan);">MISSION LOGS:</span><br/>${projs}`;
      break;
    case 'certs':
      const certs = window.cyberStore.getCertificates().map((c) => `✓ ${c.title} (${c.issuer})`).join('<br/>');
      resLine.innerHTML = `<span style="color: var(--cp-green);">VERIFIED CERTIFICATES:</span><br/>${certs}`;
      break;
    case 'bio':
      const p = window.cyberStore.getProfile();
      resLine.innerHTML = `<span style="color: var(--cp-yellow);">${p.name}</span> // ${p.title}<br/>${p.bio}`;
      break;
    case 'contact':
      const pr = window.cyberStore.getProfile();
      resLine.innerHTML = `Email: ${pr.email} // WA: ${pr.whatsapp} // Discord: ${pr.discord}`;
      break;
    case 'sound':
      const muted = window.cyberAudio.toggleMute();
      resLine.innerHTML = `Sound Synthesizer status: ${muted ? 'MUTED' : 'ONLINE'}`;
      break;
    case 'clear':
      outputEl.innerHTML = '';
      return;
    default:
      resLine.innerHTML = `<span style="color: var(--cp-pink);">COMMAND NOT RECOGNIZED: '${cmd}'. Ketik 'help' untuk daftar perintah.</span>`;
  }

  outputEl.appendChild(resLine);
  outputEl.scrollTop = outputEl.scrollHeight;
}
