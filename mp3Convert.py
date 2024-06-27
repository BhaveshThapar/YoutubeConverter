from pytube import YouTube
from sys import argv
from pathlib import Path
import requests
import re
from pydub import AudioSegment
import os

downloads_path = str(Path.home() / "Downloads")
 
link = argv[1]
def checkSite(url):
    youtube_regex = (
        r'(https?://)?(www\.)?'
        '(youtube|youtu|youtube-nocookie)\.(com|be)/'
        '(watch\?v=|embed/|v/|.+\?v=)?([^&=%\?]{11})')

    match = re.match(youtube_regex, url)
    if not match:
        return False

    video_id = match.group(6)
    api_url = f'https://www.youtube.com/oembed?url=http://www.youtube.com/watch?v={video_id}&format=json'
    request = requests.get(api_url, allow_redirects=False)
    return request.status_code == 200



if(checkSite(link) is True):
    yt = YouTube(link)
else:
    print("This is not a link, please try again!")
    exit()

print(f"Now converting {yt.title} into an audio file!")

audio = yt.streams.get_audio_only()
if audio:
    audio_file_path = audio.download(output_path=downloads_path)
    print("Download finished. Now converting to MP3...")

    audio_segment = AudioSegment.from_file(audio_file_path)
    mp3_file_path = os.path.splitext(audio_file_path)[0] + '.mp3'
    audio_segment.export(mp3_file_path, format='mp3')
else:
    print("Failed to get audio")