# Setting the required environment variables
### 1. Obtain Spotify API token
1. Head over to https://developer.spotify.com/dashboard/applications
2. Click on "CREATE AN APP"
3. Fill out the required details (content does not matter)
4. Click on your newly created app
5. Copy the Client ID
6. Click on "SHOW CLIENT SECRET"
7. Copy your Client Secret
### 2. Set the environment variables
```
export SPOTIFY_CLIENT_ID=YOUR_CLIENT_ID
export SPOTIFY_CLIENT_SECRET=YOUR_CLIENT_SECRET
```
This would need to be run every time you restart your terminal emulator.
### 3. (Optional) Automatically set the environment variables
Add the following lines to your `~/.bashrc` or `~/.zshrc`
```sh
export SPOTIFY_CLIENT_ID=YOUR_CLIENT_ID
export SPOTIFY_CLIENT_SECRET=YOUR_CLIENT_SECRET
```
