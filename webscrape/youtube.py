from pytubefix import YouTube
from pytube import Playlist
from bs4 import BeautifulSoup
import requests
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import csv


def getHref(url):
    # get href from a search page
    driver = webdriver.Chrome()
    driver.get(url)
    print(driver.title)
    tags = driver.find_elements(By.XPATH, value=f'//*[@id="video-title"]')
    print(tags)
    driver.implicitly_wait(5)
    links = []
    with open('youtube_tcpip.csv','w') as new_file:
        fieldnames= ['url','title']
        csv_writer = csv.DictWriter(new_file,fieldnames=fieldnames, delimiter='\t')
        csv_writer.writeheader()
        for tag in tags:
            href = tag.get_attribute('href')
            title = tag.accessible_name
            if href:
                links.append(href)
                print(href)
                print(title)
                csv_writer.writerow({'url':url, 'title':title})
        print(len(links))
    driver.quit()

def getPlayList(url):
    driver = webdriver.Chrome()
    driver.get(url)
    print(driver.title)
    driver.implicitly_wait(15)
    tags = driver.find_elements(By.XPATH, value=f'//*[@id="wc-endpoint"]')
    print(tags)
    links = []
    for tag in tags:
        href = tag.get_attribute('href')
        if href:
            links.append(href)
            print(href)
    print(len(links))
    driver.quit()

def  getMorePageAndVideo(url):
    driver = webdriver.Chrome()
    driver.get(url)
    print(driver.title)
    driver.implicitly_wait(15)
    for i in range(5):
        html = driver.find_elements(By.TAG_NAME, value='html')
        print(html)
        print(f'------------' )
        print(f'{i}st')
        print(f'------------' )

        # getHref('https://www.youtube.com/results?search_query=247talk&sp=CAISAhAB')
        html[0].send_keys(Keys.END)
        driver.implicitly_wait(20)
    tags = driver.find_elements(By.XPATH, value=f'//*[@id="video-title"]')

    # print(f'------------' )
    # print(f'2nd')
    # print(f'------------' )
    # getHref('https://www.youtube.com/results?search_query=247talk&sp=CAISAhAB')
    links = []
    for index,tag in enumerate(tags):
        href = tag.get_attribute('href')
        if href:
            links.append(href)
            print(str(index)+' '+href+tag.text)
    print(len(links))
    driver.quit()

r = getHref('https://www.youtube.com/results?search_query=virtual+connection+tcpip')
# getMorePageAndVideo('https://www.youtube.com/results?search_query=247talk&sp=CAISAhAB')
# getPlayList('https://www.youtube.com/watch?v=D91EqWrlnC8&list=PLaKrQOjpVj_aFbV8wQCaVKoHFIsGR35sd')
# getPlayList('https://www.youtube.com/watch?v=PaFPbb66DxQ&list=PLblh5JKOoLUIzaEkCLIUxQFjPIlapw8nU')
# headers = {
#     'content-type': 'text/html; charset=UTF-8',
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
# }
# yt = requests.get('https://www.youtube.com/watch?v=QffwmodQd9A&list=LL', headers=headers)
# soup = BeautifulSoup(yt.text, 'lxml')
# # print(soup)
# jobs = soup.findAll('div', class_='ytm-playlist-panel-renderer-v2')
# # print(jobs)
# # print(yt.text)
playlist = Playlist('https://www.youtube.com/playlist?list=LL')
# playlist._video_regex = re.compile(r"/")
# vlist = re.findall('watch\?v=.*&list',yt.text)
# for item in vlist:
#     print(item)
#     print()
print(playlist.video_urls)

# yt = YouTube('https://www.youtube.com/watch?v=zN9UMH-yCtQ')
# # yt.streams.filter(only_audio=True).first().download()
# # print(yt.captions['a.en'])
# srt = yt.captions['a.en'].generate_srt_captions()
# # print(srt)
# with open('encaption.txt', 'w') as f:
#     f.write(srt)
