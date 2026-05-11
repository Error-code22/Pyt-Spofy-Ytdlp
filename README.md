# 🎵 Spotify to MP3 Downloader v1.2 (Portable)

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

## ✨ New in v1.2

- **YouTube Music Engine**: Uses `ytmsearch` to prioritize official studio/album tracks over music videos (no more cinematic intros or sound effects).
- **Spotify oEmbed Metadata**: Fetches official "Clean Titles" and high-res 640x640 artwork directly from Spotify.
- **High-Fidelity Audio**: Upgraded to 320kbps MP3 encoding for audiophile quality.
- **Stealth Mode**: Randomized "Human-like" pauses to prevent YouTube IP bans on large (10k+) collections.
- **Instant Start**: Switched to a one-folder build for immediate application opening.
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

- **The 3-Worker Limit**: We strictly limit simultaneous downloads to 3. While 10+ might be faster, 3 is the "Goldilocks Zone" that maximizes speed while remaining under the radar of YouTube's anti-bot systems.
- **The "Hybrid" Engine**: We use **Spotify oEmbed** for 100% accurate metadata and **YouTube Music (`ytmsearch`)** for the audio. This ensures you get the official studio masters instead of messy music videos with cinematic intros.
- **Human-Like Pauses**: The tool injects randomized 3-7 second pauses between songs to mimic a real person browsing.

## ⚠️ Risks & Disclaimer

- **IP Bans**: While our "Stealth Mode" significantly reduces risk, downloading thousands of songs in a short window is always a cat-and-mouse game. Use this tool responsibly.
- **Copyright**: This tool is for **educational purposes and personal use only**. Please respect the copyrights of the artists. By using this tool, you agree to take full responsibility for the content you download.
- **Privacy**: We never see your data. Your CSV files stay local on your machine.

## 🙏 Special Thanks

- **yt-dlp team**: This project would literally be impossible without the incredible, tireless work of the [yt-dlp](https://github.com/yt-dlp/yt-dlp) contributors. They are the giants whose shoulders we stand on.
- **Firebase Studio**: For providing the spark that brought this Human/AI partnership together.

---
*Created with ❤️ by a Human/AI Partnership.*
