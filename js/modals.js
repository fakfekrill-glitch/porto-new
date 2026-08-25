/**
 * CYBERPUNK 2077 MODALS & LIGHTBOX CONTROLLER
 * Handles fullscreen media viewer, project deep-dive HUD, and interactive terminal.
 */

class CyberModalController {
  constructor() {
    this.activeModal = null;
    this.currentLightboxItem = null;
    this.initEventListeners();
  }

  initEventListeners() {
    // Close on overlay click
    document.querySelectorAll('.cyber-modal-overlay').forEach((overlay) => {
      overlay.addEventListener('click', (e) => {
        if (e.target === overlay) {
          this.closeModal(overlay.id);
        }
      });
    });

    // Close on ESC key
    window.addEventListener('keydown', (e) => {
      if (e.key === 'Escape' && this.activeModal) {
        this.closeModal(this.activeModal);
      }
    });
  }

  openModal(modalId) {
    const modal = document.getElementById(modalId);
    if (!modal) return;
    if (window.cyberAudio) window.cyberAudio.playClick();
    modal.classList.add('active');
    this.activeModal = modalId;
    document.body.style.overflow = 'hidden';
  }

  closeModal(modalId) {
    const modal = document.getElementById(modalId);
    if (!modal) return;
    if (window.cyberAudio) window.cyberAudio.playHover();
    modal.classList.remove('active');
    this.activeModal = null;
    document.body.style.overflow = 'auto';
  }

  // Open Lightbox for Images/Certificates (Public View)
  openLightbox(item, type = 'gallery') {
    if (window.cyberAudio) window.cyberAudio.playScan();
    this.currentLightboxItem = item;
    const imgEl = document.getElementById('lightbox-image');
    const titleEl = document.getElementById('lightbox-title');
    const metaEl = document.getElementById('lightbox-meta');
    const captionEl = document.getElementById('lightbox-caption');

    if (imgEl) imgEl.src = item.image || '';
    if (titleEl) titleEl.textContent = item.title || 'CYBER_MEDIA';
    if (metaEl) metaEl.textContent = item.issuer || item.tag || item.date || 'VERIFIED';
    if (captionEl) captionEl.textContent = item.caption || item.desc || (item.credentialId ? `Credential ID: ${item.credentialId}` : '');

    this.openModal('modal-lightbox');
  }

  // Open Project Details Modal (Public Deep-Dive HUD)
  openProjectModal(proj) {
    if (window.cyberAudio) window.cyberAudio.playScan();
    const titleEl = document.getElementById('proj-modal-title');
    const codeEl = document.getElementById('proj-modal-code');
    const imgEl = document.getElementById('proj-modal-image');
    const descEl = document.getElementById('proj-modal-desc');
    const specsEl = document.getElementById('proj-modal-specs');
    const tagsContainer = document.getElementById('proj-modal-tags');
    const demoBtn = document.getElementById('proj-modal-demo');
    const repoBtn = document.getElementById('proj-modal-repo');

    if (titleEl) titleEl.textContent = proj.title || '';
    if (codeEl) codeEl.textContent = proj.code || '';
    if (imgEl) imgEl.src = proj.image || '';
    if (descEl) descEl.textContent = proj.desc || '';
    if (specsEl) specsEl.textContent = proj.specs || 'N/A';

    if (tagsContainer && proj.tags) {
      tagsContainer.innerHTML = proj.tags.map((t) => `<span class="card-tag">${t}</span>`).join('');
    }

    if (demoBtn) demoBtn.href = proj.demoUrl || '#';
    if (repoBtn) repoBtn.href = proj.repoUrl || '#';

    this.openModal('modal-project-detail');
  }
}

window.cyberModals = new CyberModalController();
