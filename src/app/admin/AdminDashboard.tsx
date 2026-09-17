'use client'

import { useEffect, useRef } from 'react'

export default function AdminDashboard() {
  const containerRef = useRef<HTMLDivElement>(null)

  useEffect(() => {
    if (!containerRef.current) return

    // Load the admin.html content
    fetch('/admin.html')
      .then(res => res.text())
      .then(html => {
        const parser = new DOMParser()
        const doc = parser.parseFromString(html, 'text/html')
        
        // Get the body content (skip head/scripts)
        const body = doc.querySelector('body')
        if (body && containerRef.current) {
          containerRef.current.innerHTML = body.innerHTML
          
          // Execute scripts from admin.html
          const scripts = containerRef.current.querySelectorAll('script')
          scripts.forEach(oldScript => {
            const newScript = document.createElement('script')
            if (oldScript.src) {
              newScript.src = oldScript.src
            } else {
              newScript.textContent = oldScript.textContent
            }
            oldScript.replaceWith(newScript)
          })
        }
      })
      .catch(err => console.error('Failed to load admin dashboard:', err))

    return () => {
      if (containerRef.current) {
        containerRef.current.innerHTML = ''
      }
    }
  }, [])

  return <div ref={containerRef} className="min-h-screen" />
}