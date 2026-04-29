from yt_dlp import YoutubeDL
import os
import tkinter as tk
from tkinter import scrolledtext, ttk
import threading

def log_message(log_widget, message):
    log_widget.insert(tk.END, message + "\n")
    log_widget.see(tk.END)

def download_playlist(artist_name, playlist_url, output_format, quality, log_widget):
    ydl_opts = {
        'format': 'bestaudio' if output_format != 'mp4' else 'bestvideo+bestaudio',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': output_format,
            'preferredquality': quality,
        }] if output_format != 'mp4' else [],
        'outtmpl': '%(title)s.%(ext)s',
        'ignoreerrors': 'True',
        'cookiefile': 'path/to/cookies.txt'  # Add this line if you have a cookies file
    }

    # create folder
    try:
        music_dir = os.path.join(r"C:\Users\yuzup\Music", artist_name)
        os.makedirs(music_dir, exist_ok=True)
        os.chdir(music_dir)
    except Exception as e:
        log_widget.after(0, log_message, log_widget, f"Error creating directory: {e}")
        return

    try:
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([playlist_url])
            log_widget.after(0, log_message, log_widget, f"Downloaded playlist: {playlist_url}")
    except Exception as e:
        log_widget.after(0, log_message, log_widget, f"Error downloading playlist: {e}")

def start_download():
    artist_name = artist_entry.get().strip()
    playlist_url = url_entry.get().strip()
    output_format = format_var.get()
    quality = quality_var.get()
    if not artist_name or not playlist_url or not output_format or not quality:
        log_message(log_widget, "Folder name, playlist URL, format, and quality cannot be empty.")
        return
    log_message(log_widget, f"Starting download for artist: {artist_name}, URL: {playlist_url}, Format: {output_format}, Quality: {quality}")
    threading.Thread(target=download_playlist, args=(artist_name, playlist_url, output_format, quality, log_widget)).start()

# Create GUI
root = tk.Tk()
root.title("YouTube Playlist Downloader")

tk.Label(root, text="Folder Name:").grid(row=0, column=0, padx=10, pady=10)
artist_entry = tk.Entry(root, width=50)
artist_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Playlist URL:").grid(row=1, column=0, padx=10, pady=10)
url_entry = tk.Entry(root, width=50)
url_entry.grid(row=1, column=1, padx=10, pady=10)

tk.Label(root, text="Output Format:").grid(row=2, column=0, padx=10, pady=10)
format_var = tk.StringVar(value="mp3")
format_menu = ttk.Combobox(root, textvariable=format_var, values=["mp3", "m4a", "wav", "mp4"])
format_menu.grid(row=2, column=1, padx=10, pady=10)

tk.Label(root, text="Quality:").grid(row=3, column=0, padx=10, pady=10)
quality_var = tk.StringVar(value="192")
quality_menu = ttk.Combobox(root, textvariable=quality_var, values=["128", "192", "320"])
quality_menu.grid(row=3, column=1, padx=10, pady=10)

download_button = tk.Button(root, text="Download", command=start_download)
download_button.grid(row=4, column=0, columnspan=2, pady=10)

log_widget = scrolledtext.ScrolledText(root, width=60, height=20)
log_widget.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()