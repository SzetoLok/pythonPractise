import threading
import queue
import requests

q = queue.Queue()
valid_proxies = []

with open('freeProxyList.txt', 'r') as f:
    proxies = f.read().split("\n")
    for proxy in proxies:
        q.put(proxy)

def check_proxies():
    global q
    while not q.empty():
        proxy = q.get()
        try:    
            response = requests.get('http://httpbin.org/ip', proxies={'http': proxy, 'https':proxy})
        except:
            continue
        if response.status_code == 200:
            print(proxy)

# for _ in range(10):
#     threading.Thread(target=check_proxies).start()

# with open('validproxy.txt', 'r') as f:
#     valid_proxies = f.read().split("\n")

sites = ['https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=&searchTextText=&txtKeywords=&txtLocation=hong+kong',
        'https://brightdata.com/cp/data_api/gd_ld7ll037kqy322v05?id=hl_ea8c0733&tab=api',
        'https://hk.jobsdb.com/software-jobs',
        'https://www.zenrows.com/blog/puppeteer-vs-beautifulsoup#avoid-getting-blocked',
        'http://httpbin.org/ip']

counter = 0
# for site in sites:
#     try:
#         print(f'using the proxy:{ proxies[counter]}')
#         res = requests.get(site, proxies={"http": proxies[counter],"https":  proxies[counter]})
#         print(res.status_code)
#         # print(res.text)
#     except:
#         print('failed')
#     finally:
#         counter+=1
#         counter%len(sites)

def run_all_proxy(proxies,sites):
    for site in sites:
        counter = 0
        for proxy in proxies:
            res = ''
            try:
                print(f'using the proxy:{ proxies[counter]}')
                res = requests.get(site, proxies={"http": proxies[counter],"https":  proxies[counter]})
                print(res.status_code)
                # print(res.text)
            except:
                print(res)
                print(type(res))
            finally:
                counter+=1

run_all_proxy(proxies,sites)