@echo off
echo [*] Starting build process (One-Folder mode for instant startup)...
python -m PyInstaller --onedir --noconfirm --console --name "SpotifyToMP3" --hidden-import="tkinter" --hidden-import="tqdm" spotify_downloader.py
echo.
if %ERRORLEVEL% NEQ 0 (
    echo [!] Build FAILED. Check the errors above.
) else (
    echo [+] Build SUCCESSFUL! Your app is in 'dist/SpotifyToMP3'.
    echo [+] To run it, open that folder and double-click 'SpotifyToMP3.exe'.
)
pause
