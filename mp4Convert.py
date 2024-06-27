from pytube import YouTube
from sys import argv
from pathlib import Path
import requests
import re

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

print("Now converting " + yt.title + " into a video!")

res = yt.streams.get_highest_resolution()
res.download(downloads_path)

print("Task has finished!")