version = "spotify-dl 1.0.0"

supported_audio_formats = [
    'flac',
    'mp3',
    'wav',
    'webm'
]

supported_types = [
    'album',
    'track',
    'playlist'
]

replace_chars = [
    '#',
    ':',
    '/'
]

ytdlp_options = {
    'format': 'bestaudio',
    'default_search': 'ytsearch',
    'noplaylist': True,
    'postprocessors': []
}
