import os

from args import parsed_args
import constants
import spotify

def main():
    arguments = parsed_args()

    if arguments.version:
        print(constants.version)
        exit(0)
    
    if arguments.link is None:
        print('No playlist/track link provided')
        link = None
        exit(1)
    else:
        link = arguments.link

    if arguments.audio_format is not None:
        if arguments.audio_format not in constants.supported_audio_formats:
            print("Invalid audio format")
            exit(1)
        audio_format = arguments.audio_format
    else:
        audio_format = 'mp3'

    if spotify.get_tokens() is None:
        print('client_id or client_secret not provided. Please read the docs')
        exit(1)

    if not spotify.valid_link(link):
        print('Link is not a valid playlist/track/album')
        exit(1)
    
    if arguments.path is not None:
        path = arguments.path
    else:
        path = os.getcwd()

    link_type, link_id = spotify.parse_link(link)
    tracks = spotify.get_tracks(link, link_type)
    spotify.download(tracks, audio_format, path)


if __name__ == '__main__':
    main()
