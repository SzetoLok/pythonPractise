import httpx
import json
import pandas as pd
from pytrends.request import TrendReq
import pandas as pd
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import nmap


   
def getTrendByKeywords(keywords):


    # Initialize the pytrends request
    pytrends = TrendReq(hl='en-US', tz=360)

    # Define the keywords

    # Create a payload with the required keywords
    pytrends.build_payload(keywords, timeframe='today 12-m')

    # Retrieve interest over time
    data = pytrends.interest_over_time()

    # Check if the data has the 'isPartial' column and drop it
    if 'isPartial' in data.columns:
        data = data.drop(columns=['isPartial'])

    # Display the data
    print(data)

    # Optionally, save the data to a CSV file
    data.to_csv('google_trends_data.csv')


def getTopic(url):
    # date = '20240827'
    # url = url.format(date)
    r = requests.get(url)
    # print(r.text)
    data = json.loads(r.text.replace(")]}\',\n", ""))
    # print(data)
    # results = data["default"]["rankedList"][1]["rankedKeyword"][0]['topic']
    # print(results)
    for j in range(len(data["default"]["rankedList"])):
        print(len(data["default"]["rankedList"][j]["rankedKeyword"]))
        for i in range(len(data["default"]["rankedList"][j]["rankedKeyword"])):
            print(data["default"]["rankedList"][j]["rankedKeyword"][i]['topic'])
    # driver = webdriver.Chrome()
    # driver.get(url)
    # driver.implicitly_wait(15)

    # print(driver.text)

def pytrends():
    pytrend = TrendReq(hl='zh-TW', tz=-480)
    keywords = ["Python"]
    pytrend.build_payload(
        kw_list=keywords,
        cat=0,
        timeframe="2024-08-01 2024-08-28",
        geo="HK")
    # print(pytrend.interest_over_time())
    hk = pytrend.trending_searches(pn="hong_kong")
    print(hk.head(10))
    annualHK = pytrend.top_charts(2023,hl='zh-TW', tz=-480, geo='HK')
    print(annualHK.head(20))

def topCharts(url):
    r = requests.get(url)
    data = json.loads(r.text.replace(")]}\'\n", ""))
    for i in range(len(data['topCharts'])):
        print('--------------')
        print(str(i)+data['topCharts'][i]['listTitle'])
        print('--------------')

        for j in range(len(data['topCharts'][i]["listItems"])):
            print(str(j)+data['topCharts'][i]["listItems"][j]["title"])
def getSuggestion():
    # r = requests.get(url)
    pytrends = TrendReq()
    suggest = pytrends.suggestions(keyword='python')
    # print(suggest)
    pytrends2 = TrendReq(hl='zh-TW', tz=-480)
    pytrends2.build_payload(kw_list=['Python'])

    region = pytrends2.interest_by_region()
    # print(regionr.sort_values(['Python'], ascending=False).head(10))
    # print(pytrends2.related_queries())
    print(pytrends2.related_topics())

def relatedQuery(url):
    r = requests.get(url)
    data = json.loads(r.text.replace(")]}\',\n", ""))
    for j in range(len(data["default"]["rankedList"])):
        print(len(data["default"]["rankedList"][j]["rankedKeyword"]))
        for i in range(len(data["default"]["rankedList"][j]["rankedKeyword"])):
            print(data["default"]["rankedList"][j]["rankedKeyword"][i]['query'])

def plotLine(keywords):
    pd.set_option('future.no_silent_downcasting', True)
    pytrend = TrendReq(hl='zh-TW', tz=-480)
    pytrend.build_payload(
        kw_list=keywords,
        cat=0,
        timeframe="today 3-m",
        geo="HK")
    df = pytrend.interest_over_time().drop(['isPartial'], axis=1)
    print(df)
    df.plot(kind='line', title="python vs r")
# pytrends()
# topCharts('https://trends.google.com.tw/trends/api/topcharts?hl=zh-TW&tz=-480&date=2023&geo=HK&isMobile=false')
# relatedQuery('https://trends.google.com.tw/trends/api/widgetdata/relatedsearches?hl=zh-TW&tz=-480&req=%7B%22restriction%22:%7B%22geo%22:%7B%22country%22:%22HK%22%7D,%22time%22:%222023-08-30+2024-08-30%22,%22originalTimeRangeForExploreUrl%22:%22today+12-m%22,%22complexKeywordsRestriction%22:%7B%22keyword%22:%5B%7B%22type%22:%22BROAD%22,%22value%22:%22python%22%7D%5D%7D%7D,%22keywordType%22:%22QUERY%22,%22metric%22:%5B%22TOP%22,%22RISING%22%5D,%22trendinessSettings%22:%7B%22compareTime%22:%222022-08-28+2023-08-29%22%7D,%22requestOptions%22:%7B%22property%22:%22%22,%22backend%22:%22IZG%22,%22category%22:0%7D,%22language%22:%22zh%22,%22userCountryCode%22:%22HK%22,%22userConfig%22:%7B%22userType%22:%22USER_TYPE_LEGIT_USER%22%7D%7D&token=APP6_UEAAAAAZtL_VI_K2QiADHi6z3PkrzWADgSxWNq9')
plotLine(['Python','R'])