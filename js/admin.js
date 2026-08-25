/**
 * CYBERPUNK 2077 - ADMIN COMMAND DECK CONTROLLER (SECURE & BUG-FREE v2.077)
 * Night City Classified Admin Interface Protocol
 */

document.addEventListener('DOMContentLoaded', () => {
  initSecurityAuth();
  initAdminNavigation();
  initDropzones();
  initForms();
  initPasswordVisibilityToggle();
});

// Safe DOM Value Helpers (Zero Null Pointer Errors)
function getVal(id) {
  const el = document.getElementById(id);
  return el ? el.value.trim() : '';
}

function setVal(id, val) {
  const el = document.getElementById(id);
  if (el) el.value = val || '';
}

// Toast Notification System for Admin
function showAdminToast(message, type = 'yellow') {
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
}

// 1. SECURITY & AUTHENTICATION
let failedAttempts = 0;

function initSecurityAuth() {
  const loginView = document.getElementById('ice-login-screen');
  const dashboardView = document.getElementById('admin-dashboard-app');
  const loginForm = document.getElementById('ice-login-form');
  const pinInput = document.getElementById('ice-pin-input');

  // Check if already authenticated
  if (window.cyberStore && window.cyberStore.isAdminAuthenticated()) {
    if (loginView) loginView.style.display = 'none';
    if (dashboardView) dashboardView.style.display = 'flex';
    renderDashboardOverview();
  } else {
    if (loginView) loginView.style.display = 'flex';
    if (dashboardView) dashboardView.style.display = 'none';
  }

  // Handle Login Form Submit
  if (loginForm) {
    loginForm.addEventListener('submit', (e) => {
      e.preventDefault();
      const pinVal = pinInput ? pinInput.value : '';

      if (!pinVal || pinVal.trim() === '') {
        showAdminToast('MASUKKAN MASTER PASSPHRASE TERLEBIH DAHULU!', 'pink');
        return;
      }

      if (failedAttempts >= 5) {
        if (window.cyberAudio) window.cyberAudio.playGlitch();
        showAdminToast('ICE LOCKDOWN ACTIVE: Tunggu beberapa saat sebelum mencoba lagi.', 'pink');
        return;
      }

      const success = window.cyberStore.loginAdmin(pinVal);

      if (success) {
        if (window.cyberAudio) window.cyberAudio.playSuccess();
        failedAttempts = 0;
        showAdminToast('ICE BREACH SUCCESSFUL // ACCESS GRANTED', 'yellow');
        if (loginView) loginView.style.display = 'none';
        if (dashboardView) dashboardView.style.display = 'flex';
        renderDashboardOverview();
      } else {
        failedAttempts++;
        if (window.cyberAudio) window.cyberAudio.playGlitch();
        showAdminToast(`PASSPHRASE SALAH! Percobaan gagal: ${failedAttempts}/5`, 'pink');

        if (failedAttempts >= 5) {
          showAdminToast('SISTEM TERKUNCI SELAMA 15 DETIK DEMI KEAMANAN!', 'pink');
          const submitBtn = loginForm.querySelector('button[type="submit"]');
          if (submitBtn) submitBtn.disabled = true;

          setTimeout(() => {
            failedAttempts = 0;
            if (submitBtn) submitBtn.disabled = false;
            showAdminToast('LOCKDOWN BERAKHIR. Anda dapat mencoba kembali.', 'cyan');
          }, 15000);
        }
      }
    });
  }

  // Logout Button
  const logoutBtn = document.getElementById('admin-logout-btn');
  if (logoutBtn) {
    logoutBtn.addEventListener('click', () => {
      window.cyberStore.logoutAdmin();
      if (window.cyberAudio) window.cyberAudio.playClick();
      if (loginView) loginView.style.display = 'flex';
      if (dashboardView) dashboardView.style.display = 'none';
      if (pinInput) pinInput.value = '';
      showAdminToast('TERMINAL TERKUNCI // ADMIN DISCONNECTED', 'pink');
    });
  }
}

// Password Visibility Toggle
function initPasswordVisibilityToggle() {
  const toggleBtn = document.getElementById('toggle-pin-visibility');
  const pinInput = document.getElementById('ice-pin-input');
  if (toggleBtn && pinInput) {
    toggleBtn.addEventListener('click', () => {
      if (window.cyberAudio) window.cyberAudio.playHover();
      if (pinInput.type === 'password') {
        pinInput.type = 'text';
        toggleBtn.textContent = '🙈 SEMBUNYIKAN';
      } else {
        pinInput.type = 'password';
        toggleBtn.textContent = '👁️ LIHAT';
      }
    });
  }
}

// 2. ADMIN NAVIGATION
function initAdminNavigation() {
  document.querySelectorAll('.admin-nav-item button').forEach((btn) => {
    btn.addEventListener('click', () => {
      if (window.cyberAudio) window.cyberAudio.playHover();
      document.querySelectorAll('.admin-nav-item button').forEach((b) => b.classList.remove('active'));
      btn.classList.add('active');

      const targetTab = btn.getAttribute('data-tab');
      document.querySelectorAll('.admin-tab-pane').forEach((pane) => pane.classList.remove('active'));

      const activePane = document.getElementById(targetTab);
      if (activePane) {
        activePane.classList.add('active');
      }

      if (targetTab === 'tab-overview') renderDashboardOverview();
      if (targetTab === 'tab-profile') renderProfileTab();
      if (targetTab === 'tab-projects') renderProjectsTab();
      if (targetTab === 'tab-arsenal') renderArsenalTab();
      if (targetTab === 'tab-certificates') renderCertificatesTab();
      if (targetTab === 'tab-documentation') renderDocumentationTab();
    });
  });
}

// 3. DROPZONES (ALL IMAGE FORMAT SUPPORT)
let tempAdminProfileImg = null;
let tempAdminProjectImg = null;
let tempAdminEditProjectImg = null;
let tempAdminCertImg = null;
let tempAdminDocImg = null;

function initDropzones() {
  setupAdminDropzone('admin-profile-dropzone', 'admin-profile-file-input', (url) => {
    tempAdminProfileImg = url;
    const imgEl = document.getElementById('admin-profile-preview-img');
    const container = document.getElementById('admin-profile-preview-container');
    if (imgEl) imgEl.src = url;
    if (container) container.style.display = 'flex';
  });

  setupAdminDropzone('admin-project-dropzone', 'admin-project-file-input', (url) => {
    tempAdminProjectImg = url;
    const imgEl = document.getElementById('admin-project-preview-img');
    const container = document.getElementById('admin-project-preview-container');
    if (imgEl) imgEl.src = url;
    if (container) container.style.display = 'flex';
  });

  setupAdminDropzone('admin-edit-project-dropzone', 'admin-edit-project-file-input', (url) => {
    tempAdminEditProjectImg = url;
    const imgEl = document.getElementById('admin-edit-project-preview-img');
    const container = document.getElementById('admin-edit-project-preview-container');
    if (imgEl) imgEl.src = url;
    if (container) container.style.display = 'flex';
  });

  setupAdminDropzone('admin-cert-dropzone', 'admin-cert-file-input', (url) => {
    tempAdminCertImg = url;
    const imgEl = document.getElementById('admin-cert-preview-img');
    const container = document.getElementById('admin-cert-preview-container');
    if (imgEl) imgEl.src = url;
    if (container) container.style.display = 'flex';
  });

  setupAdminDropzone('admin-doc-dropzone', 'admin-doc-file-input', (url) => {
    tempAdminDocImg = url;
    const imgEl = document.getElementById('admin-doc-preview-img');
    const container = document.getElementById('admin-doc-preview-container');
    if (imgEl) imgEl.src = url;
    if (container) container.style.display = 'flex';
  });
}

function setupAdminDropzone(dropzoneId, inputId, onLoaded) {
  const dropzone = document.getElementById(dropzoneId);
  const input = document.getElementById(inputId);
  if (!dropzone || !input) return;

  dropzone.addEventListener('click', () => {
    if (window.cyberAudio) window.cyberAudio.playClick();
    input.click();
  });

  input.addEventListener('change', async (e) => {
    const file = e.target.files[0];
    if (file) {
      try {
        const dataUrl = await window.cyberStore.readImageFile(file);
        if (window.cyberAudio) window.cyberAudio.playScan();
        onLoaded(dataUrl);
        showAdminToast('BERKAS GAMBAR DIMUAT (SEMUA FORMAT DIDUKUNG)', 'cyan');
      } catch (err) {
        if (window.cyberAudio) window.cyberAudio.playGlitch();
        showAdminToast(err.message, 'pink');
      }
    }
  });

  ['dragenter', 'dragover'].forEach((eventName) => {
    dropzone.addEventListener(eventName, (e) => {
      e.preventDefault();
      dropzone.classList.add('dragover');
    });
  });

  ['dragleave', 'drop'].forEach((eventName) => {
    dropzone.addEventListener(eventName, (e) => {
      e.preventDefault();
      dropzone.classList.remove('dragover');
    });
  });

  dropzone.addEventListener('drop', async (e) => {
    const file = e.dataTransfer.files[0];
    if (file) {
      try {
        const dataUrl = await window.cyberStore.readImageFile(file);
        if (window.cyberAudio) window.cyberAudio.playScan();
        onLoaded(dataUrl);
        showAdminToast('GAMBAR BERHASIL DIUNGGAH (DRAG & DROP)', 'cyan');
      } catch (err) {
        if (window.cyberAudio) window.cyberAudio.playGlitch();
        showAdminToast(err.message, 'pink');
      }
    }
  });
}

// 4. OVERVIEW TAB
function renderDashboardOverview() {
  const profile = window.cyberStore.getProfile();
  const projects = window.cyberStore.getProjects();
  const arsenal = window.cyberStore.getArsenal();
  const certs = window.cyberStore.getCertificates();
  const docs = window.cyberStore.getDocumentation();

  const elProjects = document.getElementById('overview-total-projects');
  const elSkills = document.getElementById('overview-total-skills');
  const elCerts = document.getElementById('overview-total-certs');
  const elDocs = document.getElementById('overview-total-docs');
  const elName = document.getElementById('overview-profile-name');
  const elTitle = document.getElementById('overview-profile-title');

  if (elProjects) elProjects.textContent = projects.length;
  if (elSkills) elSkills.textContent = arsenal.length;
  if (elCerts) elCerts.textContent = certs.length;
  if (elDocs) elDocs.textContent = docs.length;
  if (elName) elName.textContent = profile.name || '-';
  if (elTitle) elTitle.textContent = profile.title || '-';
}

// 5. PROFILE TAB
function renderProfileTab() {
  const profile = window.cyberStore.getProfile();

  setVal('admin-prof-name', profile.name);
  setVal('admin-prof-title', profile.title);
  setVal('admin-prof-bio', profile.bio);
  setVal('admin-prof-location', profile.location);
  setVal('admin-prof-email', profile.email);
  setVal('admin-prof-steam', profile.steam);
  setVal('admin-prof-instagram', profile.instagram);
  setVal('admin-prof-facebook', profile.facebook);
  setVal('admin-prof-discord', profile.discord);
  setVal('admin-prof-github', profile.github);
  setVal('admin-prof-telegram', profile.telegram);

  tempAdminProfileImg = profile.avatar;
  const previewImg = document.getElementById('admin-profile-preview-img');
  const previewContainer = document.getElementById('admin-profile-preview-container');
  if (previewImg && profile.avatar) {
    previewImg.src = profile.avatar;
    if (previewContainer) previewContainer.style.display = 'flex';
  }
}

// 6. EKSPLORASI & KEAHLIAN (PROJECTS) TAB
function renderProjectsTab() {
  const container = document.getElementById('admin-projects-list');
  if (!container) return;

  const projects = window.cyberStore.getProjects();
  if (projects.length === 0) {
    container.innerHTML = `<div style="grid-column: 1/-1; padding: 30px; text-align: center; color: var(--text-muted); font-family: var(--font-mono);">[EMPTY] Belum ada proyek eksplorasi. Tambahkan melalui formulir di atas.</div>`;
    return;
  }

  container.innerHTML = projects
    .map(
      (p) => `
    <div class="admin-item-card">
      <div class="admin-item-media">
        <img src="${p.image}" alt="${p.title}" />
        <span class="card-hud-badge" style="position: absolute; top: 8px; left: 8px;">${p.code}</span>
      </div>
      <div class="admin-item-body">
        <h4 class="admin-item-title">${p.title}</h4>
        <p class="admin-item-desc">${p.desc}</p>
        <div class="card-tags" style="margin-bottom: 12px;">
          ${p.tags.map((t) => `<span class="card-tag">${t}</span>`).join('')}
        </div>
        <div class="admin-item-actions">
          <button class="cyber-btn cyber-btn-cyan cyber-btn-sm" style="flex: 1;" onclick="openEditProjectModal('${p.id}')">
            ✏️ EDIT MISI
          </button>
          <button class="cyber-btn cyber-btn-pink cyber-btn-sm" onclick="deleteProjectItem('${p.id}')">
            🗑️ HAPUS
          </button>
        </div>
      </div>
    </div>
  `
    )
    .join('');
}

window.deleteProjectItem = function (id) {
  if (confirm('Hapus misi eksplorasi ini secara permanen dari memory?')) {
    window.cyberStore.deleteProject(id);
    if (window.cyberAudio) window.cyberAudio.playGlitch();
    showAdminToast('PROYEK EKSPLORASI BERHASIL DIHAPUS', 'pink');
    renderProjectsTab();
  }
};

window.openEditProjectModal = function (id) {
  const p = window.cyberStore.getProjects().find((proj) => proj.id === id);
  if (!p) return;

  setVal('edit-proj-id', p.id);
  setVal('edit-proj-title', p.title);
  setVal('edit-proj-code', p.code);
  setVal('edit-proj-category', p.category);
  setVal('edit-proj-tags', p.tags ? p.tags.join(', ') : '');
  setVal('edit-proj-desc', p.desc);
  setVal('edit-proj-specs', p.specs);
  setVal('edit-proj-demo', p.demoUrl);
  setVal('edit-proj-repo', p.repoUrl);

  tempAdminEditProjectImg = p.image;
  const previewImg = document.getElementById('admin-edit-project-preview-img');
  const previewContainer = document.getElementById('admin-edit-project-preview-container');
  if (previewImg && p.image) {
    previewImg.src = p.image;
    if (previewContainer) previewContainer.style.display = 'flex';
  }

  const modal = document.getElementById('modal-edit-project-admin');
  if (modal) modal.classList.add('active');
};

// 7. TECH ARSENAL TAB
function renderArsenalTab() {
  const container = document.getElementById('admin-arsenal-list');
  if (!container) return;

  const skills = window.cyberStore.getArsenal();
  container.innerHTML = skills
    .map(
      (s) => `
    <div class="tech-card">
      <div class="tech-card-header">
        <div class="tech-icon-box">${s.icon}</div>
        <span class="tech-category-tag">${s.categoryLabel}</span>
      </div>
      <div>
        <h4 class="tech-name">${s.name}</h4>
        <p class="tech-desc">${s.desc}</p>
        <div class="tech-proficiency-meta">
          <span>${s.level}</span>
          <span>${s.proficiency}%</span>
        </div>
      </div>
      <div style="margin-top: 15px; display: flex; gap: 8px;">
        <button class="cyber-btn cyber-btn-pink cyber-btn-sm" style="width: 100%;" onclick="deleteSkillItem('${s.id}')">
          🗑️ HAPUS SKILL
        </button>
      </div>
    </div>
  `
    )
    .join('');
}

window.deleteSkillItem = function (id) {
  if (confirm('Hapus teknologi ini dari Tech Arsenal?')) {
    window.cyberStore.deleteArsenal(id);
    if (window.cyberAudio) window.cyberAudio.playGlitch();
    showAdminToast('SKILL BERHASIL DIHAPUS DARI ARSENAL', 'pink');
    renderArsenalTab();
  }
};

// 8. PRESTASI & SERTIFIKAT TAB
function renderCertificatesTab() {
  const container = document.getElementById('admin-certs-list');
  if (!container) return;

  const certs = window.cyberStore.getCertificates();
  container.innerHTML = certs
    .map(
      (c) => `
    <div class="admin-item-card">
      <div class="admin-item-media">
        <img src="${c.image}" alt="${c.title}" />
        <span class="cert-verified-stamp">✓ VERIFIED</span>
      </div>
      <div class="admin-item-body">
        <div style="font-family: var(--font-mono); font-size: 0.72rem; color: var(--cp-cyan);">${c.issuer}</div>
        <h4 class="admin-item-title">${c.title}</h4>
        <div style="font-family: var(--font-mono); font-size: 0.75rem; color: var(--text-muted); margin-bottom: 12px;">
          ${c.date} // ID: ${c.credentialId}
        </div>
        <div class="admin-item-actions">
          <button class="cyber-btn cyber-btn-pink cyber-btn-sm" style="width: 100%;" onclick="deleteCertItem('${c.id}')">
            🗑️ HAPUS SERTIFIKAT
          </button>
        </div>
      </div>
    </div>
  `
    )
    .join('');
}

window.deleteCertItem = function (id) {
  if (confirm('Hapus sertifikat ini dari data portofolio?')) {
    window.cyberStore.deleteCertificate(id);
    if (window.cyberAudio) window.cyberAudio.playGlitch();
    showAdminToast('SERTIFIKAT BERHASIL DIHAPUS', 'pink');
    renderCertificatesTab();
  }
};

// 9. DOKUMENTASI & BUKTI TAB
function renderDocumentationTab() {
  const container = document.getElementById('admin-docs-list');
  if (!container) return;

  const docs = window.cyberStore.getDocumentation();
  container.innerHTML = docs
    .map(
      (d) => `
    <div class="admin-item-card">
      <div class="admin-item-media">
        <img src="${d.image}" alt="${d.title}" />
        <span class="card-hud-badge" style="position: absolute; top: 8px; left: 8px;">${d.tag}</span>
      </div>
      <div class="admin-item-body">
        <h4 class="admin-item-title">${d.title}</h4>
        <p class="admin-item-desc">${d.caption}</p>
        <div style="font-family: var(--font-mono); font-size: 0.72rem; color: var(--cp-cyan); margin-bottom: 12px;">${d.date}</div>
        <div class="admin-item-actions">
          <button class="cyber-btn cyber-btn-pink cyber-btn-sm" style="width: 100%;" onclick="deleteDocItem('${d.id}')">
            🗑️ HAPUS FOTO
          </button>
        </div>
      </div>
    </div>
  `
    )
    .join('');
}

window.deleteDocItem = function (id) {
  if (confirm('Hapus dokumentasi foto ini dari galeri bukti?')) {
    window.cyberStore.deleteDocumentation(id);
    if (window.cyberAudio) window.cyberAudio.playGlitch();
    showAdminToast('FOTO DOKUMENTASI BERHASIL DIHAPUS', 'pink');
    renderDocumentationTab();
  }
};

// 10. FORMS DISPATCH
function initForms() {
  // A. Save Profile (Guarded & Safe)
  const formProfile = document.getElementById('admin-form-profile');
  if (formProfile) {
    formProfile.addEventListener('submit', (e) => {
      e.preventDefault();
      try {
        const profile = window.cyberStore.getProfile();
        profile.name = getVal('admin-prof-name') || profile.name;
        profile.title = getVal('admin-prof-title') || profile.title;
        profile.bio = getVal('admin-prof-bio') || profile.bio;
        profile.location = getVal('admin-prof-location') || profile.location;
        profile.email = getVal('admin-prof-email') || profile.email;
        profile.steam = getVal('admin-prof-steam') || profile.steam;
        profile.instagram = getVal('admin-prof-instagram') || profile.instagram;
        profile.facebook = getVal('admin-prof-facebook') || profile.facebook;
        profile.discord = getVal('admin-prof-discord') || profile.discord;
        profile.github = getVal('admin-prof-github') || profile.github;
        profile.telegram = getVal('admin-prof-telegram') || profile.telegram;

        if (tempAdminProfileImg) {
          profile.avatar = tempAdminProfileImg;
        }

        window.cyberStore.saveProfile(profile);
        if (window.cyberAudio) window.cyberAudio.playSuccess();
        showAdminToast('PROFIL & FOTO MUKA BERHASIL DISIMPAN!', 'yellow');
        renderDashboardOverview();
      } catch (err) {
        if (window.cyberAudio) window.cyberAudio.playGlitch();
        showAdminToast('GAGAL MENYIMPAN PROFIL: ' + err.message, 'pink');
      }
    });
  }

  // B. Add New Project (Eksplorasi)
  const formAddProject = document.getElementById('admin-form-add-project');
  if (formAddProject) {
    formAddProject.addEventListener('submit', (e) => {
      e.preventDefault();
      try {
        const title = getVal('add-proj-title');
        const code = getVal('add-proj-code') || 'OP_CUSTOM_MISSION';
        const category = getVal('add-proj-category') || 'web';
        const tagsStr = getVal('add-proj-tags');
        const desc = getVal('add-proj-desc');
        const specs = getVal('add-proj-specs') || 'Latency: <10ms // Verified';
        const demoUrl = getVal('add-proj-demo') || '#';
        const repoUrl = getVal('add-proj-repo') || '#';

        if (!tempAdminProjectImg) {
          if (window.cyberAudio) window.cyberAudio.playGlitch();
          showAdminToast('UNGGAH GAMBAR PROYEK EKSPLORASI TERLEBIH DAHULU!', 'pink');
          return;
        }

        const categoryLabels = {
          web: 'CYBER PLATFORM',
          ai: 'AI & NETRUNNING',
          security: 'CYBER SECURITY'
        };

        const newProject = {
          id: 'proj-' + Date.now(),
          title,
          code,
          category,
          categoryLabel: categoryLabels[category] || 'MISSION LOG',
          desc,
          tags: tagsStr ? tagsStr.split(',').map((t) => t.trim()).filter(Boolean) : ['Cyberpunk', 'Fullstack'],
          image: tempAdminProjectImg,
          demoUrl,
          repoUrl,
          specs
        };

        window.cyberStore.addProject(newProject);
        if (window.cyberAudio) window.cyberAudio.playSuccess();
        showAdminToast('MISI EKSPLORASI BARU BERHASIL DITAMBAHKAN!', 'cyan');

        formAddProject.reset();
        tempAdminProjectImg = null;
        const container = document.getElementById('admin-project-preview-container');
        if (container) container.style.display = 'none';
        renderProjectsTab();
      } catch (err) {
        if (window.cyberAudio) window.cyberAudio.playGlitch();
        showAdminToast('GAGAL MENAMBAH PROYEK: ' + err.message, 'pink');
      }
    });
  }

  // C. Save Edited Project Modal
  const formEditProject = document.getElementById('admin-form-edit-project');
  if (formEditProject) {
    formEditProject.addEventListener('submit', (e) => {
      e.preventDefault();
      try {
        const id = getVal('edit-proj-id');
        const title = getVal('edit-proj-title');
        const code = getVal('edit-proj-code');
        const category = getVal('edit-proj-category');
        const tagsStr = getVal('edit-proj-tags');
        const desc = getVal('edit-proj-desc');
        const specs = getVal('edit-proj-specs');
        const demoUrl = getVal('edit-proj-demo');
        const repoUrl = getVal('edit-proj-repo');

        const categoryLabels = {
          web: 'CYBER PLATFORM',
          ai: 'AI & NETRUNNING',
          security: 'CYBER SECURITY'
        };

        const updated = {
          title,
          code,
          category,
          categoryLabel: categoryLabels[category] || 'MISSION LOG',
          desc,
          tags: tagsStr ? tagsStr.split(',').map((t) => t.trim()).filter(Boolean) : ['Cyberpunk', 'Fullstack'],
          specs,
          demoUrl,
          repoUrl
        };

        if (tempAdminEditProjectImg) {
          updated.image = tempAdminEditProjectImg;
        }

        window.cyberStore.updateProject(id, updated);
        if (window.cyberAudio) window.cyberAudio.playSuccess();
        showAdminToast('PERUBAHAN MISI EKSPLORASI BERHASIL DISIMPAN!', 'yellow');

        const modal = document.getElementById('modal-edit-project-admin');
        if (modal) modal.classList.remove('active');
        renderProjectsTab();
      } catch (err) {
        if (window.cyberAudio) window.cyberAudio.playGlitch();
        showAdminToast('GAGAL MEMPERBARUI PROYEK: ' + err.message, 'pink');
      }
    });
  }

  // D. Add Arsenal / Skill
  const formAddSkill = document.getElementById('admin-form-add-skill');
  if (formAddSkill) {
    formAddSkill.addEventListener('submit', (e) => {
      e.preventDefault();
      try {
        const name = getVal('add-skill-name');
        const icon = getVal('add-skill-icon') || '⚡';
        const category = getVal('add-skill-category');
        const proficiency = parseInt(getVal('add-skill-proficiency'), 10) || 85;
        const level = getVal('add-skill-level') || 'EXPERT';
        const desc = getVal('add-skill-desc');

        const categoryLabels = {
          frontend: 'FRONT-END CYBERWARE',
          backend: 'BACK-END ENGINE',
          devops: 'CONTAINER PROTOCOL',
          ai: 'SYNTHETIC INTELLIGENCE',
          security: 'ICE BREAKER & DEFENSE'
        };

        const newSkill = {
          id: 'tech-' + Date.now(),
          name,
          icon,
          category,
          categoryLabel: categoryLabels[category] || 'TECH ARSENAL',
          proficiency,
          level,
          desc
        };

        window.cyberStore.addArsenal(newSkill);
        if (window.cyberAudio) window.cyberAudio.playSuccess();
        showAdminToast('SKILL BARU BERHASIL DITAMBAHKAN KE TECH ARSENAL!', 'cyan');

        formAddSkill.reset();
        renderArsenalTab();
      } catch (err) {
        if (window.cyberAudio) window.cyberAudio.playGlitch();
        showAdminToast(err.message, 'pink');
      }
    });
  }

  // E. Add Certificate
  const formAddCert = document.getElementById('admin-form-add-cert');
  if (formAddCert) {
    formAddCert.addEventListener('submit', (e) => {
      e.preventDefault();
      try {
        const title = getVal('admin-cert-title');
        const issuer = getVal('admin-cert-issuer');
        const date = getVal('admin-cert-date') || '2025 - VERIFIED';
        const credentialId = getVal('admin-cert-id') || 'CERT-ID-' + Math.floor(Math.random() * 90000);
        const category = getVal('admin-cert-category');

        if (!tempAdminCertImg) {
          if (window.cyberAudio) window.cyberAudio.playGlitch();
          showAdminToast('UNGGAH GAMBAR SERTIFIKAT TERLEBIH DAHULU!', 'pink');
          return;
        }

        const newCert = {
          id: 'cert-' + Date.now(),
          title,
          issuer,
          date,
          credentialId,
          category,
          image: tempAdminCertImg,
          tags: ['Verified Credential', 'Cyber Portfolio']
        };

        window.cyberStore.addCertificate(newCert);
        if (window.cyberAudio) window.cyberAudio.playSuccess();
        showAdminToast('PRESTASI & SERTIFIKAT BERHASIL DIUNGGAH!', 'yellow');

        formAddCert.reset();
        tempAdminCertImg = null;
        const container = document.getElementById('admin-cert-preview-container');
        if (container) container.style.display = 'none';
        renderCertificatesTab();
      } catch (err) {
        if (window.cyberAudio) window.cyberAudio.playGlitch();
        showAdminToast(err.message, 'pink');
      }
    });
  }

  // F. Add Documentation Photo
  const formAddDoc = document.getElementById('admin-form-add-doc');
  if (formAddDoc) {
    formAddDoc.addEventListener('submit', (e) => {
      e.preventDefault();
      try {
        const title = getVal('admin-doc-title');
        const tag = getVal('admin-doc-tag') || 'PHOTO EVIDENCE';
        const date = getVal('admin-doc-date') || '2025 // Night City';
        const caption = getVal('admin-doc-caption');

        if (!tempAdminDocImg) {
          if (window.cyberAudio) window.cyberAudio.playGlitch();
          showAdminToast('UNGGAH FOTO DOKUMENTASI TERLEBIH DAHULU!', 'pink');
          return;
        }

        const newDoc = {
          id: 'doc-' + Date.now(),
          title,
          tag: tag.toUpperCase(),
          date,
          caption,
          image: tempAdminDocImg
        };

        window.cyberStore.addDocumentation(newDoc);
        if (window.cyberAudio) window.cyberAudio.playSuccess();
        showAdminToast('DOKUMENTASI BERHASIL DITAMBAHKAN KE MATRIX!', 'cyan');

        formAddDoc.reset();
        tempAdminDocImg = null;
        const container = document.getElementById('admin-doc-preview-container');
        if (container) container.style.display = 'none';
        renderDocumentationTab();
      } catch (err) {
        if (window.cyberAudio) window.cyberAudio.playGlitch();
        showAdminToast(err.message, 'pink');
      }
    });
  }

  // G. Change Master Passcode
  const formSecurity = document.getElementById('admin-form-security');
  if (formSecurity) {
    formSecurity.addEventListener('submit', (e) => {
      e.preventDefault();
      const oldPin = getVal('sec-old-pin');
      const newPin = getVal('sec-new-pin');
      const confirmPin = getVal('sec-confirm-pin');

      if (newPin !== confirmPin) {
        if (window.cyberAudio) window.cyberAudio.playGlitch();
        showAdminToast('KONFIRMASI PASSPHRASE BARU TIDAK COCOK!', 'pink');
        return;
      }

      try {
        window.cyberStore.changePasscode(oldPin, newPin);
        if (window.cyberAudio) window.cyberAudio.playSuccess();
        showAdminToast('MASTER PASSPHRASE BERHASIL DIPERBARUI // AMAN!', 'yellow');
        formSecurity.reset();
      } catch (err) {
        if (window.cyberAudio) window.cyberAudio.playGlitch();
        showAdminToast(err.message, 'pink');
      }
    });
  }

  // H. Export JSON Backup
  const btnExport = document.getElementById('admin-export-backup-btn');
  if (btnExport) {
    btnExport.addEventListener('click', () => {
      if (window.cyberAudio) window.cyberAudio.playScan();
      const jsonStr = window.cyberStore.exportFullDatabaseJSON();
      const blob = new Blob([jsonStr], { type: 'application/json' });
      const url = URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url;
      a.download = 'cyberpunk_portfolio_backup_' + Date.now() + '.json';
      a.click();
      URL.revokeObjectURL(url);
      showAdminToast('DATABASE MATRIX BERHASIL DIEKSPOR (JSON FILE)', 'cyan');
    });
  }

  // I. Import JSON Backup
  const inputImport = document.getElementById('admin-import-file-input');
  if (inputImport) {
    inputImport.addEventListener('change', (e) => {
      const file = e.target.files[0];
      if (file) {
        const reader = new FileReader();
        reader.onload = (evt) => {
          try {
            window.cyberStore.importFullDatabaseJSON(evt.target.result);
            if (window.cyberAudio) window.cyberAudio.playSuccess();
            showAdminToast('DATABASE BERHASIL DIRESTORASI DARI BACKUP!', 'yellow');
            renderDashboardOverview();
          } catch (err) {
            if (window.cyberAudio) window.cyberAudio.playGlitch();
            showAdminToast(err.message, 'pink');
          }
        };
        reader.readAsText(file);
      }
    });
  }
}
