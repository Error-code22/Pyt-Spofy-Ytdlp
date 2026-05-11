# 🚀 Project Progress & Handoff Report: Pyt-Spofy-Ytdlp

## 📅 Status Date: Monday, May 11, 2026
**Current Version:** v1.3 (Stable Release Candidate)
**Project Goal:** A high-speed, portable Spotify-to-MP3 downloader using yt-dlp and Spotify oEmbed metadata.

---

## ✅ Completed Features
1.  **Interactive First-Run Guide**: App now provides instructions and links if the backup folder is empty.
2.  **In-App Refresh Logic**: Added a non-restart way to refresh the playlist list.
3.  **Critical Bug Fixes**: Resolved startup `NameError` and optimized import structure.
4.  **Git Preservation**: Implemented `.gitkeep` strategy for `downloads` and `backup` folders.
5.  **Spotify oEmbed Integration**: Official high-res (640x640) artwork and clean titles fetched directly from Spotify.
6.  **High-Fidelity Audio**: Defaulted to 320kbps MP3 encoding via FFmpeg.
7.  **Stealth Mode**: Randomized sleep intervals (3-7s) to protect user IPs.
8.  **Self-Healing FFmpeg**: Script automatically configures FFmpeg binaries if missing.
9.  **GUI Integration**: `tkinter` folder picker for professional path selection.

---

## 🛠️ Project Structure
- `spotify_downloader.py`: The main logic (Source of truth).
- `requirements.txt`: Dependencies (`yt-dlp`, `mutagen`, `requests`, `tqdm`).
- `README.md`: Professional user documentation (v1.2).
- `.gitignore`: Configured to protect private CSVs and ignore large binaries/build artifacts.
- `build.bat`: Helper script for triggering the `--onedir` build.
- `config.txt`: Stores the user's preferred download directory.

---

## 🚧 Current Obstacle
None. The application is in a stable release state.

---

## ⏭️ Instructions for Next Agent
1.  **Maintenance**: Monitor for any changes in Spotify's public oEmbed response schema.
2.  **Feature Idea**: Consider adding a "Verify Library" mode that checks if existing MP3s have correct metadata without re-downloading.
3.  **Feature Idea**: Add support for direct Spotify Playlist URLs (bypassing CSV requirement) using the same oEmbed logic for metadata.

---
*End of Report*
