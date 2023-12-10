#!/bin/bash

echo "Enter the link:"
read link

if [ -z "$link" ]; then
  echo "No link provided. Exiting the script."
  exit 1
fi

cd client
node start.js $link
cd ..

cd server
gcc main.c =o keyboard
mv keyboard ~
cp start.js ~
cp send.js ~
cp enter.js ~
cd ~
chmod +x keyboard
./keyboard