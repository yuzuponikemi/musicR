import os
import subprocess
import glob
import webbrowser



    
def convert_mp4_to_mp4(mp4_file, mp4_file_new):
    subprocess.call(['ffmpeg', '-i', mp4_file, '-c:v', 'libx264', '-c:a', 'aac', mp4_file_new])
    
def convert_mp4_to_avi(mp4_file, avi_file):
    subprocess.call(['ffmpeg', '-i', mp4_file, '-c:v', 'libx264', '-c:a', 'aac', avi_file])

def convert_all_mp4_to_avi(directory):
    for filename in os.listdir(directory):
        if filename.endswith(".mp4"):
            mp4_file = os.path.join(directory, filename)
            avi_file = os.path.join(directory, os.path.splitext(filename)[0] + ".avi")
            convert_mp4_to_avi(mp4_file, avi_file)

# Replace 'your_directory' with the path to the directory containing your mp4 files
folder_path = r'C:\Users\yuzup\Videos\foreversessionslivevideos'
convert_all_mp4_to_avi(folder_path)