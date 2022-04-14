#!/bin/sh
printf "Installing dependencies\n"
pip3 install -r requirements.txt
printf "\nRoot permissions required to copy files\n"
su -c 'mkdir -p /opt/spotify-dl && cp -rf src/* /opt/spotify-dl/ && chmod +x spotify-dl && cp -f spotify-dl /bin/'
printf "Installation complete.\n"
