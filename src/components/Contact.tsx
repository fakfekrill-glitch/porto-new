'use client'

import { useState } from 'react'
import { motion } from 'framer-motion'
import { 
  Mail, Github, Linkedin, Twitter, MapPin, 
  Send, CheckCircle, AlertCircle, Loader2, Link2
} from 'lucide-react'
import { useContactLinks } from '@/lib/store'

const iconMap: Record<string, React.ElementType> = {
  Mail,
  Github,
  Linkedin,
  Twitter,
  MapPin,
}

const colorMap: Record<string, string> = {
  'hover:text-white': 'hover:text-white',
  'hover:text-blue-400': 'hover:text-blue-400',
  'hover:text-cyan-400': 'hover:text-cyan-400',
  'hover:text-pink-400': 'hover:text-pink-400',
}

export function Contact() {
  const [formData, setFormData] = useState({
    name: '',
    email: '',
    subject: '',
    message: '',
  })
  const [status, setStatus] = useState<'idle' | 'sending' | 'success' | 'error'>('idle')
  const [errors, setErrors] = useState<Partial<typeof formData>>({})
  const { contactLinks } = useContactLinks()

  const links = contactLinks?.length ? contactLinks : [
    { id: '1', label: 'GITHUB', icon: 'Github', href: 'https://github.com', color: 'hover:text-white' },
    { id: '2', label: 'LINKEDIN', icon: 'Linkedin', href: 'https://linkedin.com', color: 'hover:text-blue-400' },
    { id: '3', label: 'TWITTER', icon: 'Twitter', href: 'https://twitter.com', color: 'hover:text-cyan-400' },
    { id: '4', label: 'EMAIL', icon: 'Mail', href: 'mailto:dev@example.com', color: 'hover:text-pink-400' },
  ]

  const validateForm = () => {
    const newErrors: Partial<typeof formData> = {}
    if (!formData.name.trim()) newErrors.name = 'Name is required'
    if (!formData.email.trim()) newErrors.email = 'Email is required'
    else if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(formData.email)) newErrors.email = 'Invalid email format'
    if (!formData.subject.trim()) newErrors.subject = 'Subject is required'
    if (!formData.message.trim()) newErrors.message = 'Message is required'
    else if (formData.message.trim().length < 10) newErrors.message = 'Message too short (min 10 chars)'
    setErrors(newErrors)
    return Object.keys(newErrors).length === 0
  }

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault()
    if (!validateForm()) return

    setStatus('sending')
    
    await new Promise(resolve => setTimeout(resolve, 1500))
    
    setStatus('success')
    setFormData({ name: '', email: '', subject: '', message: '' })
    setErrors({})
    
    setTimeout(() => setStatus('idle'), 5000)
  }

  const handleChange = (e: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement>) => {
    const { name, value } = e.target
    setFormData(prev => ({ ...prev, [name]: value }))
    if (errors[name as keyof typeof errors]) {
      setErrors(prev => ({ ...prev, [name]: undefined }))
    }
  }

  return (
    <section id="contact" className="relative py-20 md:py-32 px-4 sm:px-6 lg:px-8">
      <div className="max-w-7xl mx-auto">
        <motion.div
          className="text-center mb-16"
          initial={{ opacity: 0, y: 30 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          transition={{ duration: 0.6 }}
        >
          <span className="font-mono text-xs text-pink-500 uppercase tracking-widest">// CONTACT.GET_IN_TOUCH</span>
          <h2 className="section-title mt-4">LET'S BUILD TOGETHER</h2>
          <p className="section-subtitle mx-auto">
            Have a project in mind? I'm always open to discussing new opportunities
          </p>
        </motion.div>

        <motion.div
          className="grid lg:grid-cols-2 gap-12"
          initial={{ opacity: 0, y: 30 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          transition={{ duration: 0.6, delay: 0.1 }}
        >
          <div className="space-y-8">
            <div className="card-cyber p-8">
              <h3 className="font-display text-xl font-bold text-gradient mb-6 flex items-center gap-3">
                <Mail className="w-6 h-6 text-pink-500" />
                GET IN TOUCH
              </h3>
              <div className="space-y-6">
                {[
                  { icon: Mail, label: 'EMAIL', value: 'dev@cyberpunk.dev', href: 'mailto:dev@cyberpunk.dev' },
                  { icon: MapPin, label: 'LOCATION', value: 'Night City, NC', href: '#' },
                  { icon: Github, label: 'GITHUB', value: 'github.com/username', href: 'https://github.com' },
                ].map((item) => (
                  <a
                    key={item.label}
                    href={item.href}
                    className="flex items-start gap-4 p-4 bg-cyber-darker/50 rounded-lg border border-cyber-border hover:border-pink-500/30 transition-all group"
                    target="_blank"
                    rel="noopener noreferrer"
                  >
                    <div className="w-10 h-10 rounded-lg glass border border-pink-500/20 flex items-center justify-center flex-shrink-0 group-hover:border-pink-500/50 transition-colors">
                      <item.icon className="w-5 h-5 text-pink-500" />
                    </div>
                    <div>
                      <p className="font-mono text-xs text-zinc-500 uppercase tracking-wider">{item.label}</p>
                      <p className="text-zinc-300 group-hover:text-pink-400 transition-colors">{item.value}</p>
                    </div>
                  </a>
                ))}
              </div>
            </div>

            <div className="card-cyber p-8">
              <h3 className="font-display text-xl font-bold text-gradient mb-6 flex items-center gap-3">
                <Github className="w-6 h-6 text-cyan-500" />
                SOCIAL LINKS
              </h3>
              <div className="grid grid-cols-2 gap-4">
                {links.map((social) => {
                  const Icon = iconMap[social.icon] || Link2
                  return (
                    <a
                      key={social.id}
                      href={social.href}
                      target="_blank"
                      rel="noopener noreferrer"
                      className="flex items-center justify-center gap-3 p-4 bg-cyber-darker/50 rounded-lg border border-cyber-border hover:border-pink-500/30 transition-all group"
                    >
                      <Icon className={`w-5 h-5 text-zinc-400 group-hover:text-pink-400 transition-colors ${social.color}`} />
                      <span className="font-mono text-sm text-zinc-300 group-hover:text-white transition-colors">{social.label}</span>
                    </a>
                  )
                })}
              </div>
            </div>

            <div className="card-cyber p-8">
              <h3 className="font-display text-xl font-bold text-gradient mb-6 flex items-center gap-3">
                <CheckCircle className="w-6 h-6 text-green-500" />
                AVAILABILITY
              </h3>
              <div className="space-y-4">
                {[
                  { label: 'Freelance Projects', status: 'OPEN', color: 'text-green-400' },
                  { label: 'Full-time Position', status: 'CLOSED', color: 'text-red-400' },
                  { label: 'Open Source Collab', status: 'OPEN', color: 'text-green-400' },
                  { label: 'Mentoring / Speaking', status: 'LIMITED', color: 'text-yellow-400' },
                ].map((item) => (
                  <div key={item.label} className="flex items-center justify-between p-3 bg-cyber-darker/50 rounded-lg border border-cyber-border">
                    <span className="text-zinc-300">{item.label}</span>
                    <span className={`font-mono text-xs px-2 py-1 rounded border ${item.color} border-current`}>
                      {item.status}
                    </span>
                  </div>
                ))}
              </div>
            </div>
          </div>

          <div className="card-cyber p-8">
            <h3 className="font-display text-xl font-bold text-gradient mb-8 flex items-center gap-3">
              <Send className="w-6 h-6 text-pink-500" />
              SEND MESSAGE
            </h3>

            <form onSubmit={handleSubmit} className="space-y-6" noValidate>
              <div className="grid md:grid-cols-2 gap-6">
                <div>
                  <label htmlFor="name" className="font-mono text-xs text-zinc-500 uppercase tracking-wider block mb-2">
                    NAME
                  </label>
                  <input
                    type="text"
                    id="name"
                    name="name"
                    value={formData.name}
                    onChange={handleChange}
                    className={`input-cyber ${errors.name ? 'border-red-500/50 focus:border-red-500' : ''}`}
                    placeholder="Your name"
                    disabled={status === 'sending'}
                    autoComplete="name"
                  />
                  {errors.name && (
                    <p className="font-mono text-xs text-red-400 mt-1">{errors.name}</p>
                  )}
                </div>

                <div>
                  <label htmlFor="email" className="font-mono text-xs text-zinc-500 uppercase tracking-wider block mb-2">
                    EMAIL
                  </label>
                  <input
                    type="email"
                    id="email"
                    name="email"
                    value={formData.email}
                    onChange={handleChange}
                    className={`input-cyber ${errors.email ? 'border-red-500/50 focus:border-red-500' : ''}`}
                    placeholder="your@email.com"
                    disabled={status === 'sending'}
                    autoComplete="email"
                  />
                  {errors.email && (
                    <p className="font-mono text-xs text-red-400 mt-1">{errors.email}</p>
                  )}
                </div>
              </div>

              <div>
                <label htmlFor="subject" className="font-mono text-xs text-zinc-500 uppercase tracking-wider block mb-2">
                  SUBJECT
                </label>
                <input
                  type="text"
                  id="subject"
                  name="subject"
                  value={formData.subject}
                  onChange={handleChange}
                  className={`input-cyber ${errors.subject ? 'border-red-500/50 focus:border-red-500' : ''}`}
                  placeholder="Project inquiry, collaboration, etc."
                  disabled={status === 'sending'}
                />
                {errors.subject && (
                  <p className="font-mono text-xs text-red-400 mt-1">{errors.subject}</p>
                )}
              </div>

              <div>
                <label htmlFor="message" className="font-mono text-xs text-zinc-500 uppercase tracking-wider block mb-2">
                  MESSAGE
                </label>
                <textarea
                  id="message"
                  name="message"
                  value={formData.message}
                  onChange={handleChange}
                  className={`input-cyber min-h-[150px] resize-y ${errors.message ? 'border-red-500/50 focus:border-red-500' : ''}`}
                  placeholder="Tell me about your project..."
                  disabled={status === 'sending'}
                  rows={5}
                />
                {errors.message && (
                  <p className="font-mono text-xs text-red-400 mt-1">{errors.message}</p>
                )}
              </div>

              <button
                type="submit"
                className="btn-cyber w-full md:w-auto"
                disabled={status === 'sending'}
              >
                {status === 'sending' && <Loader2 className="w-5 h-5 animate-spin mr-2" />}
                {status === 'success' && <CheckCircle className="w-5 h-5 mr-2" />}
                {status === 'error' && <AlertCircle className="w-5 h-5 mr-2" />}
                <span>
                  {status === 'sending' ? 'SENDING...' : 
                   status === 'success' ? 'MESSAGE SENT!' : 
                   status === 'error' ? 'FAILED - TRY AGAIN' : 'TRANSMIT MESSAGE'}
                </span>
              </button>

              {status === 'success' && (
                <motion.p
                  className="font-mono text-sm text-green-400 text-center animate-fade-in"
                  initial={{ opacity: 0, y: 10 }}
                  animate={{ opacity: 1, y: 0 }}
                >
                  Message transmitted successfully! I'll respond within 24 hours.
                </motion.p>
              )}

              {status === 'error' && (
                <motion.p
                  className="font-mono text-sm text-red-400 text-center animate-fade-in"
                  initial={{ opacity: 0, y: 10 }}
                  animate={{ opacity: 1, y: 0 }}
                >
                  Transmission failed. Please try again or email directly.
                </motion.p>
              )}
            </form>
          </div>
        </motion.div>
      </div>
    </section>
  )
}