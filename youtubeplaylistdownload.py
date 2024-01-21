# -*- coding: utf-8 -*-
"""
Created on Sat Jan 21 22:57:39 2023

@author: ykemi
"""

from yt_dlp import YoutubeDL
import os
ydl_video_opts = {
    'outtmpl': '%(title)s'+'.mp3',
    'format': 'bestaudio'
}

ydl_opts = {
    'format': 'bestaudio',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'outtmpl': '%(title)s',
    'ignoreerrors' : 'True'
}

#get the artist or channel name
artist_name = input('Please enter the folder name: ')
#create folder
os.chdir("G:\Music")
os.mkdir(artist_name)
os.chdir(artist_name)

with YoutubeDL(ydl_opts) as ydl:
    result = ydl.download([
        'https://www.youtube.com/@mymusic9447/videos'
    ])
    
    