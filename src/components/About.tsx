'use client'

import { motion } from 'framer-motion'
import { User, Award, Briefcase, Heart, Brain, Zap } from 'lucide-react'
import { useAboutData } from '@/lib/store'

const iconMap: Record<string, React.ElementType> = {
  Award,
  Briefcase,
  Heart,
  Zap,
  User,
  Brain,
}

export function About() {
  const { aboutData } = useAboutData()

  const bio = aboutData.bio || 'Full-stack developer with a passion for building performant, accessible, and visually striking web applications. I specialize in React ecosystem, modern CSS, and creating immersive user experiences.\n\nWhen I\'m not coding, you\'ll find me exploring new frameworks, contributing to open source, or designing cyberpunk-inspired interfaces. I believe in clean code, great UX, and pushing the limits of what\'s possible in the browser.\n\nCurrently exploring: Rust, WebGL, and AI integration.'
  const philosophy = aboutData.philosophy?.length ? aboutData.philosophy : [
    'Performance is a feature, not an afterthought',
    'Accessibility opens doors for everyone',
    'Design systems scale, one-off styles don\'t',
    'Type safety prevents bugs before they ship',
    'Animation should enhance, not distract',
  ]
  const timeline = aboutData.timeline?.length ? aboutData.timeline : [
    { id: '1', year: '2024', title: 'SENIOR DEVELOPER', company: 'Tech Corp', desc: 'Leading frontend architecture & team mentorship', tech: ['React', 'Next.js', 'TypeScript', 'GraphQL'], order: 0 },
    { id: '2', year: '2022', title: 'FULLSTACK DEVELOPER', company: 'StartupXYZ', desc: 'Built scalable web apps from concept to production', tech: ['Node.js', 'PostgreSQL', 'Docker', 'AWS'], order: 1 },
    { id: '3', year: '2020', title: 'JUNIOR DEVELOPER', company: 'Digital Agency', desc: 'Crafted responsive websites & learned best practices', tech: ['Vue.js', 'Tailwind', 'Firebase', 'Git'], order: 2 },
  ]
  const stats = aboutData.stats?.length ? aboutData.stats : [
    { label: 'PROJECTS', value: '50+', icon: 'Award' },
    { label: 'YEARS EXP', value: '3+', icon: 'Briefcase' },
    { label: 'TECHNOLOGIES', value: '20+', icon: 'Heart' },
    { label: 'PASSION', value: '100%', icon: 'Zap' },
  ]

  return (
    <section id="about" className="relative py-20 md:py-32 px-4 sm:px-6 lg:px-8">
      <div className="max-w-7xl mx-auto">
        <motion.div
          className="text-center mb-16"
          initial={{ opacity: 0, y: 30 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          transition={{ duration: 0.6 }}
        >
          <span className="font-mono text-xs text-pink-500 uppercase tracking-widest">// ABOUT.ME</span>
          <h2 className="section-title mt-4">ABOUT ME</h2>
          <p className="section-subtitle mx-auto">
            Passionate developer crafting digital experiences that push boundaries
          </p>
        </motion.div>

        <motion.div
          className="grid lg:grid-cols-3 gap-8 mb-16"
          initial={{ opacity: 0, y: 30 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          transition={{ duration: 0.6, delay: 0.1 }}
        >
          {stats.map((stat, index) => {
            const Icon = iconMap[stat.icon]
            return (
              <motion.div
                key={stat.label}
                className="card-cyber text-center group"
                whileInView={{ opacity: 1, y: 0 }}
                viewport={{ once: true }}
                transition={{ delay: 0.1 + index * 0.1 }}
              >
                <div className="flex items-center justify-center gap-3 mb-4">
                  {Icon && <Icon className="w-8 h-8 text-pink-500 group-hover:text-cyan-400 transition-colors" />}
                  <span className="font-display text-3xl font-bold text-gradient">{stat.value}</span>
                </div>
                <p className="font-mono text-xs text-zinc-400 uppercase tracking-wider">{stat.label}</p>
              </motion.div>
            )
          })}
        </motion.div>

        <motion.div
          className="grid lg:grid-cols-2 gap-12 items-start"
          initial={{ opacity: 0, y: 30 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          transition={{ duration: 0.6, delay: 0.2 }}
        >
          <div className="space-y-6">
            <div className="card-cyber p-8">
              <h3 className="font-display text-xl font-bold text-gradient mb-6 flex items-center gap-3">
                <User className="w-6 h-6 text-pink-500" />
                WHO AM I
              </h3>
              <div className="space-y-4 text-zinc-300 leading-relaxed">
                {bio.split('\n\n').map((paragraph, i) => (
                  <p key={i}>{paragraph}</p>
                ))}
              </div>
            </div>

            <div className="card-cyber p-8">
              <h3 className="font-display text-xl font-bold text-gradient mb-6 flex items-center gap-3">
                <Brain className="w-6 h-6 text-cyan-500" />
                PHILOSOPHY
              </h3>
              <div className="space-y-4">
                {philosophy.map((item, i) => (
                  <motion.div
                    key={i}
                    className="flex items-start gap-3 p-3 bg-cyber-darker/50 rounded-lg border border-cyber-border hover:border-pink-500/30 transition-colors"
                    whileInView={{ opacity: 1, x: 0 }}
                    viewport={{ once: true }}
                    initial={{ opacity: 0, x: -20 }}
                  >
                    <span className="font-mono text-pink-500 mt-1">{'>'}</span>
                    <span className="text-zinc-300 text-sm">{item}</span>
                  </motion.div>
                ))}
              </div>
            </div>
          </div>

          <div className="space-y-6">
            <h3 className="font-display text-xl font-bold text-gradient mb-6 flex items-center gap-3">
              <Award className="w-6 h-6 text-yellow-500" />
              JOURNEY
            </h3>
            
            <div className="relative">
              <div className="absolute left-6 top-0 bottom-0 w-0.5 bg-gradient-to-b from-pink-500 to-cyan-500" />
              
              {timeline.map((item, index) => (
                <motion.div
                  key={item.id}
                  className="relative pl-16 pb-12 last:pb-0"
                  initial={{ opacity: 0, x: -30 }}
                  whileInView={{ opacity: 1, x: 0 }}
                  viewport={{ once: true }}
                  transition={{ delay: index * 0.15 }}
                >
                  <div className="absolute left-0 top-1 w-12 h-12 rounded-full glass border border-pink-500/30 flex items-center justify-center">
                    <span className="font-display font-bold text-pink-500 text-sm">{item.year}</span>
                  </div>
                  
                  <div className="card-cyber p-6">
                    <div className="flex items-center justify-between mb-3">
                      <h4 className="font-bold text-lg text-white">{item.title}</h4>
                      <span className="font-mono text-xs text-cyan-400 bg-cyber-darker/50 px-2 py-1 rounded">{item.company}</span>
                    </div>
                    <p className="text-zinc-400 text-sm mb-4">{item.desc}</p>
                    <div className="flex flex-wrap gap-2">
                      {item.tech?.map((t) => (
                        <span key={t} className="font-mono text-xs px-2 py-1 bg-cyber-darker/50 border border-pink-500/20 rounded text-pink-400 hover:border-pink-500/50 transition-colors">
                          {t}
                        </span>
                      ))}
                    </div>
                  </div>
                </motion.div>
              ))}
            </div>
          </div>
        </motion.div>
      </div>
    </section>
  )
}