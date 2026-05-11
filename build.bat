@echo off
cd /d "%~dp0"
echo [*] Installing dependencies...
pip install -r requirements.txt -q
echo [*] Starting build process (One-Folder mode for instant startup)...
python -m PyInstaller --onedir --noconfirm --console --name "SpotifyToMP3" ^
    --hidden-import="tkinter" ^
    --hidden-import="tqdm" ^
    --hidden-import="yt_dlp.networking" ^
    --hidden-import="yt_dlp.networking.impersonate" ^
    --hidden-import="yt_dlp.networking._urllib" ^
    --hidden-import="yt_dlp.networking._requests" ^
    --hidden-import="yt_dlp.networking._websockets" ^
    --collect-all="yt_dlp" ^
    spotify_downloader.py
echo.
if %ERRORLEVEL% NEQ 0 (
    echo [!] Build FAILED. Check the errors above.
) else (
    echo [+] Build SUCCESSFUL! Your app is in 'dist/SpotifyToMP3'.
    echo [+] To run it, open that folder and double-click 'SpotifyToMP3.exe'.
)
pause
