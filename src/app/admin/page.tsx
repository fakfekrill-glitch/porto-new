'use client'

import { useState, useEffect } from 'react'
import { motion, AnimatePresence } from 'framer-motion'
import { Lock, Unlock, LogOut, Settings, Image, FileText, Plus, Trash2, Edit, Upload, GripVertical, Save, X, Globe, Github, Link2, LayoutDashboard, User, Crop, Check, RotateCcw, Mail } from 'lucide-react'
import ReactCrop from 'react-image-crop'
import 'react-image-crop/dist/ReactCrop.css'
import { useCertificates, useProjects, useContactLinks, useContactInfo, useAboutData, useProfileData } from '@/lib/store'

const ADMIN_PASSWORD = process.env.NEXT_PUBLIC_ADMIN_PASSWORD || 'cyberpunk2077'

export default function AdminDashboard() {
  const [authenticated, setAuthenticated] = useState(false)
  const [password, setPassword] = useState('')
  const [passwordError, setPasswordError] = useState(false)
  const [activeTab, setActiveTab] = useState<'certificates' | 'projects' | 'contact-links' | 'contact-info' | 'about' | 'profile'>('certificates')
  const [showModal, setShowModal] = useState(false)
  const [editingItem, setEditingItem] = useState<{ type: string; id: string } | null>(null)
  const [modalType, setModalType] = useState<'certificate' | 'project' | 'contact' | 'timeline' | 'profile' | 'contactInfo'>('certificate')
  const [formData, setFormData] = useState({
    title: '',
    image: '',
    imagePreview: '',
    liveUrl: '#',
    githubUrl: '#',
    href: '',
    label: '',
    year: '',
    company: '',
    desc: '',
    tech: '',
    type: 'email',
    value: '',
    icon: 'Mail',
    color: 'hover:text-pink-400',
  })
  const [imageError, setImageError] = useState('')
  const [crop, setCrop] = useState({ x: 0, y: 0, width: 200, height: 200, unit: 'px' as const })
  const [showCropper, setShowCropper] = useState(false)
  const [cropImageSrc, setCropImageSrc] = useState('')

  const { certificates, addCertificate, updateCertificate, deleteCertificate, initializeDefaults: initCerts } = useCertificates()
  const { projects, addProject, updateProject, deleteProject, initializeDefaults: initProjs } = useProjects()
  const { contactLinks, addContactLink, updateContactLink, deleteContactLink, initializeDefaults: initContactLinks } = useContactLinks()
  const { contactInfo, addContactInfo, updateContactInfo, deleteContactInfo, initializeDefaults: initContactInfo } = useContactInfo()
  const { aboutData, updateAboutData, addTimelineItem, updateTimelineItem, deleteTimelineItem, initializeDefaults: initAbout } = useAboutData()
  const { profileData, updateProfileData, initializeDefaults: initProfileData } = useProfileData()

  useEffect(() => {
    initCerts()
    initProjs()
    initContactLinks()
    initAbout()
    initProfileData()
  }, [initCerts, initProjs, initContactLinks, initAbout, initProfileData])

  const handleLogin = () => {
    if (password === ADMIN_PASSWORD) {
      const expiry = Date.now() + 24 * 60 * 60 * 1000
      localStorage.setItem('admin-session', JSON.stringify({ expiry }))
      setAuthenticated(true)
      setPasswordError(false)
      setPassword('')
    } else {
      setPasswordError(true)
      setTimeout(() => setPasswordError(false), 2000)
    }
  }

  const handleLogout = () => {
    localStorage.removeItem('admin-session')
    setAuthenticated(false)
  }

  const handleImageUpload = (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0]
    if (file) {
      if (!file.type.startsWith('image/')) { setImageError('Please select an image file'); return }
      if (file.size > 5 * 1024 * 1024) { setImageError('Image must be less than 5MB'); return }
      const reader = new FileReader()
      reader.onload = (event) => {
        const src = event.target?.result as string
        setFormData(prev => ({ ...prev, image: src, imagePreview: src }))
        setImageError('')
      }
      reader.readAsDataURL(file)
    }
  }

  const getItems = () => {
    switch (activeTab) {
      case 'certificates': return certificates
      case 'projects': return projects
      case 'contact-links': return contactLinks
      case 'contact-info': return contactInfo
      case 'about': return aboutData.timeline
      case 'profile': return [{ ...profileData, id: 'profile' }]
      default: return []
    }
  }

  const getTabLabel = (tab: string) => {
    switch(tab) {
      case 'certificates': return 'CERTIFICATES'
      case 'projects': return 'PROJECTS'
      case 'contact-links': return 'CONTACT LINKS'
      case 'contact-info': return 'CONTACT INFO'
      case 'about': return 'ABOUT'
      case 'profile': return 'PROFILE'
      default: return 'CERTIFICATES'
    }
  }

  const getTabDesc = (tab: string) => {
    switch(tab) {
      case 'certificates': return 'Drag to reorder • Click to edit • Hover for actions'
      case 'projects': return 'Manage project screenshots with links'
      case 'contact-links': return 'Customize social/contact links in footer & contact page'
      case 'contact-info': return 'Manage contact details in Get In Touch section'
      case 'about': return 'Edit bio, philosophy, timeline & stats'
      case 'profile': return 'Update name, subtitle & bio (photo: replace /public/images/profile/avatar.svg)'
      default: return ''
    }
  }

  const getModalType = () => {
    switch (activeTab) {
      case 'certificates': return 'certificate'
      case 'projects': return 'project'
      case 'contact-links': return 'contact'
      case 'contact-info': return 'contactInfo'
      case 'about': return 'timeline'
      case 'profile': return 'profile'
      default: return 'certificate'
    }
  }

  const openAddModal = () => {
    setModalType(getModalType())
    setEditingItem(null)
    setFormData({
      title: '',
      image: '',
      imagePreview: '',
      liveUrl: '#',
      githubUrl: '#',
      href: '',
      label: '',
      year: '',
      company: '',
      desc: '',
      tech: '',
      type: 'email',
      value: '',
      icon: 'Mail',
      color: 'hover:text-pink-400',
    })
    setImageError('')
    setShowModal(true)
  }

  const openEditModal = (item: any) => {
    setModalType(getModalType())
    setEditingItem({ type: getModalType(), id: item.id })
    switch(getModalType()) {
      case 'certificate':
        setFormData({ title: item.title, image: item.image, imagePreview: item.image, liveUrl: '#', githubUrl: '#', href: '', label: '', year: '', company: '', desc: '', tech: '', type: '', value: '', icon: '', color: '' })
        break
      case 'project':
        setFormData({ title: item.title, image: item.image, imagePreview: item.image, liveUrl: item.liveUrl || '#', githubUrl: item.githubUrl || '#', href: '', label: '', year: '', company: '', desc: '', tech: '', type: '', value: '', icon: '', color: '' })
        break
      case 'contact':
        setFormData({ title: '', image: '', imagePreview: '', liveUrl: '#', githubUrl: '#', href: item.href, label: item.label, year: '', company: '', desc: '', tech: '', type: '', value: '', icon: '', color: '' })
        break
      case 'contactInfo':
        setFormData({ title: '', image: '', imagePreview: '', liveUrl: '#', githubUrl: '#', href: item.href, label: item.label, year: '', company: '', desc: '', tech: '', type: item.type, value: item.value, icon: item.icon, color: item.color })
        break
      case 'timeline':
        setFormData({ title: item.title, image: '', imagePreview: '', liveUrl: '#', githubUrl: '#', href: '', label: '', year: item.year, company: item.company, desc: item.desc, tech: item.tech.join(', '), type: '', value: '', icon: '', color: '' })
        break
      case 'profile':
        setFormData({ title: profileData.name, image: '', imagePreview: '', liveUrl: '#', githubUrl: '#', href: '', label: profileData.subtitle, year: '', company: '', desc: profileData.description, tech: '', type: '', value: '', icon: '', color: '' })
        break
    }
    setImageError('')
    setShowModal(true)
  }

  const handleSave = () => {
    if (!formData.title.trim() && modalType !== 'contactInfo') { alert('Title is required'); return }
    if (!formData.label.trim() && modalType === 'contactInfo') { alert('Label is required'); return }
    if (!formData.image && modalType !== 'contact' && modalType !== 'timeline' && modalType !== 'contactInfo') { alert('Please upload an image'); return }

    if (modalType === 'certificate') {
      if (editingItem?.id) updateCertificate(editingItem.id, { title: formData.title, image: formData.image })
      else addCertificate({ title: formData.title, image: formData.image })
    } else if (modalType === 'project') {
      if (editingItem?.id) updateProject(editingItem.id, { title: formData.title, image: formData.image, liveUrl: formData.liveUrl || '#', githubUrl: formData.githubUrl || '#' })
      else addProject({ title: formData.title, image: formData.image, liveUrl: formData.liveUrl || '#', githubUrl: formData.githubUrl || '#' })
    } else if (modalType === 'contact') {
      if (editingItem?.id) updateContactLink(editingItem.id, { label: formData.label, href: formData.href, color: 'hover:text-pink-400' })
      else addContactLink({ label: formData.label, href: formData.href, icon: 'Link2', color: 'hover:text-pink-400', order: contactLinks.length })
    } else if (modalType === 'contactInfo') {
      const contactType = formData.type as 'email' | 'location' | 'github' | 'custom'
      if (editingItem?.id) updateContactInfo(editingItem.id, { label: formData.label, value: formData.value, href: formData.href, icon: formData.icon, color: formData.color, type: contactType })
      else addContactInfo({ label: formData.label, value: formData.value, href: formData.href, icon: formData.icon, color: formData.color, type: contactType, order: contactInfo.length })
    } else if (modalType === 'timeline') {
      if (editingItem?.id) updateTimelineItem(editingItem.id, { year: formData.year, title: formData.title, company: formData.company, desc: formData.desc, tech: formData.tech.split(',').map(s => s.trim()).filter(Boolean) })
      else addTimelineItem({ year: formData.year, title: formData.title, company: formData.company, desc: formData.desc, tech: formData.tech.split(',').map(s => s.trim()).filter(Boolean), order: aboutData.timeline.length })
    } else if (modalType === 'profile') {
      updateProfileData({ name: formData.title, subtitle: formData.label, description: formData.desc })
    }
    setShowModal(false)
  }

  const handleDelete = (id: string) => {
    if (!confirm('Delete this item?')) return
    if (activeTab === 'certificates') deleteCertificate(id)
    else if (activeTab === 'projects') deleteProject(id)
    else if (activeTab === 'contact-links') deleteContactLink(id)
    else if (activeTab === 'contact-info') deleteContactInfo(id)
    else if (activeTab === 'about') deleteTimelineItem(id)
  }

  const items = getItems()

  if (!authenticated) {
    return (
      <div className="min-h-screen flex items-center justify-center px-4 bg-cyber-dark relative overflow-hidden">
        <div className="absolute inset-0" style={{ backgroundImage: 'linear-gradient(rgba(255,0,110,0.03) 1px, transparent 1px), linear-gradient(90deg, rgba(255,0,110,0.03) 1px, transparent 1px)', backgroundSize: '60px 60px' }} />
        <div className="absolute inset-0 opacity-20" style={{ backgroundImage: 'url("data:image/svg+xml,%3Csvg viewBox=%220 0 256 256%22 xmlns=%22http://www.w3.org/2000/svg%22%3E%3Cfilter id=%22noise%22%3E%3CfeTurbulence type=%22fractalNoise%22 baseFrequency=%220.9%22 numOctaves=%224%22 stitchTiles=%22stitch%22/%3E%3C/filter%3E%3Crect width=%22100%25%22 height=%22100%25%22 filter=%22url(%23noise)%22/%3E%3C/svg%3E")' }} />
        <motion.div className="relative z-10 card-cyber w-full max-w-md p-8" initial={{ opacity: 0, y: 30, scale: 0.95 }} animate={{ opacity: 1, y: 0, scale: 1 }} transition={{ duration: 0.5 }}>
          <div className="text-center mb-8">
            <Lock className="w-16 h-16 mx-auto mb-4 text-pink-500" />
            <h1 className="font-display text-2xl font-bold text-gradient mb-2">ADMIN ACCESS</h1>
            <p className="text-zinc-500 font-mono text-sm">Enter password to manage portfolio</p>
          </div>
          <div className="space-y-4">
            <div className="relative">
              <input type="password" value={password} onChange={e => setPassword(e.target.value)} onKeyDown={e => e.key === 'Enter' && handleLogin()} placeholder="PASSWORD" className={`input-cyber text-center text-lg tracking-widest ${passwordError ? 'border-red-500/50' : ''}`} autoFocus autoComplete="current-password" />
              {passwordError && <motion.p className="font-mono text-xs text-red-400 text-center animate-shake">INVALID ACCESS CODE</motion.p>}
            </div>
            <button onClick={handleLogin} className="btn-cyber w-full py-4 text-lg" disabled={!password.trim()}>
              <Unlock className="w-5 h-5 mr-2" /><span>GRANT ACCESS</span>
            </button>
          </div>
          <p className="text-center text-zinc-600 text-xs mt-6 font-mono">Set password in .env.local as NEXT_PUBLIC_ADMIN_PASSWORD</p>
        </motion.div>
      </div>
    )
  }

  return (
    <div className="min-h-screen bg-cyber-dark relative">
      <div className="absolute inset-0" style={{ backgroundImage: 'linear-gradient(rgba(255,0,110,0.02) 1px, transparent 1px), linear-gradient(90deg, rgba(255,0,110,0.02) 1px, transparent 1px)', backgroundSize: '60px 60px' }} />
      
      <header className="relative z-10 border-b border-cyber-border bg-cyber-darker/95 backdrop-blur sticky top-0">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex items-center justify-between h-16">
            <div className="flex items-center gap-4">
              <Settings className="w-8 h-8 text-pink-500" />
              <span className="font-display text-xl font-bold text-gradient">ADMIN DASHBOARD</span>
              <span className="font-mono text-xs px-2 py-1 bg-pink-500/20 text-pink-400 rounded border border-pink-500/30">SECURE</span>
            </div>
            <div className="flex items-center gap-4">
              <span className="font-mono text-xs text-zinc-500 hidden sm:block">SESSION ACTIVE</span>
              <button onClick={handleLogout} className="px-4 py-2 font-mono text-sm uppercase tracking-wider border border-zinc-600 text-zinc-400 hover:border-pink-500 hover:text-pink-400 transition-all rounded-lg flex items-center gap-2">
                <LogOut className="w-4 h-4" /> LOGOUT
              </button>
            </div>
          </div>
          <div className="flex gap-2 pb-4 border-b border-cyber-border flex-wrap">
            <button onClick={() => setActiveTab('certificates')} className={`px-6 py-2 font-mono text-sm uppercase tracking-wider rounded-t-lg transition-all ${activeTab === 'certificates' ? 'bg-pink-500/20 text-pink-400 border-b-2 border-pink-500' : 'text-zinc-500 hover:text-zinc-300'}`}>
              <FileText className="w-4 h-4 mr-2 inline" /> CERTIFICATES <span className="ml-2 px-2 py-0.5 text-xs bg-pink-500/20 text-pink-400 rounded">{certificates.length}</span>
            </button>
            <button onClick={() => setActiveTab('projects')} className={`px-6 py-2 font-mono text-sm uppercase tracking-wider rounded-t-lg transition-all ${activeTab === 'projects' ? 'bg-cyan-500/20 text-cyan-400 border-b-2 border-cyan-500' : 'text-zinc-500 hover:text-zinc-300'}`}>
              <Image className="w-4 h-4 mr-2 inline" /> PROJECTS <span className="ml-2 px-2 py-0.5 text-xs bg-cyan-500/20 text-cyan-400 rounded">{projects.length}</span>
            </button>
            <button onClick={() => setActiveTab('contact-links')} className={`px-6 py-2 font-mono text-sm uppercase tracking-wider rounded-t-lg transition-all ${activeTab === 'contact-links' ? 'bg-purple-500/20 text-purple-400 border-b-2 border-purple-500' : 'text-zinc-500 hover:text-zinc-300'}`}>
              <Link2 className="w-4 h-4 mr-2 inline" /> CONTACT LINKS <span className="ml-2 px-2 py-0.5 text-xs bg-purple-500/20 text-purple-400 rounded">{contactLinks.length}</span>
            </button>
            <button onClick={() => setActiveTab('contact-info')} className={`px-6 py-2 font-mono text-sm uppercase tracking-wider rounded-t-lg transition-all ${activeTab === 'contact-info' ? 'bg-orange-500/20 text-orange-400 border-b-2 border-orange-500' : 'text-zinc-500 hover:text-zinc-300'}`}>
              <Mail className="w-4 h-4 mr-2 inline" /> CONTACT INFO <span className="ml-2 px-2 py-0.5 text-xs bg-orange-500/20 text-orange-400 rounded">{contactInfo.length}</span>
            </button>
            <button onClick={() => setActiveTab('about')} className={`px-6 py-2 font-mono text-sm uppercase tracking-wider rounded-t-lg transition-all ${activeTab === 'about' ? 'bg-green-500/20 text-green-400 border-b-2 border-green-500' : 'text-zinc-500 hover:text-zinc-300'}`}>
              <LayoutDashboard className="w-4 h-4 mr-2 inline" /> ABOUT <span className="ml-2 px-2 py-0.5 text-xs bg-green-500/20 text-green-400 rounded">{aboutData.timeline.length} items</span>
            </button>
            <button onClick={() => setActiveTab('profile')} className={`px-6 py-2 font-mono text-sm uppercase tracking-wider rounded-t-lg transition-all ${activeTab === 'profile' ? 'bg-yellow-500/20 text-yellow-400 border-b-2 border-yellow-500' : 'text-zinc-500 hover:text-zinc-300'}`}>
              <User className="w-4 h-4 mr-2 inline" /> PROFILE
            </button>
          </div>
        </div>
      </header>

      <main className="relative z-10 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        <div className="flex items-center justify-between mb-8 flex-wrap gap-4">
          <div>
            <h2 className="font-display text-2xl font-bold text-white">{getTabLabel(activeTab)}</h2>
            <p className="text-zinc-500 font-mono text-sm mt-1">{getTabDesc(activeTab)}</p>
          </div>
          <motion.button onClick={openAddModal} className="btn-cyber inline-flex items-center gap-2" whileHover={{ scale: 1.02 }} whileTap={{ scale: 0.98 }}>
            <Plus className="w-4 h-4" /><span>ADD {getTabLabel(activeTab)}</span>
          </motion.button>
        </div>

        {items.length === 0 ? (
          <motion.div className="card-cyber p-12 text-center" initial={{ opacity: 0, y: 20 }} animate={{ opacity: 1, y: 0 }}>
            <Image className="w-16 h-16 mx-auto mb-4 text-zinc-600" />
            <h3 className="font-display text-xl font-bold mb-2">NO {getTabLabel(activeTab)} YET</h3>
            <p className="text-zinc-500 mb-6">Add your first item to get started</p>
            <motion.button onClick={openAddModal} className="btn-cyber inline-flex items-center gap-2 mx-auto">
              <Plus className="w-4 h-4" /><span>ADD FIRST ITEM</span>
            </motion.button>
          </motion.div>
        ) : (
          <motion.div className="grid sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-4" initial={{ opacity: 0, y: 20 }} animate={{ opacity: 1, y: 0 }} transition={{ duration: 0.4 }}>
            {items.map((item: any, index) => {
              const isContact = activeTab === 'contact-links'
              const isTimeline = activeTab === 'about'
              const isProfile = activeTab === 'profile'
              const itemImage = isContact ? `/images/certificates/${item.icon?.toLowerCase() || 'link2'}.svg` : isTimeline ? '/images/certificates/calendar.svg' : isProfile ? '/images/profile/avatar.svg' : (item.image || '/images/profile/avatar.svg')
              return (
                <motion.article key={item.id} className="card-cyber group relative overflow-hidden aspect-[4/3] flex flex-col" whileInView={{ opacity: 1, y: 0 }} viewport={{ once: true }} transition={{ delay: index * 0.05 }}>
                  <div className="relative flex-1 overflow-hidden">
                    <img src={itemImage} alt={item.title || item.label || item.name || 'Item'} className="w-full h-full object-cover transition-transform duration-300 group-hover:scale-105" loading="lazy" />
                    <div className="absolute inset-0 bg-gradient-to-t from-cyber-darker/90 via-transparent to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-300" />
                    <div className="absolute top-3 right-3 flex gap-1 opacity-0 group-hover:opacity-100 transition-all duration-300 translate-y-2 group-hover:translate-y-0">
                      <button onClick={() => openEditModal(item)} className="w-9 h-9 rounded-lg glass border border-cyan-500/30 flex items-center justify-center text-cyan-400 hover:bg-cyan-500/10 hover:border-cyan-500 transition-all" aria-label="Edit"><Edit className="w-4 h-4" /></button>
                      <button onClick={() => handleDelete(item.id)} className="w-9 h-9 rounded-lg glass border border-red-500/30 flex items-center justify-center text-red-400 hover:bg-red-500/10 hover:border-red-500 transition-all" aria-label="Delete"><Trash2 className="w-4 h-4" /></button>
                    </div>
                    <div className="absolute bottom-3 left-3 right-3 flex items-center justify-between">
                      {item.dateAdded && <span className="font-mono text-xs bg-cyber-darker/80 px-2 py-1 rounded border border-pink-500/30 text-pink-400">{new Date(item.dateAdded).toLocaleDateString()}</span>}
                      {item.year && <span className="font-mono text-xs bg-cyber-darker/80 px-2 py-1 rounded border border-cyan-500/30 text-cyan-400">{item.year}</span>}
                      <GripVertical className="w-5 h-5 text-zinc-600 cursor-grab active:cursor-grabbing opacity-50" />
                    </div>
                  </div>
                  <div className="p-4 bg-cyber-darker/50 border-t border-cyber-border">
                    <h3 className="font-display font-bold text-sm text-white truncate">{item.title || item.label || item.name || 'Profile'}</h3>
                    {item.liveUrl && item.githubUrl && (
                      <div className="flex gap-2 mt-2">
                        <a href={item.liveUrl} target="_blank" rel="noopener noreferrer" className="font-mono text-xs text-cyan-400 hover:text-cyan-300 flex items-center gap-1" title="Live Demo"><Globe className="w-3 h-3" /> LIVE</a>
                        <a href={item.githubUrl} target="_blank" rel="noopener noreferrer" className="font-mono text-xs text-pink-400 hover:text-pink-300 flex items-center gap-1" title="Source Code"><Github className="w-3 h-3" /> CODE</a>
                      </div>
                    )}
                    {item.href && !item.liveUrl && (
                      <a href={item.href} target="_blank" rel="noopener noreferrer" className="font-mono text-xs text-purple-400 hover:text-purple-300 flex items-center gap-1 mt-2 inline-flex"><Link2 className="w-3 h-3" /> {item.label}</a>
                    )}
                  </div>
                </motion.article>
              )
            })}
          </motion.div>
        )}
      </main>

      <AnimatePresence>
        {showModal && (
          <motion.div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/80 backdrop-blur-sm" initial={{ opacity: 0 }} animate={{ opacity: 1 }} exit={{ opacity: 0 }} onClick={() => setShowModal(false)}>
            <motion.div className="card-cyber w-full max-w-2xl max-h-[90vh] overflow-y-auto" initial={{ opacity: 0, scale: 0.95, y: 20 }} animate={{ opacity: 1, scale: 1, y: 0 }} exit={{ opacity: 0, scale: 0.95, y: 20 }} onClick={e => e.stopPropagation()}>
              <div className="p-6">
                <div className="flex items-center justify-between mb-6">
                  <h3 className="font-display text-xl font-bold text-gradient">{editingItem ? 'EDIT' : 'ADD'} {getTabLabel(activeTab).slice(0, -1)}</h3>
                  <button onClick={() => setShowModal(false)} className="w-8 h-8 rounded-lg glass border border-zinc-600 flex items-center justify-center text-zinc-400 hover:text-white hover:border-pink-500 transition-all"><X className="w-4 h-4" /></button>
                </div>
                <div className="space-y-4">
                  <div className="relative aspect-[4/3] rounded-lg overflow-hidden bg-cyber-darker border border-cyber-border">
                    {formData.imagePreview ? <img src={formData.imagePreview} alt="Preview" className="w-full h-full object-cover" /> : (
                      <label className="w-full h-full flex flex-col items-center justify-center cursor-pointer text-zinc-500 hover:text-pink-400 transition-colors p-4">
                        <Upload className="w-12 h-12 mb-3 opacity-50" />
                        <span className="font-mono text-sm">CLICK TO UPLOAD IMAGE</span>
                        <span className="text-xs text-zinc-600 mt-1">JPG, PNG up to 5MB</span>
                        <input type="file" accept="image/*" onChange={handleImageUpload} className="hidden" id="admin-image-upload" />
                      </label>
                    )}
                    {imageError && <div className="absolute bottom-0 left-0 right-0 bg-red-500/90 text-white text-xs font-mono px-3 py-2">{imageError}</div>}
                  </div>
                  <input type="text" placeholder="TITLE / NAME *" value={formData.title} onChange={e => setFormData(prev => ({ ...prev, title: e.target.value }))} className="input-cyber" required autoFocus />
                  {modalType === 'project' && (
                    <>
                      <input type="url" placeholder="LIVE DEMO URL" value={formData.liveUrl} onChange={e => setFormData(prev => ({ ...prev, liveUrl: e.target.value }))} className="input-cyber" />
                      <input type="url" placeholder="GITHUB REPO URL" value={formData.githubUrl} onChange={e => setFormData(prev => ({ ...prev, githubUrl: e.target.value }))} className="input-cyber" />
                    </>
                  )}
                  {modalType === 'contact' && (
                    <>
                      <input type="text" placeholder="LABEL (e.g. GITHUB, EMAIL)" value={formData.label} onChange={e => setFormData(prev => ({ ...prev, label: e.target.value }))} className="input-cyber" required />
                      <input type="url" placeholder="LINK URL (e.g. https://github.com/you, mailto:you@email.com)" value={formData.href} onChange={e => setFormData(prev => ({ ...prev, href: e.target.value }))} className="input-cyber" required />
                    </>
                  )}
                  {modalType === 'contactInfo' && (
                    <>
                      <input type="text" placeholder="LABEL (e.g. EMAIL, LOCATION, GITHUB)" value={formData.label} onChange={e => setFormData(prev => ({ ...prev, label: e.target.value }))} className="input-cyber" required />
                      <input type="text" placeholder="VALUE (e.g. dev@email.com, Night City, NC, github.com/you)" value={formData.value} onChange={e => setFormData(prev => ({ ...prev, value: e.target.value }))} className="input-cyber" required />
                      <input type="url" placeholder="LINK URL (e.g. mailto:dev@email.com, #, https://github.com/you)" value={formData.href} onChange={e => setFormData(prev => ({ ...prev, href: e.target.value }))} className="input-cyber" required />
                      <select value={formData.type} onChange={e => setFormData(prev => ({ ...prev, type: e.target.value }))} className="input-cyber">
                        <option value="email">EMAIL</option>
                        <option value="location">LOCATION</option>
                        <option value="github">GITHUB</option>
                        <option value="custom">CUSTOM</option>
                      </select>
                      <input type="text" placeholder="ICON NAME (Mail, MapPin, Github, Link2, Twitter, Linkedin)" value={formData.icon} onChange={e => setFormData(prev => ({ ...prev, icon: e.target.value }))} className="input-cyber" />
                      <input type="text" placeholder="COLOR CLASS (hover:text-pink-400, hover:text-cyan-400, etc.)" value={formData.color} onChange={e => setFormData(prev => ({ ...prev, color: e.target.value }))} className="input-cyber" />
                    </>
                  )}
                  {modalType === 'timeline' && (
                    <>
                      <input type="text" placeholder="YEAR (e.g. 2024)" value={formData.year} onChange={e => setFormData(prev => ({ ...prev, year: e.target.value }))} className="input-cyber" required />
                      <input type="text" placeholder="TITLE / ROLE" value={formData.title} onChange={e => setFormData(prev => ({ ...prev, title: e.target.value }))} className="input-cyber" required />
                      <input type="text" placeholder="COMPANY" value={formData.company} onChange={e => setFormData(prev => ({ ...prev, company: e.target.value }))} className="input-cyber" />
                      <textarea placeholder="DESCRIPTION" value={formData.desc} onChange={e => setFormData(prev => ({ ...prev, desc: e.target.value }))} className="input-cyber min-h-[80px]" rows={3} />
                      <input type="text" placeholder="TECH STACK (comma separated)" value={formData.tech} onChange={e => setFormData(prev => ({ ...prev, tech: e.target.value }))} className="input-cyber" />
                    </>
                  )}
                  {modalType === 'profile' && (
                    <>
                      <input type="text" placeholder="NAME" value={formData.title} onChange={e => setFormData(prev => ({ ...prev, title: e.target.value }))} className="input-cyber" required />
                      <input type="text" placeholder="SUBTITLE (e.g. Full-Stack Developer)" value={formData.label} onChange={e => setFormData(prev => ({ ...prev, label: e.target.value }))} className="input-cyber" />
                      <textarea placeholder="BIO / DESCRIPTION" value={formData.desc} onChange={e => setFormData(prev => ({ ...prev, desc: e.target.value }))} className="input-cyber min-h-[80px]" rows={3} />
                    </>
                  )}
                  <div className="flex gap-3 pt-4">
                    <button onClick={() => setShowModal(false)} className="flex-1 px-4 py-3 font-mono text-sm uppercase tracking-wider border border-zinc-600 text-zinc-400 hover:border-pink-500 hover:text-pink-400 transition-all rounded-lg">CANCEL</button>
                    <button onClick={handleSave} className="btn-cyber flex-1"><Save className="w-4 h-4 mr-2" /><span>{editingItem ? 'UPDATE' : 'SAVE'}</span></button>
                  </div>
                </div>
              </div>
            </motion.div>
          </motion.div>
        )}
      </AnimatePresence>

      <AnimatePresence>
        {showCropper && cropImageSrc && (
          <motion.div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/90 backdrop-blur-sm" initial={{ opacity: 0 }} animate={{ opacity: 1 }} exit={{ opacity: 0 }} onClick={() => setShowCropper(false)}>
            <motion.div className="card-cyber w-full max-w-4xl max-h-[90vh] overflow-hidden" initial={{ opacity: 0, scale: 0.95, y: 20 }} animate={{ opacity: 1, scale: 1, y: 0 }} exit={{ opacity: 0, scale: 0.95, y: 20 }} onClick={e => e.stopPropagation()}>
              <div className="p-4 border-b border-cyber-border flex items-center justify-between">
                <h3 className="font-display text-lg font-bold text-gradient">CROP PROFILE IMAGE</h3>
                <div className="flex items-center gap-2">
                  <button onClick={() => setCrop(prev => ({ ...prev, x: Math.max(0, prev.x - 10) }))} className="w-8 h-8 rounded-lg glass border border-zinc-600 flex items-center justify-center text-zinc-400 hover:text-white hover:border-pink-500 transition-all" title="Move Left"><Crop className="w-4 h-4 rotate-180" /></button>
                  <button onClick={() => setCrop(prev => ({ ...prev, y: Math.max(0, prev.y - 10) }))} className="w-8 h-8 rounded-lg glass border border-zinc-600 flex items-center justify-center text-zinc-400 hover:text-white hover:border-pink-500 transition-all" title="Move Up"><Crop className="w-4 h-4 rotate-90" /></button>
                  <button onClick={() => setCrop(prev => ({ ...prev, y: prev.y + 10 }))} className="w-8 h-8 rounded-lg glass border border-zinc-600 flex items-center justify-center text-zinc-400 hover:text-white hover:border-pink-500 transition-all" title="Move Down"><Crop className="w-4 h-4 rotate-270" /></button>
                  <button onClick={() => setCrop(prev => ({ ...prev, x: prev.x + 10 }))} className="w-8 h-8 rounded-lg glass border border-zinc-600 flex items-center justify-center text-zinc-400 hover:text-white hover:border-pink-500 transition-all" title="Move Right"><Crop className="w-4 h-4" /></button>
                  <button onClick={() => setCrop({ x: 0, y: 0, width: 300, height: 300, unit: 'px' })} className="w-8 h-8 rounded-lg glass border border-zinc-600 flex items-center justify-center text-zinc-400 hover:text-white hover:border-pink-500 transition-all" title="Reset"><RotateCcw className="w-4 h-4" /></button>
                  <button onClick={() => setShowCropper(false)} className="w-8 h-8 rounded-lg glass border border-zinc-600 flex items-center justify-center text-zinc-400 hover:text-white hover:border-red-500 transition-all"><X className="w-4 h-4" /></button>
                </div>
              </div>
              <div className="p-4 relative">
                <div className="max-h-[60vh] overflow-auto">
                  <ReactCrop
                    crop={crop}
                    onChange={setCrop}
                    aspect={1}
                    minWidth={100}
                    minHeight={100}
                    keepSelection
                    ruleOfThirds
                    circularCrop
                  >
                    <img src={cropImageSrc} alt="Crop preview" />
                  </ReactCrop>
                </div>
                <div className="flex gap-3 pt-4 justify-end">
                  <button onClick={() => setShowCropper(false)} className="px-4 py-2 font-mono text-sm uppercase tracking-wider border border-zinc-600 text-zinc-400 hover:border-pink-500 hover:text-pink-400 transition-all rounded-lg">CANCEL</button>
                  <button
                    onClick={() => {
                      const canvas = document.createElement('canvas')
                      canvas.width = crop.width
                      canvas.height = crop.height
                      const ctx = canvas.getContext('2d')
                      const img = new window.Image()
                      img.crossOrigin = 'anonymous'
                      img.src = cropImageSrc
                      img.onload = () => {
                        if (!ctx) return
                        const scaleX = img.naturalWidth / img.width
                        const scaleY = img.naturalHeight / img.height
                        ctx.clearRect(0, 0, canvas.width, canvas.height)
                        ctx.drawImage(
                          img,
                          crop.x * scaleX,
                          crop.y * scaleY,
                          crop.width * scaleX,
                          crop.height * scaleY,
                          0, 0,
                          crop.width,
                          crop.height
                        )
                        const croppedDataUrl = canvas.toDataURL('image/png')
                        setFormData(prev => ({ ...prev, image: croppedDataUrl, imagePreview: croppedDataUrl }))
                        setShowCropper(false)
                      }
                      img.onerror = () => {
                        setShowCropper(false)
                        alert('Failed to crop image')
                      }
                    }}
                    className="btn-cyber"
                  >
                    <Check className="w-4 h-4 mr-2" />
                    <span>APPLY CROP</span>
                  </button>
                </div>
              </div>
            </motion.div>
          </motion.div>
        )}
      </AnimatePresence>
    </div>
  )
}