import { Navigation } from '@/components/Navigation'
import { Hero } from '@/components/Hero'
import { About } from '@/components/About'
import { Skills } from '@/components/Skills'
import { Projects } from '@/components/Projects'
import { Certificates } from '@/components/Certificates'
import { Contact } from '@/components/Contact'
import { Footer } from '@/components/Footer'
import { CyberBackground } from '@/components/CyberBackground'

export default function Home() {
  return (
    <>
      <CyberBackground />
      <Navigation />
      <main className="relative z-10">
        <Hero />
        <About />
        <Skills />
        <Projects />
        <Certificates />
        <Contact />
      </main>
      <Footer />
    </>
  )
}