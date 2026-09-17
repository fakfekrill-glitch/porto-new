'use client'

import { motion } from 'framer-motion'
import { Github, ExternalLink } from 'lucide-react'
import { useProjects } from '@/lib/store'

export function Projects() {
  const { projects } = useProjects()

  const projectList = projects?.length ? projects : [
    { id: '1', image: '/images/projects/project1.svg', title: 'Neural Network Visualizer', liveUrl: '#', githubUrl: '#', dateAdded: '2024-01-10' },
    { id: '2', image: '/images/projects/project2.svg', title: 'Cyberpunk Dashboard', liveUrl: '#', githubUrl: '#', dateAdded: '2023-12-05' },
    { id: '3', image: '/images/projects/project3.svg', title: 'AI Code Review Bot', liveUrl: '#', githubUrl: '#', dateAdded: '2023-11-20' },
    { id: '4', image: '/images/projects/project4.svg', title: 'Realtime Collaborative Editor', liveUrl: '#', githubUrl: '#', dateAdded: '2023-10-15' },
    { id: '5', image: '/images/projects/project5.svg', title: 'E-Commerce Platform', liveUrl: '#', githubUrl: '#', dateAdded: '2023-09-01' },
    { id: '6', image: '/images/projects/project6.svg', title: 'Task Management App', liveUrl: '#', githubUrl: '#', dateAdded: '2023-08-10' },
  ]

  return (
    <section id="projects" className="relative py-20 md:py-32 px-4 sm:px-6 lg:px-8">
      <div className="max-w-7xl mx-auto">
        <motion.div
          className="text-center mb-16"
          initial={{ opacity: 0, y: 30 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          transition={{ duration: 0.6 }}
        >
          <span className="font-mono text-xs text-pink-500 uppercase tracking-widest">// PROJECTS.PORTFOLIO</span>
          <h2 className="section-title mt-4">SELECTED WORK</h2>
          <p className="section-subtitle mx-auto">Click image for live demo / source code</p>
        </motion.div>

        <motion.div
          className="grid sm:grid-cols-2 lg:grid-cols-3 gap-6"
          initial={{ opacity: 0, y: 30 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          transition={{ duration: 0.6, delay: 0.1 }}
        >
          {projectList.map((project, index) => (
            <motion.article
              key={project.id}
              className="card-cyber group relative overflow-hidden aspect-video"
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true }}
              transition={{ delay: index * 0.1 }}
            >
              <img
                src={project.image}
                alt={project.title}
                className="w-full h-full object-cover transition-transform duration-500 group-hover:scale-105"
                loading="lazy"
              />
              <div className="absolute inset-0 bg-gradient-to-t from-cyber-darker/90 via-transparent to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-300" />
              
              <div className="absolute top-4 right-4 flex gap-2 opacity-0 group-hover:opacity-100 transition-all duration-300 translate-y-2 group-hover:translate-y-0">
                <a
                  href={project.liveUrl}
                  className="w-10 h-10 rounded-lg glass border border-cyan-500/30 flex items-center justify-center text-cyan-400 hover:bg-cyan-500/10 hover:border-cyan-500 transition-all"
                  aria-label="Live demo"
                  target="_blank"
                  rel="noopener noreferrer"
                >
                  <ExternalLink className="w-5 h-5" />
                </a>
                <a
                  href={project.githubUrl}
                  className="w-10 h-10 rounded-lg glass border border-pink-500/30 flex items-center justify-center text-pink-400 hover:bg-pink-500/10 hover:border-pink-500 transition-all"
                  aria-label="Source code"
                  target="_blank"
                  rel="noopener noreferrer"
                >
                  <Github className="w-5 h-5" />
                </a>
              </div>
            </motion.article>
          ))}
        </motion.div>

        <motion.div
          className="text-center mt-12"
          initial={{ opacity: 0, y: 30 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          transition={{ duration: 0.6, delay: 0.3 }}
        >
          <a
            href="https://github.com"
            target="_blank"
            rel="noopener noreferrer"
            className="btn-cyber inline-flex items-center gap-2"
          >
            <span>VIEW ALL PROJECTS</span>
            <Github className="w-5 h-5" />
          </a>
        </motion.div>
      </div>
    </section>
  )
}