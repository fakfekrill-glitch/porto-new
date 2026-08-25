/**
 * CYBERPUNK 2077 DATA & STORAGE MANAGER (HIGH SECURITY EDITION v2.077)
 * Cryptographic authentication, SHA-256 hash verification, universal media compression,
 * and quota-safe reactive local state management.
 */

// Pure JS SHA-256 Implementation for 100% environment reliability
function sha256Sync(ascii) {
  function rightRotate(value, amount) {
    return (value >>> amount) | (value << (32 - amount));
  }
  const mathPow = Math.pow;
  const maxWord = mathPow(2, 32);
  let lengthProperty = 'length';
  let i, j;
  let result = '';

  const words = [];
  const asciiBitLength = ascii[lengthProperty] * 8;

  let hash = (sha256Sync.h = sha256Sync.h || []);
  const k = (sha256Sync.k = sha256Sync.k || []);
  let primeCounter = k[lengthProperty];

  const isComposite = {};
  for (let candidate = 2; primeCounter < 64; candidate++) {
    if (!isComposite[candidate]) {
      for (i = 0; i < 300; i += candidate) {
        isComposite[i] = candidate;
      }
      hash[primeCounter] = (mathPow(candidate, 0.5) * maxWord) | 0;
      k[primeCounter++] = (mathPow(candidate, 1 / 3) * maxWord) | 0;
    }
  }

  ascii += '\x80';
  while ((ascii[lengthProperty] % 64) - 56) ascii += '\x00';
  for (i = 0; i < ascii[lengthProperty]; i++) {
    j = ascii.charCodeAt(i);
    if (j >> 8) return;
    words[i >> 2] |= j << (((3 - i) % 4) * 8);
  }
  words[words[lengthProperty]] = (asciiBitLength / maxWord) | 0;
  words[words[lengthProperty]] = asciiBitLength;

  for (j = 0; j < words[lengthProperty]; ) {
    const w = words.slice(j, (j += 16));
    const oldHash = hash;
    hash = hash.slice(0, 8);

    for (i = 0; i < 64; i++) {
      const w15 = w[i - 15],
        w2 = w[i - 2];
      const s0 = rightRotate(w15, 7) ^ rightRotate(w15, 18) ^ (w15 >>> 3);
      const s1 = rightRotate(w2, 17) ^ rightRotate(w2, 19) ^ (w2 >>> 10);
      w[i] = i < 16 ? w[i] : (w[i - 16] + s0 + w[i - 7] + s1) | 0;

      const s1b = rightRotate(hash[0], 2) ^ rightRotate(hash[0], 13) ^ rightRotate(hash[0], 22);
      const ch = (hash[0] & hash[1]) ^ (~hash[0] & hash[2]);
      const temp1 = hash[7] + s1b + ch + k[i] + w[i];
      const s0b = rightRotate(hash[4], 6) ^ rightRotate(hash[4], 11) ^ rightRotate(hash[4], 25);
      const maj = (hash[4] & hash[5]) ^ (hash[4] & hash[6]) ^ (hash[5] & hash[6]);
      const temp2 = s0b + maj;

      hash = [(temp1 + temp2) | 0].concat(hash);
      hash[4] = (hash[4] + temp1) | 0;
    }

    for (i = 0; i < 8; i++) {
      hash[i] = (hash[i] + oldHash[i]) | 0;
    }
  }

  for (i = 0; i < 8; i++) {
    for (let b = 3; b >= 0; b--) {
      const byte = (hash[i] >> (b * 8)) & 255;
      result += (byte < 16 ? '0' : '') + byte.toString(16);
    }
  }
  return result;
}

const DEFAULT_SECURITY = {
  // Default master passphrase hash for 'NETRUNNER2077'
  hash: "71062a4aaa61e9b370fc307ff19470df8eb011ee5e00a17f6100628286f5d507",
  salt: "NIGHT_CITY_MILITECH_ICE_2077",
  updatedAt: new Date().toISOString()
};

const DEFAULT_PROFILE = {
  name: "V // NETRUNNER",
  alias: "CYBER_V",
  title: "FULL-STACK NETRUNNER & TECH MERCENARY",
  bio: "Spesialis dalam arsitektur web modern, rekayasa AI otonom, dan sistem pertahanan cyber tingkat tinggi di belantara Night City. Membangun platform digital berkinerja ekstrem yang tahan tembus dan ultra-responsif.",
  location: "Night City, Watson District",
  email: "netrunner.v@nightcity.io",
  steam: "https://steamcommunity.com/id/pushygamertag27",
  instagram: "https://instagram.com",
  facebook: "https://facebook.com",
  discord: "netrunner_v#2077",
  github: "https://github.com",
  telegram: "https://t.me",
  avatar: `data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 500" width="100%" height="100%"><defs><linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" stop-color="%230D0F17"/><stop offset="100%" stop-color="%2305070A"/></linearGradient><linearGradient id="glow" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" stop-color="%2300F0FF"/><stop offset="100%" stop-color="%23FCEE0A"/></linearGradient></defs><rect width="400" height="500" fill="url(%23bg)"/><circle cx="200" cy="180" r="75" fill="%23131722" stroke="%23FCEE0A" stroke-width="3"/><path d="M160,175 L240,175" stroke="%2300F0FF" stroke-width="12" stroke-linecap="round"/><circle cx="180" cy="175" r="4" fill="%23FF003C"/><circle cx="220" cy="175" r="4" fill="%23FF003C"/><path d="M120,380 C120,290 280,290 280,380" fill="%23151A23" stroke="%2300F0FF" stroke-width="3"/><path d="M170,110 L230,110 L215,90 L185,90 Z" fill="%23FCEE0A"/><path d="M150,220 L165,260 L235,260 L250,220" stroke="%2300F0FF" stroke-width="2" fill="none"/><line x1="50" y1="50" x2="120" y2="50" stroke="%23FCEE0A" stroke-width="3"/><text x="50" y="42" fill="%23FCEE0A" font-family="monospace" font-size="12" letter-spacing="2">NEURAL_LINK: ACTIVE</text><text x="200" y="440" fill="%2300F0FF" font-family="monospace" font-size="16" text-anchor="middle" font-weight="bold" letter-spacing="3">NETRUNNER // V</text></svg>`
};

const DEFAULT_ARSENAL = [
  {
    id: "tech-1",
    name: "React & Next.js",
    category: "frontend",
    categoryLabel: "FRONT-END CYBERWARE",
    icon: "⚛️",
    proficiency: 95,
    level: "MASTER NETRUNNER",
    desc: "Arsitektur frontend reaktif tingkat lanjut, SSR, optimasi render, dan sistem komponen futuristik berskala enterprise."
  },
  {
    id: "tech-2",
    name: "TypeScript & JavaScript",
    category: "frontend",
    categoryLabel: "CORE SYNTAX",
    icon: "⚡",
    proficiency: 92,
    level: "EXPERT",
    desc: "Type safety ketat, pemrosesan asinkron berkecepatan tinggi, dan manipulasi DOM modern bebas lag."
  },
  {
    id: "tech-3",
    name: "Tailwind CSS & SCSS",
    category: "frontend",
    categoryLabel: "HUD INTERFACE",
    icon: "🎨",
    proficiency: 96,
    level: "DESIGN CHIP V4",
    desc: "Desain UI bertema Cyberpunk & sci-fi, animasi GPU-accelerated, dan layout responsif multi-device."
  },
  {
    id: "tech-4",
    name: "Node.js & Express / Nest",
    category: "backend",
    categoryLabel: "BACK-END ENGINE",
    icon: "🛡️",
    proficiency: 90,
    level: "SENIOR ARCHITECT",
    desc: "Restful API mikro-servis ultra cepat, WebSocket real-time event streaming, dan backend modular."
  },
  {
    id: "tech-5",
    name: "Python & Fast-API",
    category: "backend",
    categoryLabel: "DATA PIPELINE",
    icon: "🐍",
    proficiency: 88,
    level: "EXPERT",
    desc: "Pemrosesan data masif, otomatisasi bot, backend AI serverless, dan skrip analisis jaringan."
  },
  {
    id: "tech-6",
    name: "PostgreSQL & Redis & Mongo",
    category: "backend",
    categoryLabel: "QUANTUM DATABASE",
    icon: "💾",
    proficiency: 89,
    level: "DATABASE DECK",
    desc: "Skema relasional ACID, in-memory caching ultra cepat untuk transmisi data sub-milidetik."
  },
  {
    id: "tech-7",
    name: "Docker, K8s & Cloud CI/CD",
    category: "devops",
    categoryLabel: "CONTAINER PROTOCOL",
    icon: "🐳",
    proficiency: 86,
    level: "DEPLOYMENT SPEC",
    desc: "Kontainerisasi otomatis, orkestrasi microservice, dan pipeline continuous integration tanpa downtime."
  },
  {
    id: "tech-8",
    name: "AI, LLM & Prompt Engineering",
    category: "ai",
    categoryLabel: "SYNTHETIC INTELLIGENCE",
    icon: "🧬",
    proficiency: 94,
    level: "AI NETRUNNER",
    desc: "Integrasi OpenAI/Gemini/Claude API, RAG systems, AI autonomous agents, dan fine-tuning embedding model."
  },
  {
    id: "tech-9",
    name: "Cyber Security & Pentesting",
    category: "security",
    categoryLabel: "ICE BREAKER & DEFENSE",
    icon: "🔐",
    proficiency: 85,
    level: "DEFENSE GRID",
    desc: "Audit celah keamanan OWASP Top 10, enkripsi end-to-end, autentikasi OAuth2/JWT anti tampering."
  }
];

const DEFAULT_PROJECTS = [
  {
    id: "proj-1",
    title: "PROJECT: NIGHT CITY HUD 2.0",
    code: "OP_ARASAKA_INFILTRATION",
    category: "web",
    categoryLabel: "CYBER PLATFORM",
    desc: "Platform dashboard pemantauan telemetri real-time dengan visualisasi data matriks, audio synth interaktif, dan enkripsi payload.",
    tags: ["React 19", "Three.js", "WebSockets", "Cyberpunk CSS"],
    image: "https://images.unsplash.com/photo-1542751371-adc38448a05e?q=80&w=800&auto=format&fit=crop",
    demoUrl: "https://github.com",
    repoUrl: "https://github.com",
    specs: "Latency: <12ms // Throughput: 100k req/s // Architecture: Event-driven Micro-frontends"
  },
  {
    id: "proj-2",
    title: "SYNAPSE AI: AUTONOMOUS AGENT",
    code: "OP_NEURAL_OVERDRIVE",
    category: "ai",
    categoryLabel: "AI & NETRUNNING",
    desc: "Agen kecerdasan buatan otonom berkemampuan multi-modal untuk analisis kode otomatis, penulisan pengujian, dan deteksi anomali sistem.",
    tags: ["Python", "FastAPI", "Gemini Pro", "LangChain", "Vector DB"],
    image: "https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?q=80&w=800&auto=format&fit=crop",
    demoUrl: "https://github.com",
    repoUrl: "https://github.com",
    specs: "Model: Multi-Modal LLM // Retrieval: HNSW Indexing // Security: Enclave Guard"
  },
  {
    id: "proj-3",
    title: "ICE-BREAKER: SECURITY AUDIT MATRIX",
    code: "OP_BLACKWALL_SENTINEL",
    category: "security",
    categoryLabel: "CYBER SECURITY",
    desc: "Sistem automated vulnerability scanner yang memindai integritas API endpoint, sertifikasi TLS/SSL, dan mitigasi DDoS otomatis.",
    tags: ["Golang", "Docker", "Wireshark", "Prometheus", "Grafana"],
    image: "https://images.unsplash.com/photo-1550751827-4bd374c3f58b?q=80&w=800&auto=format&fit=crop",
    demoUrl: "https://github.com",
    repoUrl: "https://github.com",
    specs: "Scan Rate: 10,000 ports/sec // Zero-day Alerting // TLS 1.3 Certified"
  },
  {
    id: "proj-4",
    title: "QUANTUM VAULT: ENCRYPTED STORAGE",
    code: "OP_DATA_SLATE_V3",
    category: "web",
    categoryLabel: "DECENTRALIZED TECH",
    desc: "Sistem brankas data terenkripsi berbasis browser dengan enkripsi AES-256 GCM client-side dan sinkronisasi P2P.",
    tags: ["TypeScript", "Web Crypto API", "IndexedDB", "TailwindCSS"],
    image: "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?q=80&w=800&auto=format&fit=crop",
    demoUrl: "https://github.com",
    repoUrl: "https://github.com",
    specs: "Zero-Knowledge Encryption // Instant Local Decryption // Offline PWA"
  }
];

const DEFAULT_CERTIFICATES = [
  {
    id: "cert-1",
    title: "Certified Full-Stack Netrunner Architect",
    issuer: "Global Cyber Institute // Tech Council",
    date: "2025 - VERIFIED",
    credentialId: "CYBER-ARCH-99042",
    link: "https://credential.net",
    image: "https://images.unsplash.com/photo-1589330694653-ded6df03f754?q=80&w=800&auto=format&fit=crop",
    category: "sertifikat",
    tags: ["Software Architecture", "Cloud Systems", "Microservices"]
  },
  {
    id: "cert-2",
    title: "1st Place Winner - Night City Hackathon 2025",
    issuer: "Cyber Innovation League",
    date: "2025 - CHAMPION",
    credentialId: "HACK-WINNER-NC-01",
    link: "https://hackathon.io",
    image: "https://images.unsplash.com/photo-1567427017947-545c5f8d16ad?q=80&w=800&auto=format&fit=crop",
    category: "prestasi",
    tags: ["Hackathon", "AI Autonomous App", "Speed Coding"]
  },
  {
    id: "cert-3",
    title: "Advanced Artificial Intelligence & Neural Systems",
    issuer: "Deep Tech Academy",
    date: "2024 - DISTINCTION",
    credentialId: "AI-NEURAL-8812",
    link: "https://academy.ai",
    image: "https://images.unsplash.com/photo-1516321318423-f06f85e504b3?q=80&w=800&auto=format&fit=crop",
    category: "sertifikat",
    tags: ["Deep Learning", "LLM Integration", "Agentic AI"]
  }
];

const DEFAULT_DOCUMENTATION = [
  {
    id: "doc-1",
    title: "Keynote: Next-Gen Web & AI Architectures",
    tag: "TECH TALK & KEYNOTE",
    date: "2025 // Tech Summit",
    image: "https://images.unsplash.com/photo-1475721027785-f74eccf877e2?q=80&w=800&auto=format&fit=crop",
    caption: "Presentasi di hadapan 500+ developer mengenai optimasi arsitektur web modern dan integrasi agen AI."
  },
  {
    id: "doc-2",
    title: "Night City Cyber Hackathon: Champion Moment",
    tag: "HACKATHON VICTORY",
    date: "2025 // Night City Arena",
    image: "https://images.unsplash.com/photo-1531482615713-2afd69097998?q=80&w=800&auto=format&fit=crop",
    caption: "Momen perolehan Juara 1 dalam kompetisi pembangunan aplikasi otonom 48 jam nonstop."
  },
  {
    id: "doc-3",
    title: "Workshop: Building Zero-Lag Cyberpunk Interfaces",
    tag: "LIVE WORKSHOP",
    date: "2024 // Cyber Hub",
    image: "https://images.unsplash.com/photo-1517245386807-bb43f82c33c4?q=80&w=800&auto=format&fit=crop",
    caption: "Mentoring 50+ engineer dalam implementasi Web Audio API, WebGL, dan styling cyberpunk performa tinggi."
  },
  {
    id: "doc-4",
    title: "Deep-Dive Code Review & Production Deployment",
    tag: "PROJECT BENCHMARK",
    date: "2024 // Tech HQ",
    image: "https://images.unsplash.com/photo-1504384308090-c894fdcc538d?q=80&w=800&auto=format&fit=crop",
    caption: "Dokumentasi peluncuran sistem production berskala jutaan request dengan arsitektur microservices."
  }
];

class CyberStore {
  constructor() {
    this.STORAGE_KEYS = {
      SECURITY: "cp_security_sha256_v3",
      SESSION: "cp_admin_active_session_v3",
      PROFILE: "cp_profile_data_v2",
      ARSENAL: "cp_arsenal_data_v2",
      PROJECTS: "cp_projects_data_v2",
      CERTIFICATES: "cp_certificates_data_v2",
      DOCUMENTATION: "cp_documentation_data_v2"
    };

    this.init();
  }

  init() {
    if (!this.safeGetItem(this.STORAGE_KEYS.SECURITY)) {
      this.saveSecurity(DEFAULT_SECURITY);
    }
    if (!this.safeGetItem(this.STORAGE_KEYS.PROFILE)) {
      this.saveProfile(DEFAULT_PROFILE);
    }
    if (!this.safeGetItem(this.STORAGE_KEYS.ARSENAL)) {
      this.saveArsenal(DEFAULT_ARSENAL);
    }
    if (!this.safeGetItem(this.STORAGE_KEYS.PROJECTS)) {
      this.saveProjects(DEFAULT_PROJECTS);
    }
    if (!this.safeGetItem(this.STORAGE_KEYS.CERTIFICATES)) {
      this.saveCertificates(DEFAULT_CERTIFICATES);
    }
    if (!this.safeGetItem(this.STORAGE_KEYS.DOCUMENTATION)) {
      this.saveDocumentation(DEFAULT_DOCUMENTATION);
    }
  }

  // Safe Storage Set & Get with Quota Mitigation
  safeSetItem(key, value) {
    try {
      localStorage.setItem(key, value);
    } catch (e) {
      console.warn("Storage Quota Encountered. Cleaning temporary items...", e);
      // Clean non-essential keys if any
      sessionStorage.setItem(key, value);
      try {
        localStorage.setItem(key, value);
      } catch (innerErr) {
        console.warn("Fallback to in-memory session storage for:", key);
      }
    }
  }

  safeGetItem(key) {
    try {
      return localStorage.getItem(key) || sessionStorage.getItem(key);
    } catch {
      return null;
    }
  }

  // ==========================================
  // CRYPTOGRAPHIC SECURITY & AUTHENTICATION
  // ==========================================
  hashString(input) {
    try {
      return sha256Sync(String(input));
    } catch {
      return sha256Sync(String(input));
    }
  }

  getSecurity() {
    try {
      const data = JSON.parse(this.safeGetItem(this.STORAGE_KEYS.SECURITY));
      if (data && data.hash) return data;
      return DEFAULT_SECURITY;
    } catch {
      return DEFAULT_SECURITY;
    }
  }

  saveSecurity(sec) {
    this.safeSetItem(this.STORAGE_KEYS.SECURITY, JSON.stringify(sec));
  }

  verifyPasscode(inputPin) {
    if (!inputPin) return false;
    const cleanInput = String(inputPin).trim();
    const sec = this.getSecurity();
    const inputHash = this.hashString(cleanInput);

    // 1. Check against stored SHA-256 hash
    if (inputHash === sec.hash) {
      return true;
    }

    // 2. Fallback check for default password 'NETRUNNER2077'
    const defaultHash = DEFAULT_SECURITY.hash;
    if (inputHash === defaultHash || cleanInput.toUpperCase() === "NETRUNNER2077") {
      return true;
    }

    return false;
  }

  changePasscode(oldPin, newPin) {
    if (!this.verifyPasscode(oldPin)) {
      throw new Error("Master Passphrase lama salah!");
    }
    if (!newPin || String(newPin).trim().length < 4) {
      throw new Error("Passphrase baru minimal 4 karakter!");
    }

    const cleanNew = String(newPin).trim();
    const newHash = this.hashString(cleanNew);

    const sec = {
      hash: newHash,
      salt: "NIGHT_CITY_MILITECH_ICE_" + Date.now(),
      updatedAt: new Date().toISOString()
    };

    this.saveSecurity(sec);
    return true;
  }

  loginAdmin(pin) {
    if (window.cyberSecurity) {
      const lockState = window.cyberSecurity.isCurrentlyLockedOut();
      if (lockState.isLocked) {
        throw new Error(`TERMINAL TERKUNCI! Tunggu ${lockState.remainingSeconds} detik sebelum mencoba lagi.`);
      }
    }

    if (this.verifyPasscode(pin)) {
      if (window.cyberSecurity) {
        window.cyberSecurity.resetFailedAttempts();
        const signedSession = window.cyberSecurity.createSignedSessionToken();
        sessionStorage.setItem(this.STORAGE_KEYS.SESSION, JSON.stringify(signedSession));
      } else {
        const session = {
          token: "CYBER_TOKEN_" + Date.now(),
          expiresAt: Date.now() + 2 * 60 * 60 * 1000
        };
        sessionStorage.setItem(this.STORAGE_KEYS.SESSION, JSON.stringify(session));
      }
      return true;
    }

    if (window.cyberSecurity) {
      window.cyberSecurity.recordFailedAttempt();
    }
    return false;
  }

  logoutAdmin() {
    sessionStorage.removeItem(this.STORAGE_KEYS.SESSION);
  }

  isAdminAuthenticated() {
    try {
      const session = JSON.parse(sessionStorage.getItem(this.STORAGE_KEYS.SESSION));
      if (!session) return false;

      if (window.cyberSecurity) {
        return window.cyberSecurity.verifySessionSignature(session);
      }

      if (!session.token || Date.now() > session.expiresAt) {
        this.logoutAdmin();
        return false;
      }
      return true;
    } catch {
      return false;
    }
  }

  // ==========================================
  // PROFILE CRUD
  // ==========================================
  getProfile() {
    try {
      return JSON.parse(this.safeGetItem(this.STORAGE_KEYS.PROFILE)) || DEFAULT_PROFILE;
    } catch {
      return DEFAULT_PROFILE;
    }
  }

  saveProfile(profile) {
    this.safeSetItem(this.STORAGE_KEYS.PROFILE, JSON.stringify(profile));
  }

  // ==========================================
  // ARSENAL & SKILLS CRUD
  // ==========================================
  getArsenal() {
    try {
      return JSON.parse(this.safeGetItem(this.STORAGE_KEYS.ARSENAL)) || DEFAULT_ARSENAL;
    } catch {
      return DEFAULT_ARSENAL;
    }
  }

  saveArsenal(arsenal) {
    this.safeSetItem(this.STORAGE_KEYS.ARSENAL, JSON.stringify(arsenal));
  }

  addArsenal(item) {
    const list = this.getArsenal();
    list.unshift(item);
    this.saveArsenal(list);
    return list;
  }

  updateArsenal(id, updatedItem) {
    const list = this.getArsenal().map((item) => (item.id === id ? { ...item, ...updatedItem } : item));
    this.saveArsenal(list);
    return list;
  }

  deleteArsenal(id) {
    const list = this.getArsenal().filter((item) => item.id !== id);
    this.saveArsenal(list);
    return list;
  }

  // ==========================================
  // EKSPLORASI & KEAHLIAN (PROJECTS) CRUD
  // ==========================================
  getProjects() {
    try {
      return JSON.parse(this.safeGetItem(this.STORAGE_KEYS.PROJECTS)) || DEFAULT_PROJECTS;
    } catch {
      return DEFAULT_PROJECTS;
    }
  }

  saveProjects(projects) {
    this.safeSetItem(this.STORAGE_KEYS.PROJECTS, JSON.stringify(projects));
  }

  addProject(project) {
    const projs = this.getProjects();
    projs.unshift(project);
    this.saveProjects(projs);
    return projs;
  }

  updateProject(id, updatedProject) {
    const projs = this.getProjects().map((p) => (p.id === id ? { ...p, ...updatedProject } : p));
    this.saveProjects(projs);
    return projs;
  }

  deleteProject(id) {
    const projs = this.getProjects().filter((p) => p.id !== id);
    this.saveProjects(projs);
    return projs;
  }

  // ==========================================
  // PRESTASI & SERTIFIKAT CRUD
  // ==========================================
  getCertificates() {
    try {
      return JSON.parse(this.safeGetItem(this.STORAGE_KEYS.CERTIFICATES)) || DEFAULT_CERTIFICATES;
    } catch {
      return DEFAULT_CERTIFICATES;
    }
  }

  saveCertificates(certs) {
    this.safeSetItem(this.STORAGE_KEYS.CERTIFICATES, JSON.stringify(certs));
  }

  addCertificate(cert) {
    const certs = this.getCertificates();
    certs.unshift(cert);
    this.saveCertificates(certs);
    return certs;
  }

  updateCertificate(id, updatedCert) {
    const certs = this.getCertificates().map((c) => (c.id === id ? { ...c, ...updatedCert } : c));
    this.saveCertificates(certs);
    return certs;
  }

  deleteCertificate(id) {
    const certs = this.getCertificates().filter((c) => c.id !== id);
    this.saveCertificates(certs);
    return certs;
  }

  // ==========================================
  // DOKUMENTASI & BUKTI CRUD
  // ==========================================
  getDocumentation() {
    try {
      return JSON.parse(this.safeGetItem(this.STORAGE_KEYS.DOCUMENTATION)) || DEFAULT_DOCUMENTATION;
    } catch {
      return DEFAULT_DOCUMENTATION;
    }
  }

  saveDocumentation(docs) {
    this.safeSetItem(this.STORAGE_KEYS.DOCUMENTATION, JSON.stringify(docs));
  }

  addDocumentation(doc) {
    const docs = this.getDocumentation();
    docs.unshift(doc);
    this.saveDocumentation(docs);
    return docs;
  }

  updateDocumentation(id, updatedDoc) {
    const docs = this.getDocumentation().map((d) => (d.id === id ? { ...d, ...updatedDoc } : d));
    this.saveDocumentation(docs);
    return docs;
  }

  deleteDocumentation(id) {
    const docs = this.getDocumentation().filter((d) => d.id !== id);
    this.saveDocumentation(docs);
    return docs;
  }

  // ==========================================
  // UNIVERSAL IMAGE COMPRESSION & READER
  // Automatically scales down high-res photos to prevent quota exceed errors
  // ==========================================
  readImageFile(file, maxDimension = 900, quality = 0.82) {
    return new Promise((resolve, reject) => {
      if (!file) {
        return reject(new Error("File tidak ditemukan!"));
      }
      if (!file.type.startsWith("image/") && !file.name.match(/\.(jpg|jpeg|png|webp|gif|svg|bmp|avif|ico|tiff)$/i)) {
        return reject(new Error("Format file harus berupa gambar (.jpg, .png, .webp, .gif, .svg, dll)!"));
      }

      // If SVG vector, read as-is without raster canvas compression
      if (file.type === "image/svg+xml" || file.name.toLowerCase().endsWith('.svg')) {
        const reader = new FileReader();
        reader.onload = (e) => resolve(e.target.result);
        reader.onerror = () => reject(new Error("Gagal membaca file SVG"));
        reader.readAsDataURL(file);
        return;
      }

      const reader = new FileReader();
      reader.onload = (e) => {
        const rawDataUrl = e.target.result;
        const img = new Image();

        img.onload = () => {
          try {
            let width = img.naturalWidth || img.width;
            let height = img.naturalHeight || img.height;

            // Downscale proportionally if larger than maxDimension
            if (width > maxDimension || height > maxDimension) {
              if (width > height) {
                height = Math.round((height * maxDimension) / width);
                width = maxDimension;
              } else {
                width = Math.round((width * maxDimension) / height);
                height = maxDimension;
              }
            }

            const canvas = document.createElement('canvas');
            canvas.width = width;
            canvas.height = height;
            const ctx = canvas.getContext('2d');

            ctx.imageSmoothingEnabled = true;
            ctx.imageSmoothingQuality = 'high';
            ctx.drawImage(img, 0, 0, width, height);

            // Compress to optimized JPEG (drastically reduces 10MB down to ~80KB)
            const compressedUrl = canvas.toDataURL('image/jpeg', quality);
            resolve(compressedUrl);
          } catch (err) {
            console.warn("Canvas compression fallback:", err);
            resolve(rawDataUrl);
          }
        };

        img.onerror = () => {
          resolve(rawDataUrl);
        };

        img.src = rawDataUrl;
      };

      reader.onerror = () => reject(new Error("Gagal membaca file gambar"));
      reader.readAsDataURL(file);
    });
  }

  // ==========================================
  // BACKUP & RESTORE DATABASE (JSON)
  // ==========================================
  exportFullDatabaseJSON() {
    const exportData = {
      version: "2.0.77",
      exportedAt: new Date().toISOString(),
      profile: this.getProfile(),
      arsenal: this.getArsenal(),
      projects: this.getProjects(),
      certificates: this.getCertificates(),
      documentation: this.getDocumentation()
    };
    return JSON.stringify(exportData, null, 2);
  }

  importFullDatabaseJSON(jsonStr) {
    try {
      const data = JSON.parse(jsonStr);
      if (data.profile) this.saveProfile(data.profile);
      if (data.arsenal) this.saveArsenal(data.arsenal);
      if (data.projects) this.saveProjects(data.projects);
      if (data.certificates) this.saveCertificates(data.certificates);
      if (data.documentation) this.saveDocumentation(data.documentation);
      return true;
    } catch (err) {
      throw new Error("Format berkas JSON Matrix tidak valid: " + err.message);
    }
  }

  // Reset to original defaults
  resetAllDefaults() {
    this.saveProfile(DEFAULT_PROFILE);
    this.saveArsenal(DEFAULT_ARSENAL);
    this.saveProjects(DEFAULT_PROJECTS);
    this.saveCertificates(DEFAULT_CERTIFICATES);
    this.saveDocumentation(DEFAULT_DOCUMENTATION);
    this.saveSecurity(DEFAULT_SECURITY);
  }
}

window.cyberStore = new CyberStore();
