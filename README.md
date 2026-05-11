# 🎵 Spotify to MP3 Downloader v1.3 (Portable)

> **"The ultimate digital prepper tool for your music collection."**
> High-speed downloads, official Spotify metadata, and a stealthy engine that keeps you under the radar. 

A professional, high-speed tool to download your Spotify playlists as high-quality MP3s with official metadata and high-resolution cover art. **No Python installation required.**

## 📦 What's in the Box?

- `SpotifyToMP3/`: The application folder.
- `SpotifyToMP3.exe`: The main application (found inside the folder).
- `ffmpeg.exe` & `ffprobe.exe`: The engines that handle high-quality audio conversion.
- `Spotify-Exel-Files-Backup/`: Place your Spotify exports (Excel/CSV) here.
- `config.txt`: Remembers your custom download directory.

## 🚀 Quick Start

1.  **Get Your Playlists**:
    - Go to [Exportify.app](https://exportify.app/) (or the [GitHub mirror](https://watsonbox.github.io/exportify/)).
    - Log in with your Spotify account.
    - Export your playlists or liked songs. **Choose the CSV format** (often referred to as the Excel format in Exportify).
2.  **Add Your Playlists**: Copy those downloaded files into the `Spotify-Exel-Files-Backup` folder in the root of this project.
3.  **Download & Extract**: Extract the release ZIP of this tool to a folder.
4.  **Run**: Open the `SpotifyToMP3` folder and double-click `SpotifyToMP3.exe`.
5.  **Customize**: Use the **[D]** option to select your download folder.
6.  **Select**: Choose a playlist or select **[A]** to download everything!

## ✨ New in v1.4

- **Risk Mode (`[X]`)**: Toggle between Safe Mode (3 threads) and Risk Mode (6 threads) directly from the menu before starting any download. The current mode is always shown in the header so you know exactly what you're running.
- **Per-Run Mode Label**: Each download session prints the active thread count and mode so there's no guesswork mid-run.

## ✨ Previous v1.3 Features

- **Interactive First-Run Guide**: If no playlists are found, the app now shows a step-by-step guide with direct links to Exportify.
- **In-App Refresh**: Added a `[R] Refresh` option to the menu so you can add new CSV files without restarting the app.
- **Resilient Startup**: Fixed a critical `NameError` crash and optimized imports for faster, more stable launching.
- **Repo Integrity**: Added `.gitkeep` files to ensure the `downloads` and `backup` folders are preserved when cloning the repo.

## ✨ Previous v1.2 Features

- **YouTube Music Engine**: Uses `ytmsearch` to prioritize official studio/album tracks over music videos (no more cinematic intros or sound effects).
- **Spotify oEmbed Metadata**: Fetches official "Clean Titles" and high-res 640x640 artwork directly from Spotify.
- **High-Fidelity Audio**: Upgraded to 320kbps MP3 encoding for audiophile quality.
- **Stealth Mode**: Randomized "Human-like" pauses to prevent YouTube IP bans on large (10k+) collections.
- **Persistence**: Automatically embeds the Spotify Track URI in the MP3 comments for future-proof offline storage.
- **Failure Logging**: Generates a `failed_songs.txt` report if any tracks are missing or blocked.

## ✨ Previous v1.1 Features

- **Parallel Downloads**: Downloads 3 songs simultaneously for maximum speed.
- **Atomic File Handling**: Songs are only finalized after 100% success.
- **GUI Folder Picker**: Select your output folder with a standard Windows dialog.
- **Smart Organization**: Automatically creates subfolders for each playlist.

## 🤝 The Collaboration

This project is a unique collaboration between a **Human Visionary** and **Gemini CLI (AI Agent)**. Every feature—from the atomic download logic to the Spotify oEmbed integration—was co-engineered to create the ultimate "digital prepper" music tool for 2026.

## 🛡️ Safety & "Stealth" Strategy

To handle massive libraries (10k+ songs) without getting your IP banned, we implemented a **Stealth First** architecture:

- **The 3-Worker Limit (Safe Mode)**: We default to 3 simultaneous downloads — the "Goldilocks Zone" that maximizes speed while staying under the radar of YouTube's anti-bot systems.
- **Risk Mode (6 Workers)**: Available via `[X]` in the menu. Doubles throughput but significantly increases the chance of triggering rate limits, temporary IP blocks, or account flags on both YouTube and Spotify. **Use at your own risk.**
- **The "Hybrid" Engine**: We use **Spotify oEmbed** for 100% accurate metadata and **YouTube Music (`ytmsearch`)** for the audio. This ensures you get the official studio masters instead of messy music videos with cinematic intros.
- **Human-Like Pauses**: The tool injects randomized 3-7 second pauses between songs to mimic a real person browsing.

## ⚠️ Risks, Liability & Disclaimer

**By using this tool — especially Risk Mode — you accept full and sole responsibility for any and all consequences. The developer(s) of this project accept zero liability.**

### Risk Mode — What Can Actually Happen

Running 6 simultaneous download threads is aggressive. Here's what you're signing up for:

| Risk | Likelihood in Risk Mode | Notes |
|---|---|---|
| Temporary YouTube IP ban | High on large playlists | Usually lifts in 24–48 hours |
| YouTube account flag/strike | Medium | Especially if logged in via cookies |
| Spotify account flag | Low–Medium | Rapid oEmbed requests can trigger rate limits |
| Spotify account suspension | Low | Possible if Spotify detects automated scraping patterns |
| Permanent IP block from YouTube | Low | More likely on repeated aggressive sessions |

### The Developer's Position

- **I did not make you click `[X]`.**
- If your YouTube account gets flagged, your Spotify account gets suspended, or your IP gets blocked — that is a consequence of a choice you made.
- This tool does not store, transmit, or sell any of your data. Your CSV files and downloads stay entirely on your machine.
- This tool is provided **as-is**, with no warranty, no guarantee of uptime, and no obligation to fix anything.

### General Disclaimer

- **Copyright**: This tool is for **personal and educational use only**. You are responsible for ensuring your use complies with the laws in your jurisdiction and the Terms of Service of Spotify and YouTube. Downloading copyrighted content without authorization may be illegal where you live.
- **Privacy**: We never see your data. Everything stays local.
- **No Endorsement**: This project is not affiliated with, endorsed by, or connected to Spotify, YouTube, or Google in any way.

## 🙏 Special Thanks

- **yt-dlp team**: This project would literally be impossible without the incredible, tireless work of the [yt-dlp](https://github.com/yt-dlp/yt-dlp) contributors. They are the giants whose shoulders we stand on.
- **Firebase Studio**: For providing the spark that brought this Human/AI partnership together.

---
*Created with ❤️ by a Human/AI Partnership.*
