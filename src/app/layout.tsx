import type { Metadata, Viewport } from 'next'
import { Inter } from 'next/font/google'
import './globals.css'

const inter = Inter({
  subsets: ['latin'],
  variable: '--font-inter',
  display: 'swap',
})

export const metadata: Metadata = {
  title: 'Portfolio | Cyberpunk Developer',
  description: 'Cyberpunk 2077 inspired developer portfolio showcasing projects, skills, and certifications',
  keywords: ['developer', 'portfolio', 'cyberpunk', 'web developer', 'fullstack', 'react', 'nextjs'],
  authors: [{ name: 'Developer' }],
  openGraph: {
    title: 'Portfolio | Cyberpunk Developer',
    description: 'Cyberpunk 2077 inspired developer portfolio',
    type: 'website',
  },
}

export const viewport: Viewport = {
  themeColor: '#0A0A0F',
  width: 'device-width',
  initialScale: 1,
  maximumScale: 5,
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en" className={`${inter.variable} scroll-smooth`}>
      <head>
        <link rel="preconnect" href="https://fonts.googleapis.com" />
        <link rel="preconnect" href="https://fonts.gstatic.com" crossOrigin="anonymous" />
        <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@300;400;500;600;700&family=Orbitron:wght@400;500;600;700;800;900&family=Space+Grotesk:wght@300;400;500;600;700&display=swap" rel="stylesheet" />
      </head>
      <body className="font-sans antialiased bg-cyber-dark text-zinc-100">
        {children}
      </body>
    </html>
  )
}