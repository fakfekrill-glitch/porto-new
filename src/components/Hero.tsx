'use client'

import { motion } from 'framer-motion'
import { MousePointer, Keyboard, Code, Terminal } from 'lucide-react'
import { CyberBackground, FloatingParticles } from './CyberBackground'
import { useProfileData } from '@/lib/store'

const defaultSkills = [
  { icon: Code, label: 'FRONTEND', desc: 'React, Next.js, TypeScript, Tailwind' },
  { icon: Terminal, label: 'BACKEND', desc: 'Node.js, Python, Go, PostgreSQL' },
  { icon: Keyboard, label: 'DEVOPS', desc: 'Docker, Kubernetes, AWS, Vercel' },
  { icon: MousePointer, label: 'UI/UX', desc: 'Figma, Framer Motion, GSAP' },
]

export function Hero() {
  const { profileData } = useProfileData()

  const name = profileData.name || 'DEVELOPER'
  const title = profileData.title || "HELLO, I'M"
  const subtitle = profileData.subtitle || 'Full-Stack Developer'
  const description = profileData.description || 'Crafting immersive digital experiences with clean code & cyberpunk aesthetics. Full-stack developer passionate about performance, accessibility & futuristic UI.'
  const photo = profileData.photo || '/images/profile/avatar.jpg'
  const skills = profileData.skills?.length ? profileData.skills : defaultSkills

  return (
    <section id="hero" className="relative min-h-screen flex items-center justify-center px-4 sm:px-6 lg:px-8 pt-16">
      <CyberBackground />
      <FloatingParticles />
      
      <div className="relative z-10 w-full max-w-7xl mx-auto">
        <motion.div
          className="grid lg:grid-cols-2 gap-12 lg:gap-20 items-center"
          initial={{ opacity: 0, y: 30 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.8, ease: 'easeOut' }}
        >
          <div>
            <motion.div
              className="inline-flex items-center gap-2 px-4 py-2 rounded-full glass border border-pink-500/30 mb-6"
              initial={{ opacity: 0, x: -20 }}
              animate={{ opacity: 1, x: 0 }}
              transition={{ delay: 0.2 }}
            >
              <motion.span
                className="w-2 h-2 rounded-full bg-pink-500"
                animate={{ scale: [1, 1.5, 1], opacity: [1, 0.5, 1] }}
                transition={{ duration: 1.5, repeat: Infinity }}
              />
              <span className="font-mono text-xs text-pink-400 uppercase tracking-wider">
                SYSTEM ONLINE
              </span>
              <span className="font-mono text-xs text-cyan-400 uppercase tracking-wider">
                v2.0.77
              </span>
            </motion.div>

            <motion.h1
              className="font-display font-black text-5xl md:text-7xl lg:text-8xl leading-[0.95] tracking-tighter mb-6"
              initial={{ opacity: 0, y: 30 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ delay: 0.3, duration: 0.6 }}
            >
              <span className="text-white">{title}</span>
              <br />
              <span className="glitch-text text-gradient" data-text={name}>
                {name}
              </span>
            </motion.h1>

            <motion.p
              className="text-lg md:text-xl text-zinc-300 max-w-xl mb-8 leading-relaxed font-light"
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ delay: 0.4, duration: 0.6 }}
            >
              {description}
            </motion.p>

            <motion.div
              className="flex flex-wrap items-center gap-4 mb-12"
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ delay: 0.5, duration: 0.6 }}
            >
              <a
                href="#projects"
                className="btn-cyber group"
                onClick={(e) => { e.preventDefault(); document.getElementById('projects')?.scrollIntoView({ behavior: 'smooth' }); }}
              >
                <span>VIEW WORK</span>
                <motion.span
                  className="ml-2 inline-block"
                  animate={{ x: [0, 4, 0] }}
                  transition={{ duration: 1.5, repeat: Infinity }}
                >
                  →
                </motion.span>
              </a>
              <a
                href="#contact"
                className="px-6 py-3 font-mono text-sm uppercase tracking-wider transition-all duration-300 border border-cyan-500/30 text-cyan-400 hover:bg-cyan-500/10 hover:text-cyan-300 rounded-lg group"
                onClick={(e) => { e.preventDefault(); document.getElementById('contact')?.scrollIntoView({ behavior: 'smooth' }); }}
              >
                <span>GET IN TOUCH</span>
              </a>
            </motion.div>

            <motion.div
              className="flex flex-wrap items-center gap-6 text-zinc-500"
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ delay: 0.6, duration: 0.6 }}
            >
              {skills.map((skill, index) => (
                <motion.div
                  key={skill.label}
                  className="flex items-center gap-2"
                  initial={{ opacity: 0, y: 10 }}
                  animate={{ opacity: 1, y: 0 }}
                  transition={{ delay: 0.7 + index * 0.1 }}
                >
                  <skill.icon className="w-5 h-5 text-pink-500" />
                  <span className="font-mono text-xs uppercase tracking-wider text-zinc-400">{skill.label}</span>
                </motion.div>
              ))}
            </motion.div>
          </div>

          <motion.div
            className="relative"
            initial={{ opacity: 0, x: 50 }}
            animate={{ opacity: 1, x: 0 }}
            transition={{ delay: 0.4, duration: 0.8 }}
          >
            <div className="relative aspect-square max-w-md mx-auto">
              <div className="absolute inset-0 bg-gradient-to-br from-pink-500/20 via-transparent to-cyan-500/20 rounded-3xl blur-2xl animate-pulse-neon" />
              
              <div className="relative aspect-square glass rounded-3xl border border-pink-500/20 overflow-hidden neon-border">
                <div className="absolute inset-0 bg-gradient-to-br from-pink-500/5 via-transparent to-cyan-500/5" />
                
                <div className="absolute top-4 left-4 right-4 flex items-center justify-between">
                  <div className="flex gap-2">
                    <div className="w-3 h-3 rounded-full bg-red-500/80 animate-pulse" />
                    <div className="w-3 h-3 rounded-full bg-yellow-500/80" />
                    <div className="w-3 h-3 rounded-full bg-green-500/80" />
                  </div>
                  <div className="font-mono text-xs text-zinc-500 px-3 py-1 bg-cyber-darker/50 rounded">
                    profile.tsx
                  </div>
                </div>

                <div className="absolute inset-0 flex items-center justify-center p-8">
                  <motion.div
                    className="relative w-48 h-48 md:w-64 md:h-64"
                    animate={{ rotate: [0, 1, -1, 0], scale: [1, 1.02, 1] }}
                    transition={{ duration: 4, repeat: Infinity, ease: 'easeInOut' }}
                  >
                    <div className="relative w-full h-full rounded-2xl overflow-hidden glass border border-pink-500/20">
                      <div className="absolute inset-0 bg-gradient-to-br from-pink-500/10 via-transparent to-cyan-500/10" />
                      <img
                        src={photo}
                        alt="Profile"
                        className="w-full h-full object-cover"
                      />
                      <div className="absolute inset-0 bg-gradient-to-t from-cyber-darker/80 via-transparent to-transparent" />
                    </div>
                    
                    <motion.div
                      className="absolute -bottom-4 -right-4 w-16 h-16 rounded-full glass border border-cyan-500/30 flex items-center justify-center"
                      animate={{ rotate: [0, 360] }}
                      transition={{ duration: 20, repeat: Infinity, ease: 'linear' }}
                    >
                      <Code className="w-8 h-8 text-cyan-400" />
                    </motion.div>
                    
                    <motion.div
                      className="absolute -top-4 -left-4 w-12 h-12 rounded-full glass border border-pink-500/30 flex items-center justify-center"
                      animate={{ rotate: [0, -360] }}
                      transition={{ duration: 15, repeat: Infinity, ease: 'linear' }}
                    >
                      <Terminal className="w-6 h-6 text-pink-400" />
                    </motion.div>
                  </motion.div>
                </div>

                <div className="absolute bottom-4 left-4 right-4 grid grid-cols-3 gap-2 text-center">
                  {skills.slice(0, 3).map((skill, i) => (
                    <motion.div
                      key={skill.label}
                      className="px-3 py-1.5 font-mono text-xs bg-cyber-darker/50 border border-pink-500/20 rounded transition-all hover:border-pink-500/50 hover:text-pink-400"
                      initial={{ opacity: 0, y: 10 }}
                      animate={{ opacity: 1, y: 0 }}
                      transition={{ delay: 0.8 + i * 0.1 }}
                    >
                      {skill.label}
                    </motion.div>
                  ))}
                </div>
              </div>
            </div>

            <motion.div
              className="absolute -bottom-8 left-1/2 -translate-x-1/2 flex items-center gap-4"
              animate={{ y: [0, 10, 0] }}
              transition={{ duration: 2, repeat: Infinity }}
            >
              <motion.div
                className="w-8 h-8 rounded-full border-2 border-pink-500/50 flex items-center justify-center"
                animate={{ scale: [1, 1.2, 1], borderColor: ['#FF006E', '#00F3FF', '#FF006E'] }}
                transition={{ duration: 2, repeat: Infinity }}
              >
                <MousePointer className="w-4 h-4 text-pink-500" />
              </motion.div>
              <span className="font-mono text-xs text-zinc-500 uppercase tracking-wider hidden sm:block">
                SCROLL
              </span>
              <motion.div
                className="w-8 h-8 rounded-full border-2 border-cyan-500/50 flex items-center justify-center"
                animate={{ scale: [1, 1.2, 1], borderColor: ['#00F3FF', '#FF006E', '#00F3FF'] }}
                transition={{ duration: 2, repeat: Infinity, delay: 1 }}
              >
                <Keyboard className="w-4 h-4 text-cyan-500" />
              </motion.div>
            </motion.div>
          </motion.div>
        </motion.div>
      </div>
    </section>
  )
}