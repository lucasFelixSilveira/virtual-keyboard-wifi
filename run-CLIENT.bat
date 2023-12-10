@echo off
set /p link=Enter the link:

if "%link%"=="" (
  echo No link provided. Exiting the script.
  exit /b 1
)

cd client
node start.js %link%
cd ..
cd server
gcc main.c -o keyboard.exe
keyboard.exe