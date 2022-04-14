import os
from os import getenv
import constants
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from yt_dlp import YoutubeDL


def get_tokens():
    # TODO: Implement a more secure way to obtain tokens
    client_secret = getenv('SPOTIFY_CLIENT_SECRET')
    client_id = getenv('SPOTIFY_CLIENT_ID')

    if client_secret is None or client_id is None:
        return None
    return client_secret, client_id


def parse_link(link):
    link = link.replace('https://open.spotify.com/', '')
    link_type = link.split('/')[0]
    link_id = link.split('/')[1].split('?')[0]
    return link_type, link_id


def valid_link(link):
    link_type, link_id = parse_link(link)
    if link_id is None:
        return False
    if link_type not in constants.supported_types:
        return False
    return True


def get_tracks(link, link_type):
    client_secret, client_id = get_tokens()
    spy = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=client_id, client_secret=client_secret))

    songs = []
    offset = 0

    if link_type == 'playlist':
        while True:
            tracks = spy.playlist_items(
                playlist_id=link,
                fields='items.track.name,items.track.artists(name, uri)',
                additional_types=['track'], offset=offset
            )

            total_tracks = len(tracks['items'])
            for track in tracks['items']:
                track = track.get('track')
                name = track.get('name')
                artists_arr = track.get('artists')
                artists = ''
                for artist_obj in artists_arr:
                    artists += artist_obj.get('name')+', '
                artists = artists[:-2]

                songs.append({
                    "name": name,
                    "artists": artists,
                })

                offset += 1

            if total_tracks == offset:
                break
    elif link_type == 'album':
        while True:
            tracks = spy.album_tracks(album_id=link, offset=offset)
            total_tracks = tracks.get('total')
            for track in tracks['items']:
                track = track.get('track')
                name = track.get('name')
                artists_arr = track.get('artists')
                artists = ''
                for artist_obj in artists_arr:
                    artists += artist_obj.get('name') + ', '
                artists = artists[:-2]

                songs.append({
                    "name": name,
                    "artists": artists,
                })

                offset += 1
            if total_tracks == offset:
                break
    elif link_type == 'track':
        track = spy.track(track_id=link)
        name = track.get('name')
        artists_arr = track.get('artists')
        artists = ''
        for artist_obj in artists_arr:
            artists += artist_obj.get('name') + ', '
        artists = artists[:-2]

        songs.append({
            "name": name,
            "artists": artists,
        })

    return songs

def download(tracks, audio_format, path):
    for track in tracks:
        query = f"{track.get('artists')} - {track.get('name')} Lyrics"
        for char in constants.replace_chars:
            query.replace(char, '')
        os.chdir(path)

        opts = constants.ytdlp_options
        if audio_format == 'flac':
            opts['postprocessors'].append({
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'flac',
                'preferredquality': '165'
            })
        elif audio_format == 'mp3':
            opts['postprocessors'].append({
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '165'
            })
        elif audio_format == 'wav':
            opts['postprocessors'].append({
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'wav',
                'preferredquality': '165'
            })
        elif audio_format == 'webm':
            # do nothing
            pass

        file = f"{os.getcwd()}/{track.get('artists')} - {track.get('name')}.%(ext)s"
        opts.update({
            'outtmpl': file
        })

        with YoutubeDL(opts) as ydl:
            try:
                ydl.download([query])
            except Exception as e:
                print(e)
                continue
