@echo off
pip install -r requirements.txt
python spotify_downloader.py %1
pause
