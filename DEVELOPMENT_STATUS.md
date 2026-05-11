# 🚀 Project Progress & Handoff Report: Pyt-Spofy-Ytdlp

## 📅 Status Date: Monday, May 11, 2026
**Current Version:** v1.4 (Active Development)
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
10. **Risk Mode Toggle**: `[X]` in menu switches between Safe Mode (3 threads) and Risk Mode (6 threads). Mode is shown in the header and printed per-run.
11. **Search Engine Fix**: Switched from `ytmsearch1:` to `ytsearch1:` (standard YouTube search) for compatibility across all yt-dlp builds — `ytmsearch1:` requires optional network backends not bundled in the exe.
12. **Per-Playlist Summary**: After each playlist finishes, the script prints a summary of successful, skipped, and failed downloads with track names.
13. **Runtime File Gitignore**: `downloaded_songs.txt` and `failed_songs.txt` added to `.gitignore` and untracked — these are machine-local runtime files, not source code.
14. **Build & Run .bat Fixes**: Both `run.bat` and `build.bat` now use `cd /d "%~dp0"` to always execute from their own directory regardless of where they're launched from.
15. **Expanded build.bat**: PyInstaller build now includes all yt-dlp networking hidden imports (`_urllib`, `_requests`, `_websockets`) and `--collect-all=yt_dlp` to prevent missing extractor errors in the compiled exe.

---

## 🛠️ Project Structure
- `spotify_downloader.py`: The main logic (Source of truth).
- `requirements.txt`: Dependencies (`yt-dlp[default]`, `mutagen`, `requests`, `tqdm`).
- `README.md`: Professional user documentation (v1.4).
- `.gitignore`: Configured to protect private CSVs, runtime logs, and large binaries/build artifacts.
- `build.bat`: Helper script for triggering the `--onedir` PyInstaller build with full yt-dlp networking support.
- `run.bat`: Runs the script directly via Python — always `cd`s to its own folder first.
- `config.txt`: Stores the user's preferred download directory.
- `DEVELOPMENT_STATUS.md`: This file.

---

## 🚧 Known Issues / Planned Work

### 1. Age-Restricted YouTube Videos
**Error seen:**
```
ERROR: [youtube] WkZ5e94QnWk: Sign in to confirm your age.
Use --cookies-from-browser or --cookies for authentication.
```
**What's happening:** Some YouTube videos are age-gated. yt-dlp can't download them without browser cookies proving the user is signed in and old enough.

**Planned fix options (pick one):**
- **Option A — Cookie file support**: Add a `--cookies` flag pointing to a `cookies.txt` (Netscape format) exported from the browser. User exports once, tool uses it automatically.
- **Option B — Browser cookie passthrough**: Use `--cookies-from-browser chrome` (or `firefox`, `edge`) so yt-dlp pulls cookies live from the installed browser. No manual export needed but requires the browser to be installed.
- **Option C — Fallback search**: If the first result is age-gated, automatically retry with the next search result (`ytsearch2:`, `ytsearch3:`) until a non-gated video is found.
- **Recommended**: Option B as the default with Option C as a silent fallback — best UX, no manual steps.

### 2. Connection Reset Errors (Mid-Download)
**Error seen:**
```
[download] Got error: ConnectionResetError(10054, 'An existing connection was forcibly closed by the remote host')
```
**What's happening:** YouTube forcibly drops the connection mid-download, usually due to rate limiting or anti-bot detection. yt-dlp retries automatically but it slows things down and can cause partial downloads.

**Planned fix options:**
- Increase `sleep_interval` / `max_sleep_interval` in Risk Mode specifically (currently 3-7s for both modes).
- Add `retries` and `fragment_retries` to `ydl_opts` to make yt-dlp more resilient before giving up.
- In Risk Mode, consider reducing to 4 threads instead of 6 as a middle ground.

---

## ⏭️ Next Steps
1. Implement cookie support for age-restricted videos (see Known Issues #1).
2. Tune retry/sleep settings to reduce connection reset frequency (see Known Issues #2).
3. Consider adding a "Verify Library" mode that checks existing MP3s for correct metadata without re-downloading.
4. Consider adding direct Spotify Playlist URL support (bypassing CSV requirement).

---
*End of Report*
