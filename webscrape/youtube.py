from pytubefix import YouTube, Playlist
from bs4 import BeautifulSoup
import requests
import re

headers = {
    'content-type': 'text/html; charset=UTF-8',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
}
yt = requests.get('https://www.youtube.com/watch?v=QffwmodQd9A&list=LL', headers=headers)
soup = BeautifulSoup(yt.text, 'lxml')
# print(soup)
jobs = soup.findAll('div', class_='ytm-playlist-panel-renderer-v2')
# print(jobs)
# print(yt.text)
playlist = Playlist('https://www.youtube.com/watch?v=QffwmodQd9A&list=LL')
vlist = re.findall('watch\?v=.*&list',yt.text)
for item in vlist:
    print(item)
    print()
print(playlist)

yt = YouTube('https://www.youtube.com/watch?v=zN9UMH-yCtQ')
# yt.streams.filter(only_audio=True).first().download()
# print(yt.captions['a.en'])
srt = yt.captions['a.en'].generate_srt_captions()
# print(srt)
with open('encaption.txt', 'w') as f:
    f.write(srt)
