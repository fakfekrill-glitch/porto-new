'use client'

import { useState, useEffect } from 'react'
import Link from 'next/link'
import { motion, AnimatePresence } from 'framer-motion'
import { Menu, X, ChevronDown } from 'lucide-react'

const navItems = [
  { href: '#hero', label: 'HOME' },
  { href: '#about', label: 'ABOUT' },
  { href: '#skills', label: 'SKILLS' },
  { href: '#projects', label: 'PROJECTS' },
  { href: '#certificates', label: 'CERTS' },
  { href: '#contact', label: 'CONTACT' },
]

export function Navigation() {
  const [isOpen, setIsOpen] = useState(false)
  const [scrolled, setScrolled] = useState(false)
  const [activeSection, setActiveSection] = useState('hero')

  useEffect(() => {
    const handleScroll = () => {
      setScrolled(window.scrollY > 50)
      
      const sections = ['hero', 'about', 'skills', 'projects', 'certificates', 'contact']
      const scrollPos = window.scrollY + 100
      
      for (const section of sections) {
        const element = document.getElementById(section)
        if (element) {
          const { offsetTop, offsetHeight } = element
          if (scrollPos >= offsetTop && scrollPos < offsetTop + offsetHeight) {
            setActiveSection(section)
            break
          }
        }
      }
    }

    window.addEventListener('scroll', handleScroll)
    return () => window.removeEventListener('scroll', handleScroll)
  }, [])

  const scrollToSection = (href: string) => {
    const element = document.getElementById(href.replace('#', ''))
    if (element) {
      element.scrollIntoView({ behavior: 'smooth' })
    }
    setIsOpen(false)
  }

  return (
    <>
      <nav
        className={`fixed top-0 left-0 right-0 z-50 transition-all duration-300 ${
          scrolled ? 'bg-cyber-darker/95 backdrop-blur-md border-b border-cyber-border' : 'bg-transparent'
        }`}
      >
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex items-center justify-between h-16 md:h-20">
            <Link
              href="#hero"
              className="font-display font-bold text-xl md:text-2xl text-transparent bg-clip-text bg-gradient-to-r from-pink-500 via-purple-500 to-cyan-500 tracking-wider"
              onClick={(e) => { e.preventDefault(); scrollToSection('#hero'); }}
            >
              PORTFOLIO
            </Link>

            <div className="hidden md:flex items-center space-x-1 md:space-x-4">
              {navItems.map((item) => (
                <motion.button
                  key={item.href}
                  onClick={(e) => { e.preventDefault(); scrollToSection(item.href); }}
                  className={`relative px-3 py-2 font-mono text-xs uppercase tracking-wider transition-all duration-300 ${
                    activeSection === item.href.replace('#', '') 
                      ? 'text-pink-500' 
                      : 'text-zinc-400 hover:text-cyan-400'
                  }`}
                  whileHover={{ scale: 1.05 }}
                  whileTap={{ scale: 0.95 }}
                >
                  {item.label}
                  <motion.div
                    className="absolute bottom-0 left-0 h-0.5 bg-gradient-to-r from-pink-500 to-cyan-500"
                    initial={{ width: 0 }}
                    animate={{ width: activeSection === item.href.replace('#', '') ? '100%' : 0 }}
                    transition={{ duration: 0.3 }}
                  />
                </motion.button>
              ))}
            </div>

            <button
              className="md:hidden p-2 text-zinc-400 hover:text-cyan-400 transition-colors"
              onClick={() => setIsOpen(!isOpen)}
              aria-label="Toggle menu"
            >
              {isOpen ? <X className="w-6 h-6" /> : <Menu className="w-6 h-6" />}
            </button>
          </div>
        </div>

        <AnimatePresence>
          {isOpen && (
            <motion.div
              className="md:hidden bg-cyber-darker/95 backdrop-blur-md border-t border-cyber-border px-4 pb-6"
              initial={{ opacity: 0, height: 0 }}
              animate={{ opacity: 1, height: 'auto' }}
              exit={{ opacity: 0, height: 0 }}
              transition={{ duration: 0.3 }}
            >
              <div className="flex flex-col space-y-2 pt-4">
                {navItems.map((item) => (
                  <motion.button
                    key={item.href}
                    onClick={(e) => { e.preventDefault(); scrollToSection(item.href); }}
                    className={`text-left px-4 py-3 font-mono text-sm uppercase tracking-wider transition-all duration-300 rounded-lg ${
                      activeSection === item.href.replace('#', '')
                        ? 'bg-pink-500/10 text-pink-500 border border-pink-500/30'
                        : 'text-zinc-400 hover:text-cyan-400 hover:bg-cyber-card'
                    }`}
                    whileHover={{ x: 4 }}
                    whileTap={{ scale: 0.98 }}
                  >
                    <span className="flex items-center justify-between">
                      {item.label}
                      <ChevronDown className="w-4 h-4" />
                    </span>
                  </motion.button>
                ))}
              </div>
            </motion.div>
          )}
        </AnimatePresence>
      </nav>

      <div className="h-16 md:h-20" />
    </>
  )
}