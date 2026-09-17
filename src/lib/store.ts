import { create } from 'zustand'
import { persist, createJSONStorage } from 'zustand/middleware'

export interface Certificate {
  id: string
  image: string
  title: string
  dateAdded: string
}

export interface Project {
  id: string
  image: string
  title: string
  liveUrl: string
  githubUrl: string
  dateAdded: string
}

export interface ContactLink {
  id: string
  label: string
  icon: string
  href: string
  color: string
  order: number
}

export interface ContactInfo {
  id: string
  type: 'email' | 'location' | 'github' | 'custom'
  label: string
  value: string
  href: string
  icon: string
  color: string
  order: number
}

export interface TimelineItem {
  id: string
  year: string
  title: string
  company: string
  desc: string
  tech: string[]
  order: number
}

export interface AboutData {
  bio: string
  philosophy: string[]
  timeline: TimelineItem[]
  stats: Array<{ label: string; value: string; icon: string }>
}

export interface ProfileData {
  name: string
  title: string
  subtitle: string
  description: string
  photo: string
  skills: Array<{ label: string; icon: string }>
}

interface PortfolioStore {
  certificates: Certificate[]
  projects: Project[]
  contactLinks: ContactLink[]
  contactInfo: ContactInfo[]
  aboutData: AboutData
  profileData: ProfileData

  addCertificate: (cert: Omit<Certificate, 'id' | 'dateAdded'>) => void
  updateCertificate: (id: string, data: Partial<Certificate>) => void
  deleteCertificate: (id: string) => void
  reorderCertificates: (certs: Certificate[]) => void

  addProject: (project: Omit<Project, 'id' | 'dateAdded'>) => void
  updateProject: (id: string, data: Partial<Project>) => void
  deleteProject: (id: string) => void
  reorderProjects: (projects: Project[]) => void

  addContactLink: (link: Omit<ContactLink, 'id'>) => void
  updateContactLink: (id: string, data: Partial<ContactLink>) => void
  deleteContactLink: (id: string) => void
  reorderContactLinks: (links: ContactLink[]) => void

  addContactInfo: (info: Omit<ContactInfo, 'id'>) => void
  updateContactInfo: (id: string, data: Partial<ContactInfo>) => void
  deleteContactInfo: (id: string) => void
  reorderContactInfo: (infos: ContactInfo[]) => void

  updateAboutData: (data: Partial<AboutData>) => void
  addTimelineItem: (item: Omit<TimelineItem, 'id'>) => void
  updateTimelineItem: (id: string, data: Partial<TimelineItem>) => void
  deleteTimelineItem: (id: string) => void
  reorderTimeline: (items: TimelineItem[]) => void

  updateProfileData: (data: Partial<ProfileData>) => void
  updateSkill: (index: number, data: { label: string; icon: string }) => void

  initializeDefaults: () => void
}

const defaultContactLinks: ContactLink[] = [
  { id: '1', label: 'GITHUB', icon: 'Github', href: 'https://github.com', color: 'hover:text-white', order: 0 },
  { id: '2', label: 'LINKEDIN', icon: 'Linkedin', href: 'https://linkedin.com', color: 'hover:text-blue-400', order: 1 },
  { id: '3', label: 'TWITTER', icon: 'Twitter', href: 'https://twitter.com', color: 'hover:text-cyan-400', order: 2 },
  { id: '4', label: 'EMAIL', icon: 'Mail', href: 'mailto:dev@example.com', color: 'hover:text-pink-400', order: 3 },
]

const defaultContactInfo: ContactInfo[] = [
  { id: '1', type: 'email', label: 'EMAIL', value: 'dev@cyberpunk.dev', href: 'mailto:dev@cyberpunk.dev', icon: 'Mail', color: 'hover:text-pink-400', order: 0 },
  { id: '2', type: 'location', label: 'LOCATION', value: 'Night City, NC', href: '#', icon: 'MapPin', color: 'hover:text-cyan-400', order: 1 },
  { id: '3', type: 'github', label: 'GITHUB', value: 'github.com/username', href: 'https://github.com', icon: 'Github', color: 'hover:text-white', order: 2 },
]

const defaultAboutData: AboutData = {
  bio: 'Full-stack developer with a passion for building performant, accessible, and visually striking web applications. I specialize in React ecosystem, modern CSS, and creating immersive user experiences.\n\nWhen I\'m not coding, you\'ll find me exploring new frameworks, contributing to open source, or designing cyberpunk-inspired interfaces. I believe in clean code, great UX, and pushing the limits of what\'s possible in the browser.\n\nCurrently exploring: Rust, WebGL, and AI integration.',
  philosophy: [
    'Performance is a feature, not an afterthought',
    'Accessibility opens doors for everyone',
    'Design systems scale, one-off styles don\'t',
    'Type safety prevents bugs before they ship',
    'Animation should enhance, not distract',
  ],
  timeline: [
    { id: '1', year: '2024', title: 'SENIOR DEVELOPER', company: 'Tech Corp', desc: 'Leading frontend architecture & team mentorship', tech: ['React', 'Next.js', 'TypeScript', 'GraphQL'], order: 0 },
    { id: '2', year: '2022', title: 'FULLSTACK DEVELOPER', company: 'StartupXYZ', desc: 'Built scalable web apps from concept to production', tech: ['Node.js', 'PostgreSQL', 'Docker', 'AWS'], order: 1 },
    { id: '3', year: '2020', title: 'JUNIOR DEVELOPER', company: 'Digital Agency', desc: 'Crafted responsive websites & learned best practices', tech: ['Vue.js', 'Tailwind', 'Firebase', 'Git'], order: 2 },
  ],
  stats: [
    { label: 'PROJECTS', value: '50+', icon: 'Award' },
    { label: 'YEARS EXP', value: '3+', icon: 'Briefcase' },
    { label: 'TECHNOLOGIES', value: '20+', icon: 'Heart' },
    { label: 'PASSION', value: '100%', icon: 'Zap' },
  ],
}

const defaultProfileData: ProfileData = {
  name: 'DEVELOPER',
  title: 'HELLO, I\'M',
  subtitle: 'Full-Stack Developer',
  description: 'Crafting immersive digital experiences with clean code & cyberpunk aesthetics. Full-stack developer passionate about performance, accessibility & futuristic UI.',
  photo: '/images/profile/avatar.svg',
  skills: [
    { label: 'FRONTEND', icon: 'Code' },
    { label: 'BACKEND', icon: 'Terminal' },
    { label: 'DEVOPS', icon: 'Server' },
    { label: 'UI/UX', icon: 'MousePointer' },
  ],
}

const defaultCertificates: Certificate[] = [
  { id: '1', image: '/images/certificates/aws-architect.svg', title: 'AWS Certified Solutions Architect', dateAdded: '2024-01-15' },
  { id: '2', image: '/images/certificates/react-advanced.svg', title: 'React Advanced Patterns', dateAdded: '2023-11-20' },
  { id: '3', image: '/images/certificates/cka.svg', title: 'Kubernetes Administrator (CKA)', dateAdded: '2023-08-10' },
]

const defaultProjects: Project[] = [
  { id: '1', image: '/images/projects/project1.svg', title: 'Neural Network Visualizer', liveUrl: '#', githubUrl: '#', dateAdded: '2024-01-10' },
  { id: '2', image: '/images/projects/project2.svg', title: 'Cyberpunk Dashboard', liveUrl: '#', githubUrl: '#', dateAdded: '2023-12-05' },
  { id: '3', image: '/images/projects/project3.svg', title: 'AI Code Review Bot', liveUrl: '#', githubUrl: '#', dateAdded: '2023-11-20' },
  { id: '4', image: '/images/projects/project4.svg', title: 'Realtime Collaborative Editor', liveUrl: '#', githubUrl: '#', dateAdded: '2023-10-15' },
  { id: '5', image: '/images/projects/project5.svg', title: 'E-Commerce Platform', liveUrl: '#', githubUrl: '#', dateAdded: '2023-09-01' },
  { id: '6', image: '/images/projects/project6.svg', title: 'Task Management App', liveUrl: '#', githubUrl: '#', dateAdded: '2023-08-10' },
]

export const usePortfolioStore = create<PortfolioStore>()(
  persist(
    (set, get) => ({
      certificates: [],
      projects: [],
      contactLinks: [],
      contactInfo: [],
      aboutData: { bio: '', philosophy: [], timeline: [], stats: [] },
      profileData: { name: '', title: '', subtitle: '', description: '', photo: '', skills: [] },

      initializeDefaults: () => {
        const { certificates, projects, contactLinks, contactInfo, aboutData, profileData } = get()
        if (certificates.length === 0) set({ certificates: defaultCertificates })
        if (projects.length === 0) set({ projects: defaultProjects })
        if (contactLinks.length === 0) set({ contactLinks: defaultContactLinks })
        if (contactInfo.length === 0) set({ contactInfo: defaultContactInfo })
        if (aboutData.bio === '') set({ aboutData: defaultAboutData })
        if (profileData.name === '') set({ profileData: defaultProfileData })
      },

      addCertificate: (cert) => set((state) => ({ certificates: [{ ...cert, id: Date.now().toString(), dateAdded: new Date().toISOString() }, ...state.certificates] })),
      updateCertificate: (id, data) => set((state) => ({ certificates: state.certificates.map((c) => c.id === id ? { ...c, ...data } : c) })),
      deleteCertificate: (id) => set((state) => ({ certificates: state.certificates.filter((c) => c.id !== id) })),
      reorderCertificates: (certs) => set({ certificates: certs }),

      addProject: (project) => set((state) => ({ projects: [{ ...project, id: Date.now().toString(), dateAdded: new Date().toISOString() }, ...state.projects] })),
      updateProject: (id, data) => set((state) => ({ projects: state.projects.map((p) => p.id === id ? { ...p, ...data } : p) })),
      deleteProject: (id) => set((state) => ({ projects: state.projects.filter((p) => p.id !== id) })),
      reorderProjects: (projects) => set({ projects }),

      addContactLink: (link) => set((state) => ({ contactLinks: [...state.contactLinks, { ...link, id: Date.now().toString() }] })),
      updateContactLink: (id, data) => set((state) => ({ contactLinks: state.contactLinks.map((l) => l.id === id ? { ...l, ...data } : l) })),
      deleteContactLink: (id) => set((state) => ({ contactLinks: state.contactLinks.filter((l) => l.id !== id) })),
      reorderContactLinks: (links) => set({ contactLinks: links }),

      addContactInfo: (info) => set((state) => ({ contactInfo: [...state.contactInfo, { ...info, id: Date.now().toString() }] })),
      updateContactInfo: (id, data) => set((state) => ({ contactInfo: state.contactInfo.map((i) => i.id === id ? { ...i, ...data } : i) })),
      deleteContactInfo: (id) => set((state) => ({ contactInfo: state.contactInfo.filter((i) => i.id !== id) })),
      reorderContactInfo: (infos) => set({ contactInfo: infos }),

      updateAboutData: (data) => set((state) => ({ aboutData: { ...state.aboutData, ...data } })),
      addTimelineItem: (item) => set((state) => ({ aboutData: { ...state.aboutData, timeline: [...state.aboutData.timeline, { ...item, id: Date.now().toString() }] } })),
      updateTimelineItem: (id, data) => set((state) => ({ aboutData: { ...state.aboutData, timeline: state.aboutData.timeline.map((t) => t.id === id ? { ...t, ...data } : t) } })),
      deleteTimelineItem: (id) => set((state) => ({ aboutData: { ...state.aboutData, timeline: state.aboutData.timeline.filter((t) => t.id !== id) } })),
      reorderTimeline: (items) => set((state) => ({ aboutData: { ...state.aboutData, timeline: items } })),

      updateProfileData: (data) => set((state) => ({ profileData: { ...state.profileData, ...data } })),
      updateSkill: (index, data) => set((state) => ({ profileData: { ...state.profileData, skills: state.profileData.skills.map((s, i) => i === index ? data : s) } })),
    }),
    {
      name: 'cyberpunk-portfolio-data',
      storage: createJSONStorage(() => localStorage),
      partialize: (state) => ({
        certificates: state.certificates,
        projects: state.projects,
        contactLinks: state.contactLinks,
        contactInfo: state.contactInfo,
        aboutData: state.aboutData,
        profileData: state.profileData,
      }),
    }
  )
)

export function useCertificates() {
  const { certificates, addCertificate, updateCertificate, deleteCertificate, reorderCertificates, initializeDefaults } = usePortfolioStore()
  return { certificates, addCertificate, updateCertificate, deleteCertificate, reorderCertificates, initializeDefaults }
}

export function useProjects() {
  const { projects, addProject, updateProject, deleteProject, reorderProjects, initializeDefaults } = usePortfolioStore()
  return { projects, addProject, updateProject, deleteProject, reorderProjects, initializeDefaults }
}

export function useContactLinks() {
  const { contactLinks, addContactLink, updateContactLink, deleteContactLink, reorderContactLinks, initializeDefaults } = usePortfolioStore()
  return { contactLinks, addContactLink, updateContactLink, deleteContactLink, reorderContactLinks, initializeDefaults }
}

export function useContactInfo() {
  const { contactInfo, addContactInfo, updateContactInfo, deleteContactInfo, reorderContactInfo, initializeDefaults } = usePortfolioStore()
  return { contactInfo, addContactInfo, updateContactInfo, deleteContactInfo, reorderContactInfo, initializeDefaults }
}

export function useAboutData() {
  const { aboutData, updateAboutData, addTimelineItem, updateTimelineItem, deleteTimelineItem, reorderTimeline, initializeDefaults } = usePortfolioStore()
  return { aboutData, updateAboutData, addTimelineItem, updateTimelineItem, deleteTimelineItem, reorderTimeline, initializeDefaults }
}

export function useProfileData() {
  const { profileData, updateProfileData, updateSkill, initializeDefaults } = usePortfolioStore()
  return { profileData, updateProfileData, updateSkill, initializeDefaults }
}