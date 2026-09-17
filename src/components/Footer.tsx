'use client'

import { motion } from 'framer-motion'
import { Github, Linkedin, Twitter, Mail, Heart, Code, Lock } from 'lucide-react'
import Link from 'next/link'

export function Footer() {
  const currentYear = new Date().getFullYear()

  return (
    <footer className="relative py-12 px-4 sm:px-6 lg:px-8 border-t border-cyber-border">
      <div className="max-w-7xl mx-auto">
        <motion.div
          className="flex flex-col md:flex-row items-center justify-between gap-6"
          initial={{ opacity: 0, y: 20 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
        >
          <div className="flex items-center gap-3">
            <Code className="w-8 h-8 text-pink-500" />
            <span className="font-display font-bold text-xl text-gradient">PORTFOLIO</span>
          </div>

          <div className="flex items-center gap-6">
            <a href="https://github.com" target="_blank" rel="noopener noreferrer" className="text-zinc-400 hover:text-pink-400 transition-colors" aria-label="GitHub">
              <Github className="w-5 h-5" />
            </a>
            <a href="https://linkedin.com" target="_blank" rel="noopener noreferrer" className="text-zinc-400 hover:text-blue-400 transition-colors" aria-label="LinkedIn">
              <Linkedin className="w-5 h-5" />
            </a>
            <a href="https://twitter.com" target="_blank" rel="noopener noreferrer" className="text-zinc-400 hover:text-cyan-400 transition-colors" aria-label="Twitter">
              <Twitter className="w-5 h-5" />
            </a>
            <a href="mailto:dev@example.com" className="text-zinc-400 hover:text-pink-400 transition-colors" aria-label="Email">
              <Mail className="w-5 h-5" />
            </a>
            <Link href="/admin" className="text-zinc-400 hover:text-purple-400 transition-colors flex items-center gap-1" aria-label="Admin">
              <Lock className="w-5 h-5" />
              <span className="font-mono text-xs hidden sm:inline">ADMIN</span>
            </Link>
          </div>

          <div className="flex items-center gap-2 text-zinc-500 text-sm">
            <span className="font-mono">Built with</span>
            <Heart className="w-4 h-4 text-pink-500" />
            <span className="font-mono">Next.js + Tailwind</span>
            <span className="mx-2">|</span>
            <span className="font-mono">Deployed on Vercel</span>
          </div>
        </motion.div>

        <motion.div
          className="mt-8 pt-8 border-t border-cyber-border text-center"
          initial={{ opacity: 0 }}
          whileInView={{ opacity: 1 }}
          viewport={{ once: true }}
          transition={{ delay: 0.3 }}
        >
          <p className="font-mono text-xs text-zinc-500">
            © {currentYear} PORTFOLIO • Crafted in Night City
          </p>
        </motion.div>
      </div>
    </footer>
  )
}