import os
import subprocess
import glob

# 1. Open a folder with explorer window
folder_path = r'C:\Users\yuzup\Videos\mixsession1'

# 2. Find all the mp4 and wav files in the folder and show the list
os.chdir(folder_path)
media_files = glob.glob('*.mp4') + glob.glob('*.wav')
print(media_files)

# 3. Convert all of them into mp3 files
# 4. Save all mp3 files into the new folder named from exact folder where mp4 found
new_folder = os.path.join(folder_path, 'mp3')
os.makedirs(new_folder, exist_ok=True)

for media_file in media_files:
    mp3_file = os.path.join(new_folder, os.path.splitext(media_file)[0] + '.mp3')
    subprocess.call(['ffmpeg', '-i', media_file, '-vn', '-acodec', 'libmp3lame', '-ac', '2', '-q:a', '6', mp3_file])