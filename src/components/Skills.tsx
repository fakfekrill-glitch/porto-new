'use client'

import { motion } from 'framer-motion'
import { 
  Code, Database, Server, Cloud, Smartphone, 
  Layers, GitBranch, TestTube, Figma, Terminal 
} from 'lucide-react'

const skillCategories = [
  {
    title: 'FRONTEND',
    icon: Code,
    color: 'from-pink-500 to-purple-500',
    skills: [
      { name: 'React / Next.js', level: 95 },
      { name: 'TypeScript', level: 90 },
      { name: 'Tailwind CSS', level: 95 },
      { name: 'Framer Motion', level: 85 },
      { name: 'Vue.js / Nuxt', level: 80 },
      { name: 'Astro', level: 75 },
    ],
  },
  {
    title: 'BACKEND',
    icon: Server,
    color: 'from-cyan-500 to-blue-500',
    skills: [
      { name: 'Node.js / Express', level: 90 },
      { name: 'Python / FastAPI', level: 85 },
      { name: 'Go', level: 70 },
      { name: 'PostgreSQL / MongoDB', level: 85 },
      { name: 'GraphQL / REST', level: 90 },
      { name: 'Redis / Prisma', level: 80 },
    ],
  },
  {
    title: 'DEVOPS & CLOUD',
    icon: Cloud,
    color: 'from-purple-500 to-pink-500',
    skills: [
      { name: 'Docker / Kubernetes', level: 80 },
      { name: 'AWS / Vercel', level: 85 },
      { name: 'CI/CD (GitHub Actions)', level: 90 },
      { name: 'Linux / Nginx', level: 75 },
      { name: 'Monitoring (Datadog)', level: 70 },
      { name: 'Terraform', level: 65 },
    ],
  },
  {
    title: 'TOOLS & OTHERS',
    icon: Terminal,
    color: 'from-yellow-500 to-orange-500',
    skills: [
      { name: 'Git / GitHub', level: 95 },
      { name: 'Figma / Design Systems', level: 80 },
      { name: 'Testing (Jest, Cypress)', level: 85 },
      { name: 'Storybook', level: 75 },
      { name: 'Webpack / Vite / Turbopack', level: 80 },
      { name: 'Agile / Scrum', level: 85 },
    ],
  },
]

export function Skills() {
  return (
    <section id="skills" className="relative py-20 md:py-32 px-4 sm:px-6 lg:px-8 bg-gradient-to-b from-cyber-dark via-cyber-darker to-cyber-dark">
      <div className="max-w-7xl mx-auto">
        <motion.div
          className="text-center mb-16"
          initial={{ opacity: 0, y: 30 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          transition={{ duration: 0.6 }}
        >
          <span className="font-mono text-xs text-pink-500 uppercase tracking-widest">// SKILLS.STACK</span>
          <h2 className="section-title mt-4">TECH STACK</h2>
          <p className="section-subtitle mx-auto">
            Technologies I work with daily to build robust applications
          </p>
        </motion.div>

        <motion.div
          className="grid md:grid-cols-2 lg:grid-cols-4 gap-6"
          initial={{ opacity: 0, y: 30 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          transition={{ duration: 0.6, delay: 0.1 }}
        >
          {skillCategories.map((category, catIndex) => (
            <motion.div
              key={category.title}
              className="card-cyber group relative overflow-hidden"
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true }}
              transition={{ delay: catIndex * 0.1 }}
            >
              <div className="absolute inset-0 bg-gradient-to-br from-transparent via-transparent to-transparent group-hover:from-pink-500/5 group-hover:to-purple-500/5 transition-all duration-500" />
              
              <div className="relative z-10">
                <div className="flex items-center gap-3 mb-6">
                  <div className={`w-12 h-12 rounded-xl flex items-center justify-center bg-gradient-to-br ${category.color} text-white`}>
                    <category.icon className="w-6 h-6" />
                  </div>
                  <h3 className="font-display font-bold text-lg text-gradient">{category.title}</h3>
                </div>

                <div className="space-y-4">
                  {category.skills.map((skill, skillIndex) => (
                    <motion.div
                      key={skill.name}
                      className="group/skill"
                      initial={{ opacity: 0, x: -20 }}
                      whileInView={{ opacity: 1, x: 0 }}
                      viewport={{ once: true }}
                      transition={{ delay: catIndex * 0.1 + skillIndex * 0.05 }}
                    >
                      <div className="flex items-center justify-between mb-2">
                        <span className="font-mono text-sm text-zinc-300">{skill.name}</span>
                        <span className="font-mono text-sm text-pink-500">{skill.level}%</span>
                      </div>
                      <div className="relative h-2 bg-cyber-darker rounded-full overflow-hidden">
                        <motion.div
                          className="h-full rounded-full bg-gradient-to-r from-pink-500 to-purple-500 relative overflow-hidden"
                          initial={{ width: 0 }}
                          whileInView={{ width: `${skill.level}%` }}
                          viewport={{ once: true }}
                          transition={{ duration: 1, delay: catIndex * 0.1 + skillIndex * 0.05 + 0.3, ease: 'easeOut' }}
                        >
                          <div className="absolute inset-0 bg-gradient-to-r from-transparent via-white/20 to-transparent animate-pulse" />
                        </motion.div>
                      </div>
                    </motion.div>
                  ))}
                </div>
              </div>
            </motion.div>
          ))}
        </motion.div>

        <motion.div
          className="mt-16 grid md:grid-cols-3 gap-6"
          initial={{ opacity: 0, y: 30 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          transition={{ duration: 0.6, delay: 0.3 }}
        >
          {[
            { icon: Layers, title: 'ARCHITECTURE', desc: 'Scalable frontend architecture, micro-frontends, module federation' },
            { icon: TestTube, title: 'TESTING', desc: 'Unit, integration, E2E testing with Jest, Vitest, Cypress, Playwright' },
            { icon: Figma, title: 'DESIGN SYSTEMS', desc: 'Component libraries, design tokens, Storybook documentation' },
          ].map((item, index) => (
            <motion.div
              key={item.title}
              className="card-cyber p-6 text-center group"
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true }}
              transition={{ delay: index * 0.1 }}
            >
              <div className="w-16 h-16 mx-auto mb-4 rounded-xl glass border border-pink-500/20 flex items-center justify-center group-hover:border-pink-500/50 transition-colors">
                <item.icon className="w-8 h-8 text-pink-500 group-hover:text-cyan-400 transition-colors" />
              </div>
              <h4 className="font-display font-bold text-lg mb-2 text-gradient">{item.title}</h4>
              <p className="text-zinc-400 text-sm">{item.desc}</p>
            </motion.div>
          ))}
        </motion.div>
      </div>
    </section>
  )
}