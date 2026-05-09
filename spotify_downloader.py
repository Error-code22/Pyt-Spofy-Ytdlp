# --- Configuration ---
MAX_THREADS = 3  # Stable for both speed and avoiding bans
CONFIG_FILE = "config.txt"
FAILED_LOG = "failed_songs.txt"
DOWNLOAD_ARCHIVE = "downloaded_songs.txt"
FFMPEG_URL = "https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-essentials.zip"

# Global session for connection pooling (faster/more reliable for 10k+ requests)
session = requests.Session()

def get_base_path():
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return base_path

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def sanitize_filename(filename):
    """Sanitizes a string to be a valid filename."""
    return re.sub(r'[\\/*?:"<>|]', "", filename).strip()

def download_ffmpeg():
    """Downloads and extracts ffmpeg/ffprobe from gyan.dev."""
    clear_screen()
    print("====================================================")
    print("          FFMPEG AUTO-DOWNLOADER                    ")
    print("====================================================")
    print("\n[!] FFmpeg is required but was not found.")
    print("[?] Would you like to automatically download it? (~90MB)")
    choice = input("\nDownload now? (y/n): ").strip().lower()
    
    if choice != 'y':
        return False

    try:
        print("\n[*] Connecting to gyan.dev...")
        response = requests.get(FFMPEG_URL, stream=True)
        total_size = int(response.headers.get('content-length', 0))
        
        # Use tqdm for a nice progress bar
        block_size = 1024
        t = tqdm(total=total_size, unit='iB', unit_scale=True, desc="Downloading FFmpeg")
        
        zip_data = io.BytesIO()
        for data in response.iter_content(block_size):
            t.update(len(data))
            zip_data.write(data)
        t.close()

        if total_size != 0 and t.n != total_size:
            print("\n[!] Error: Download incomplete.")
            return False

        print("\n[*] Extracting binaries...")
        with zipfile.ZipFile(zip_data) as zip_ref:
            # Find ffmpeg.exe and ffprobe.exe in the zip
            for member in zip_ref.namelist():
                if member.endswith(('ffmpeg.exe', 'ffprobe.exe')):
                    filename = os.path.basename(member)
                    with zip_ref.open(member) as source, open(filename, "wb") as target:
                        target.write(source.read())
        
        print("[+] FFmpeg setup complete!")
        time.sleep(2)
        return True

    except Exception as e:
        print(f"\n[!] Error downloading FFmpeg: {e}")
        input("\nPress Enter to try again or exit...")
        return False

def check_ffmpeg():
    """Checks if ffmpeg is installed and accessible."""
    # 1. Check if in PATH
    try:
        subprocess.run(['ffmpeg', '-version'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return True
    except FileNotFoundError:
        pass
    
    # 2. Check in current directory
    exe_dir = os.path.dirname(sys.executable if getattr(sys, 'frozen', False) else __file__)
    local_ffmpeg = os.path.join(exe_dir, 'ffmpeg.exe')
    
    if os.path.exists(local_ffmpeg):
        os.environ["PATH"] += os.pathsep + exe_dir
        return True
    
    # 3. Try to auto-download
    return download_ffmpeg()

def get_oembed_data(track_uri):
    """Fetches official metadata from Spotify oEmbed with smart retries."""
    if not track_uri:
        return None
    
    track_id = track_uri.split(':')[-1]
    oembed_url = f"https://open.spotify.com/oembed?url=spotify:track:{track_id}"
    
    for _ in range(3): # 3 retry attempts
        try:
            response = session.get(oembed_url, timeout=10)
            if response.status_code == 200:
                return response.json()
            elif response.status_code == 429:
                # Rate limited - wait for the amount Spotify tells us
                wait_time = int(response.headers.get("Retry-After", 5))
                print(f"\n[!] Rate limited by Spotify. Waiting {wait_time}s...")
                time.sleep(wait_time)
            else:
                break
        except Exception:
            time.sleep(1)
    return None

def download_image(url, output_path):
    """Downloads an image with retries using the global session."""
    for i in range(3):
        try:
            response = session.get(url, stream=True, timeout=15)
            if response.status_code == 200:
                with open(output_path, 'wb') as f:
                    for chunk in response.iter_content(1024):
                        f.write(chunk)
                return True
        except Exception:
            time.sleep(1)
    return False

def embed_metadata(file_path, metadata, image_path=None):
    """Embeds ID3 metadata and cover art into an MP3 file."""
    try:
        if not os.path.exists(file_path):
            return False, "File not found"

        audio = MP3(file_path, ID3=ID3)
        try:
            audio.add_tags()
        except error:
            pass

        audio.tags.add(TIT2(encoding=3, text=metadata.get('title', '')))
        audio.tags.add(TPE1(encoding=3, text=metadata.get('artist', '')))
        audio.tags.add(TALB(encoding=3, text=metadata.get('album', '')))
        audio.tags.add(TYER(encoding=3, text=metadata.get('year', '')))
        audio.tags.add(TRCK(encoding=3, text=metadata.get('track_num', '')))
        
        # Add Spotify URI in the comment for "Offline Persistence"
        if metadata.get('uri'):
            from mutagen.id3 import COMM
            audio.tags.add(COMM(encoding=3, lang='eng', desc='Spotify URI', text=metadata.get('uri')))

        image_added = False
        if image_path and os.path.exists(image_path):
            with open(image_path, 'rb') as f:
                audio.tags.add(
                    APIC(
                        encoding=3,
                        mime='image/jpeg',
                        type=3,
                        desc=u'Cover',
                        data=f.read()
                    )
                )
            image_added = True
        
        audio.save()
        return True, "Success" if image_added else "Metadata added (No Image)"
    except Exception as e:
        return False, str(e)

def download_track(row, output_dir):
    """Downloads and tags a single track atomically."""
    csv_track_name = row.get('Track Name', 'Unknown Track')
    artists = row.get('Artist Name(s)', 'Unknown Artist')
    album = row.get('Album Name', '')
    csv_image_url = row.get('Album Image URL', '')
    track_uri = row.get('Track URI', '')
    release_date = row.get('Album Release Date', '')
    track_num = row.get('Track Number', '1')
    year = release_date.split('-')[0] if release_date else ""

    # Check for existing file BEFORE making any API calls to avoid rate limits
    safe_filename = sanitize_filename(f"{artists} - {csv_track_name}")
    final_mp3 = os.path.join(output_dir, f"{safe_filename}.mp3")
    temp_mp3 = os.path.join(output_dir, f"{safe_filename}.tmp.mp3")
    cover_path = os.path.join(output_dir, f"{safe_filename}_cover.jpg")

    if os.path.exists(final_mp3):
        print(f"  [-] Skipping: {csv_track_name}")
        return

    # Now that we know we need to download, get high-res metadata
    track_name = csv_track_name
    image_url = csv_image_url
    
    oembed = get_oembed_data(track_uri)
    if oembed:
        track_name = oembed.get('title', csv_track_name)
        image_url = oembed.get('thumbnail_url', csv_image_url)

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(output_dir, f"{safe_filename}.tmp.%(ext)s"),
        'download_archive': DOWNLOAD_ARCHIVE,  # Prevent re-downloading bits
        'sleep_interval': 3,                   # Stealth: wait between songs
        'max_sleep_interval': 7,               # Stealth: randomized wait
        'ignoreerrors': True,                  # Keep going even if one song fails
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '320',         # High fidelity 320kbps
        }],
        'quiet': True,
        'no_warnings': True,
    }

    try:
        search_query = f"{track_name} {artists}"
        with YoutubeDL(ydl_opts) as ydl:
            # ytmsearch ensures we get official audio/album versions rather than music videos
            ydl.download([f"ytmsearch1:{search_query}"])
        
        img_status = "❌"
        if image_url:
            if download_image(image_url, cover_path):
                img_status = "✅"

        meta_success, meta_msg = embed_metadata(temp_mp3, {
            'title': track_name,
            'artist': artists,
            'album': album,
            'year': year,
            'track_num': track_num,
            'uri': track_uri
        }, cover_path if os.path.exists(cover_path) else None)

        if os.path.exists(cover_path):
            os.remove(cover_path)

        if meta_success and os.path.exists(temp_mp3):
            os.rename(temp_mp3, final_mp3)
            print(f"  [+] Finished: {track_name} | Art: {img_status}")
        else:
            if os.path.exists(temp_mp3):
                os.remove(temp_mp3)
                with open(FAILED_LOG, "a", encoding="utf-8") as f:
                    f.write(f"{artists} - {track_name} | Error: {meta_msg}\n")

    except Exception as e:
        if os.path.exists(temp_mp3): os.remove(temp_mp3)
        with open(FAILED_LOG, "a", encoding="utf-8") as f:
            f.write(f"{artists} - {track_name} | Error: {str(e)}\n")

def process_csv(csv_path, base_output_dir):
    """Processes a single CSV file."""
    playlist_name = sanitize_filename(os.path.splitext(os.path.basename(csv_path))[0])
    playlist_dir = os.path.join(base_output_dir, playlist_name)
    
    if not os.path.exists(playlist_dir):
        os.makedirs(playlist_dir)

    print(f"\n>>> Playlist: {playlist_name}")
    print(f">>> Folder: {playlist_dir}")

    try:
        with open(csv_path, mode='r', encoding='utf-8') as f:
            reader = list(csv.DictReader(f))
            with ThreadPoolExecutor(max_workers=MAX_THREADS) as executor:
                for row in reader:
                    executor.submit(download_track, row, playlist_dir)
    except Exception as e:
        print(f"Error: {e}")

def load_config():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, 'r') as f:
            return f.read().strip()
    return "downloads"

def save_config(path):
    with open(CONFIG_FILE, 'w') as f:
        f.write(path)

def show_menu():
    backup_dir = "Spotify-Exel-Files-Backup"
    current_out = load_config()

    if not os.path.exists(backup_dir):
        print(f"Error: Directory '{backup_dir}' not found.")
        return None, current_out

    csv_files = sorted([f for f in os.listdir(backup_dir) if f.endswith('.csv')])
    
    while True:
        clear_screen()
        print("====================================================")
        print("         SPOTIFY TO MP3 DOWNLOADER (yt-dlp)         ")
        print("====================================================")
        print(f" Current Output: {os.path.abspath(current_out)}")
        print("====================================================")
        print("\nAvailable Playlists:")
        for i, file in enumerate(csv_files, 1):
            print(f"  [{i:02}] {file}")
        
        print("\n  [A] Download All Playlists")
        print("  [D] Change Download Directory")
        print("  [Q] Quit")
        print("\n====================================================")
        
        choice = input("\nSelect an option: ").strip().lower()
        
        if choice == 'q':
            sys.exit()
        elif choice == 'd':
            import tkinter as tk
            from tkinter import filedialog
            root = tk.Tk(); root.withdraw(); root.attributes("-topmost", True)
            new_path = filedialog.askdirectory(title="Select Download Directory", initialdir=os.path.abspath(current_out))
            root.destroy()
            if new_path:
                current_out = os.path.normpath(new_path)
                save_config(current_out)
                time.sleep(1)
        elif choice == 'a':
            return [os.path.join(backup_dir, f) for f in csv_files], current_out
        else:
            try:
                idx = int(choice) - 1
                if 0 <= idx < len(csv_files):
                    return [os.path.join(backup_dir, csv_files[idx])], current_out
            except ValueError:
                pass

if __name__ == "__main__":
    if not check_ffmpeg():
        sys.exit(1)

    selected_files, output_dir = show_menu()

    if selected_files:
        for file in selected_files:
            process_csv(file, output_dir)
        
        print("\n[!] All tasks finished.")
        try:
            os.startfile(output_dir)
        except:
            pass
        input("Press Enter to exit...")
