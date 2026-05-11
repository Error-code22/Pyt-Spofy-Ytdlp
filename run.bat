@echo off
cd /d "%~dp0"
pip install -r requirements.txt -q
python spotify_downloader.py %1
pause
