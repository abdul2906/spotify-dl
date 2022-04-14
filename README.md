# spotify-dl
A simple script to download music found on Spotify from YouTube.

## Installation
#### Automatic
```
$ ./install.sh
``` 
Note: you will be prompted for a root password
#### Manual
```
$ pip3 install -r requirements.txt
# mkdir -p /opt/spotify-dl
# cp -rf src/* /opt/spotify-dl/
$ chmod +x spotify-dl
$ cp -f spotify-dl /bin/
```
#### No installation
```
./spotify-dl
```
## Usage
#### IMPORTANT: Read [how to set the requied environment variables](docs/setting_environment_variables.md)
```
usage: spotify-dl url [-f FORMAT] [-o PATH] [-v]

Fetches songs from Spotify and downloads them from YouTube.

positional-arguments:
  url                   Url to Spotify playlist/track/album

optional-arguments:
  -f FORMAT             Specify the desired format (mp3/wav/flac/webm)
  -o PATH               Specify the path to download to
  -v                    Show current version of spotify-dl
```
