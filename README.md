# YouTube Playlist Downloader

This repository contains a Python script, `youtubeplaylistdownload.py`, designed to download YouTube playlists efficiently. The script leverages tools like `yt-dlp` to handle video downloads.

## Features
- Download entire YouTube playlists.
- Supports various video and audio formats.
- Logs download progress and errors.

## Prerequisites
Before using the script, ensure you have the following installed:

1. **Python** (>= 3.8)
2. **yt-dlp**
3. **FFmpeg** (for audio/video conversion)

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/yuzuponikemi/musicR.git
cd musicR
```

### 2. Set Up the Python Environment

#### Using `uv` (Recommended)
1. Ensure `uv` is installed. If not, install it:
   ```bash
   pip install uv
   ```
2. Initialize the project:
   ```bash
   uv sync
   ```

#### Using `venv`
1. Create a virtual environment:
   ```bash
   python -m venv .venv
   ```
2. Activate the virtual environment:
   - On Windows:
     ```bash
     .venv\Scripts\Activate.ps1
     ```
   - On macOS/Linux:
     ```bash
     source .venv/bin/activate
     ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### 3. Install Required Tools
- Install `yt-dlp`:
  ```bash
  pip install yt-dlp
  ```
- Ensure `FFmpeg` is installed and added to your system's PATH.

### 4. Run the Script
To download a playlist, run:
```bash
python youtubeplaylistdownload.py
```

## Logging
The script generates logs to track download progress and errors:
- `log.txt`: General logs.
- `log.csv`: Detailed logs in CSV format.

## Contributing
Feel free to fork this repository and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

## License
This project is licensed under the MIT License. See the LICENSE file for details.