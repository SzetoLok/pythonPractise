from bs4 import BeautifulSoup
import requests
import re
from pytubefix import YouTube
import yfinance as yf
# m= re.search('\D','xx135367dra')
# print(m)
# m1 = re.findall('\D','xx135367dra')
# print(m1)
# sub = re.sub('\D','*','xx135367dra')
# print(sub)
# with open('/Users/szetolok/Desktop/Coding/pythonPractise/webscrape/names.csv','r', encoding='utf-8')as f:
#     data = f.readlines()
#     print(data)

# yt = YouTube('https://www.youtube.com/watch?v=0KmUoTfGa34')
# # yt.streams.first().download()
# print(yt.title)
df = yf.download("aapl")
print(df)
# content = requests.get('https://pythonscraping.com/pages/page3.html').text
# soup = BeautifulSoup(content, 'lxml')
# for child in soup.find('div').descendants:
#     print(child)
# img = soup.find('img')
# print(img)
# sibling = soup.find('div').img.next_sibling

# sibling = soup.find('div').table.find_next_sibling()
# # print(sibling) 
# parent = soup.find('div').div.p.parent
# print(parent) 


# url = 'https://www.ptt.cc/bbs/Gossiping/index.html'
# cookies = {'over18': '1'}
# ptt = requests.get(url, cookies=cookies)
# print(ptt)
# print(ptt.content)

# url = 'https://m.youtube.com/watch?v=9BDbpfDrcDY'
# youtube = requests.get(url)
# print(youtube.text)  # print the content of the page
# print(youtube.cookies.get_dict())  # bytes
# url = 'https://mail.google.com/mail/mu/mp/946/#tl/priority/%5Esmartlabel_personal'
# youtube = requests.get(url)
# print(youtube.status_code)  
# print(youtube.cookies.get_dict())  