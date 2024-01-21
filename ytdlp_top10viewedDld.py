# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 17:12:40 2022

@author: yusuke
"""

import youtube_dl
import yt_dlp
import os

#get the artist or channel name
artist_name = input('Please enter the artist name or channel name: ')

#create folder
os.mkdir(artist_name)
os.chdir(artist_name)
# Create a list of videos
video_list = []

# Get all videos from the artist or channel
with youtube_dl.YoutubeDL({}) as ydl:
    result = ydl.extract_info(
        f'ytsearch20:{artist_name}',
        download=False # We just want to extract the info
    )

# Filter the list of videos to get only the ones longer than 20min
for video in result['entries']:
    if video['duration'] > 1200:
        video_list.append(video)

# Sort the list of videos by rating
video_list.sort(key=lambda x: x['view_count'], reverse=True)

# Get the 10 most high-rated videos
top_10_videos = video_list[:10]


# Print the list of top 10 videos
for video in top_10_videos:
    print(video["title"],video["view_count"])

# # Download all the videos in mp3 format
# for video in top_10_videos:
#     yt_dlp.download_video(video, format="mp3")


videos = [x["webpage_url"] for x in top_10_videos]

from yt_dlp import YoutubeDL

ydl_video_opts = {
    'outtmpl': '%(title)s'+'_.mp3',
    'format': 'bestaudio'
}
with YoutubeDL(ydl_video_opts) as ydl:
    result2 = ydl.download(videos)