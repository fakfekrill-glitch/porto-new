'use client'

import { useState } from 'react'
import { motion, AnimatePresence } from 'framer-motion'
import { Award, Eye, Download, Share2, X } from 'lucide-react'
import { useCertificates, Certificate } from '@/lib/store'

export function Certificates() {
  const { certificates } = useCertificates()
  const [selectedCert, setSelectedCert] = useState<Certificate | null>(null)

  const certList = certificates?.length ? certificates : [
    { id: '1', image: '/images/certificates/aws-architect.svg', title: 'AWS Certified Solutions Architect', dateAdded: '2024-01-15' },
    { id: '2', image: '/images/certificates/react-advanced.svg', title: 'React Advanced Patterns', dateAdded: '2023-11-20' },
    { id: '3', image: '/images/certificates/cka.svg', title: 'Kubernetes Administrator (CKA)', dateAdded: '2023-08-10' },
  ]

  const downloadImage = (cert: Certificate) => {
    const link = document.createElement('a')
    link.href = cert.image
    link.download = `${cert.title.replace(/\s+/g, '_')}.jpg`
    link.click()
  }

  return (
    <section id="certificates" className="relative py-20 md:py-32 px-4 sm:px-6 lg:px-8 bg-gradient-to-b from-cyber-darker via-cyber-dark to-cyber-darker">
      <div className="max-w-7xl mx-auto">
        <motion.div
          className="text-center mb-16"
          initial={{ opacity: 0, y: 30 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          transition={{ duration: 0.6 }}
        >
          <span className="font-mono text-xs text-pink-500 uppercase tracking-widest">// CERTIFICATES.GALLERY</span>
          <h2 className="section-title mt-4">CERTIFICATIONS</h2>
          <p className="section-subtitle mx-auto">Click to view full size • Hover for actions</p>
        </motion.div>

        {certificates.length === 0 ? (
          <motion.div
            className="card-cyber p-12 text-center"
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
          >
            <Award className="w-16 h-16 mx-auto mb-4 text-zinc-600" />
            <h3 className="font-display text-xl font-bold mb-2">NO CERTIFICATES YET</h3>
            <p className="text-zinc-500 mb-6">Add certificates via the admin dashboard</p>
            <a href="/admin" className="btn-cyber inline-flex items-center gap-2 mx-auto">
              <span>GO TO ADMIN</span>
            </a>
          </motion.div>
        ) : (
          <motion.div
            className="grid sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-4"
            initial={{ opacity: 0, y: 30 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
            transition={{ duration: 0.6, delay: 0.1 }}
          >
            {certList.map((cert, index) => (
              <motion.article
                key={cert.id}
                className="card-cyber group relative overflow-hidden aspect-[4/3]"
                whileInView={{ opacity: 1, y: 0 }}
                viewport={{ once: true }}
                transition={{ delay: index * 0.08 }}
              >
                <img
                  src={cert.image}
                  alt={cert.title}
                  className="w-full h-full object-cover transition-transform duration-500 group-hover:scale-105"
                  loading="lazy"
                />
                <div className="absolute inset-0 bg-gradient-to-t from-cyber-darker/90 via-transparent to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-300" />
                
                <div className="absolute top-3 right-3 flex gap-1 opacity-0 group-hover:opacity-100 transition-all duration-300 translate-y-2 group-hover:translate-y-0">
                  <button
                    onClick={() => setSelectedCert(cert)}
                    className="w-9 h-9 rounded-lg glass border border-cyan-500/30 flex items-center justify-center text-cyan-400 hover:bg-cyan-500/10 hover:border-cyan-500 transition-all"
                    aria-label="View full size"
                  >
                    <Eye className="w-4 h-4" />
                  </button>
                  <button
                    onClick={() => downloadImage(cert)}
                    className="w-9 h-9 rounded-lg glass border border-pink-500/30 flex items-center justify-center text-pink-400 hover:bg-pink-500/10 hover:border-pink-500 transition-all"
                    aria-label="Download"
                  >
                    <Download className="w-4 h-4" />
                  </button>
                </div>

                <div className="absolute bottom-3 left-3">
                  <Award className="w-5 h-5 text-yellow-400" />
                </div>

                <div className="absolute bottom-3 right-3">
                  <span className="font-mono text-xs bg-cyber-darker/80 px-2 py-1 rounded border border-zinc-600 text-zinc-400">
                    {certificates.length - index}
                  </span>
                </div>
              </motion.article>
            ))}
          </motion.div>
        )}

        <AnimatePresence>
          {selectedCert && (
            <motion.div
              className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/90 backdrop-blur-sm"
              initial={{ opacity: 0 }}
              animate={{ opacity: 1 }}
              exit={{ opacity: 0 }}
              onClick={() => setSelectedCert(null)}
            >
              <motion.div
                className="relative max-w-4xl w-full max-h-[90vh] overflow-hidden"
                initial={{ opacity: 0, scale: 0.95 }}
                animate={{ opacity: 1, scale: 1 }}
                exit={{ opacity: 0, scale: 0.95 }}
                onClick={(e) => e.stopPropagation()}
              >
                <button
                  onClick={() => setSelectedCert(null)}
                  className="absolute top-4 right-4 z-10 w-10 h-10 rounded-full glass border border-zinc-600 flex items-center justify-center text-zinc-400 hover:text-white hover:border-pink-500 transition-all"
                >
                  <X className="w-5 h-5" />
                </button>

                <div className="aspect-[4/3] relative">
                  <img
                    src={selectedCert.image}
                    alt={selectedCert.title}
                    className="w-full h-full object-contain bg-cyber-darker"
                  />
                </div>

                <div className="card-cyber p-4 mt-4 flex items-center justify-between">
                  <h3 className="font-display text-lg font-bold text-gradient">{selectedCert.title}</h3>
                  <div className="flex gap-2">
                    <button
                      onClick={() => downloadImage(selectedCert)}
                      className="w-10 h-10 rounded-lg glass border border-pink-500/30 flex items-center justify-center text-pink-400 hover:bg-pink-500/10 hover:border-pink-500 transition-all"
                    >
                      <Download className="w-4 h-4" />
                    </button>
                    <button
                      className="w-10 h-10 rounded-lg glass border border-cyan-500/30 flex items-center justify-center text-cyan-400 hover:bg-cyan-500/10 hover:border-cyan-500 transition-all"
                    >
                      <Share2 className="w-4 h-4" />
                    </button>
                  </div>
                </div>
              </motion.div>
            </motion.div>
          )}
        </AnimatePresence>

        <p className="text-center text-zinc-500 text-sm mt-8 font-mono">
          Manage certificates in <a href="/admin" className="text-pink-400 hover:text-pink-300 underline">Admin Dashboard</a>
        </p>
      </div>
    </section>
  )
}