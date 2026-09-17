'use client'

import { useState, useEffect } from 'react'
import { motion } from 'framer-motion'
import { Music, Gamepad2, MessageCircle, Heart, Loader2 } from 'lucide-react'

interface LanyardData {
  discord_user: {
    username: string
    discriminator: string
    avatar: string
    public_flags: number
  }
  discord_status: 'online' | 'idle' | 'dnd' | 'offline'
  activities: Array<{
    type: number
    name: string
    state?: string
    details?: string
    assets?: {
      large_image?: string
      large_text?: string
      small_image?: string
      small_text?: string
    }
    timestamps?: {
      start?: number
      end?: number
    }
    application_id?: string
    url?: string
  }>
  listening_to_spotify?: {
    song: string
    artist: string
    album_art_url: string
    track_id: string
  }
  spotify?: {
    track_id: string
    timestamps: {
      start: number
      end: number
    }
    song: string
    artist: string
    album: string
    album_art_url: string
  }
  active_on_discord_web: boolean
  active_on_discord_desktop: boolean
  active_on_discord_mobile: boolean
}

export function DiscordActivity() {
  const [data, setData] = useState<LanyardData | null>(null)
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState<string | null>(null)

  useEffect(() => {
    const fetchData = async () => {
      try {
        const res = await fetch('https://api.lanyard.rest/v1/users/582206666431266816')
        const json = await res.json()
        if (json.success) {
          setData(json.data)
        } else {
          setError('Failed to fetch Discord data')
        }
      } catch {
        setError('Error fetching Discord activity')
      } finally {
        setLoading(false)
      }
    }

    fetchData()
    const interval = setInterval(fetchData, 30000)
    return () => clearInterval(interval)
  }, [])

  const getStatusColor = (status: string) => {
    switch (status) {
      case 'online': return 'text-green-400'
      case 'idle': return 'text-yellow-400'
      case 'dnd': return 'text-red-400'
      default: return 'text-zinc-500'
    }
  }

  const getStatusLabel = (status: string) => {
    switch (status) {
      case 'online': return 'ONLINE'
      case 'idle': return 'IDLE'
      case 'dnd': return 'DO NOT DISTURB'
      default: return 'OFFLINE'
    }
  }

  const getActivityIcon = (type: number) => {
    switch (type) {
      case 0: return <Gamepad2 className="w-4 h-4" />
      case 1: return <MessageCircle className="w-4 h-4" />
      case 2: return <Music className="w-4 h-4" />
      case 3: return <Gamepad2 className="w-4 h-4" />
      case 4: return <Gamepad2 className="w-4 h-4" />
      case 5: return <MessageCircle className="w-4 h-4" />
      default: return <MessageCircle className="w-4 h-4" />
    }
  }

  if (loading) {
    return (
      <motion.div className="card-cyber p-6" initial={{ opacity: 0, y: 20 }} animate={{ opacity: 1, y: 0 }}>
        <div className="flex items-center gap-4">
          <Loader2 className="w-8 h-8 text-pink-500 animate-spin" />
          <div>
            <p className="font-mono text-xs text-pink-400 uppercase tracking-wider">DISCORD PRESENCE</p>
            <p className="text-zinc-400">Loading activity...</p>
          </div>
        </div>
      </motion.div>
    )
  }

  if (error || !data) {
    return (
      <motion.div className="card-cyber p-6" initial={{ opacity: 0, y: 20 }} animate={{ opacity: 1, y: 0 }}>
        <div className="flex items-center gap-4 text-red-400">
          <MessageCircle className="w-8 h-8" />
          <div>
            <p className="font-mono text-xs text-pink-400 uppercase tracking-wider">DISCORD PRESENCE</p>
            <p className="text-zinc-400">Unable to load activity</p>
          </div>
        </div>
      </motion.div>
    )
  }

  const { discord_user, discord_status, activities, listening_to_spotify, spotify } = data
  const currentActivity = activities[0]
  const spotifyData = listening_to_spotify || spotify

  return (
    <motion.div className="card-cyber p-6 relative overflow-hidden" initial={{ opacity: 0, y: 20 }} animate={{ opacity: 1, y: 0 }} transition={{ duration: 0.5 }}>
      <div className="absolute inset-0 bg-gradient-to-br from-pink-500/5 via-transparent to-cyan-500/5" />
      <div className="relative z-10">
        <div className="flex items-center justify-between mb-4">
          <div className="flex items-center gap-3">
            <div className="relative">
              {discord_user.avatar && (
                <img
                  src={`https://cdn.discordapp.com/avatars/582206666431266816/${discord_user.avatar}.png?size=64`}
                  alt={discord_user.username}
                  className="w-12 h-12 rounded-full border-2 border-pink-500/50"
                />
              )}
              <div className={`absolute bottom-0 right-0 w-3 h-3 rounded-full border-2 border-cyber-darker ${getStatusColor(discord_status)}`} />
            </div>
            <div>
              <p className="font-display text-lg font-bold text-white">
                {discord_user.username}#{discord_user.discriminator}
              </p>
              <div className="flex items-center gap-2">
                <span className={`font-mono text-xs uppercase tracking-wider ${getStatusColor(discord_status)}`}>
                  {getStatusLabel(discord_status)}
                </span>
              </div>
            </div>
          </div>
          <span className="font-mono text-xs text-pink-400 uppercase tracking-wider">DISCORD PRESENCE</span>
        </div>

        {spotifyData && (
          <div className="mb-4 p-4 bg-cyber-darker/50 rounded-lg border border-cyber-border">
            <div className="flex items-center gap-4">
              <div className="relative">
                <img
                  src={spotifyData.album_art_url}
                  alt={spotifyData.song}
                  className="w-16 h-16 rounded-lg object-cover"
                />
              </div>
              <div className="flex-1 min-w-0">
                <p className="font-mono text-xs text-pink-400 uppercase tracking-wider">LISTENING ON SPOTIFY</p>
                <p className="font-bold text-white truncate">{spotifyData.song}</p>
                <p className="text-zinc-400 text-sm truncate">{spotifyData.artist}</p>
                <p className="text-zinc-500 text-xs truncate">{(spotifyData as Record<string, unknown>).album as string || ''}</p>
              </div>
              <Music className="w-6 h-6 text-green-400" />
            </div>
          </div>
        )}

        {currentActivity && currentActivity.type !== 2 && (
          <div className="p-4 bg-cyber-darker/50 rounded-lg border border-cyber-border">
            <div className="flex items-start gap-4">
              <div className="w-10 h-10 rounded-lg bg-pink-500/20 flex items-center justify-center flex-shrink-0">
                {getActivityIcon(currentActivity.type)}
              </div>
              <div className="flex-1 min-w-0">
                <p className="font-mono text-xs text-pink-400 uppercase tracking-wider">
                  {currentActivity.type === 0 ? 'PLAYING' : currentActivity.type === 1 ? 'STREAMING' : 'ACTIVITY'}
                </p>
                <p className="font-bold text-white truncate">{currentActivity.name}</p>
                {currentActivity.details && <p className="text-zinc-300 text-sm truncate">{currentActivity.details}</p>}
                {currentActivity.state && <p className="text-zinc-400 text-sm truncate">{currentActivity.state}</p>}
              </div>
            </div>
            {currentActivity.assets?.large_image && (
              <img
                src={`https://cdn.discordapp.com/app-assets/${currentActivity.application_id}/${currentActivity.assets.large_image}.png`}
                alt={currentActivity.assets.large_text || ''}
                className="mt-3 w-16 h-16 rounded-lg object-cover opacity-50"
              />
            )}
          </div>
        )}

        {!spotifyData && !currentActivity && (
          <div className="text-center py-4 text-zinc-500">
            <MessageCircle className="w-8 h-8 mx-auto mb-2 opacity-30" />
            <p className="font-mono text-xs">No active activity</p>
          </div>
        )}

        <div className="mt-4 pt-4 border-t border-cyber-border flex items-center justify-between text-xs text-zinc-500">
          <span>Auto-refreshes every 30s</span>
          <span className="flex items-center gap-1">
            {data.active_on_discord_desktop && <span className="text-green-400">●</span>}
            {data.active_on_discord_mobile && <span className="text-yellow-400">●</span>}
            {data.active_on_discord_web && <span className="text-cyan-400">●</span>}
          </span>
        </div>
      </div>
    </motion.div>
  )
}