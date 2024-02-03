import os
import subprocess
import glob
import webbrowser

# 1. Open a folder with explorer window
folder_path = r'C:\Users\yuzup\Videos\mixsession1'

# 2. Find all the mp4 files in the folder and show the list
os.chdir(folder_path)
mp4_files = glob.glob('*.mp4')
print(mp4_files)

# 3. Convert all of them into mp3 files
# 4. Save all mp3 files into the new folder named from exact folder where mp4 found
new_folder = folder_path + '\\mp3'
os.makedirs(new_folder, exist_ok=True)

for mp4_file in mp4_files:
    mp3_file = os.path.join(new_folder, os.path.splitext(mp4_file)[0] + '.mp3')
    subprocess.call(['ffmpeg', '-i', mp4_file, '-vn', '-acodec', 'libmp3lame', '-ac', '2', '-q:a', '6', mp3_file])