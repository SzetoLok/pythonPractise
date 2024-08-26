from bs4 import BeautifulSoup
import requests
import csv
print(f'Type your unfamiliar skill here:')
unfamiliar_skill = input('>')
print(f'\n Filtering "{unfamiliar_skill}"...')

content = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=&searchTextText=&txtKeywords=python&txtLocation=').text
# content2 = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=&searchTextText=&txtKeywords=python&txtLocation=')
# print(content.status_code)
soup = BeautifulSoup(content, 'lxml')
# print(soup)
jobs = soup.findAll('li',class_ = 'clearfix job-bx wht-shd-bx')
print('========')
# print(job)
all = []
for index, job in enumerate(jobs):
    published_date = soup.find('span', class_ = 'sim-posted').span.text
    # print(published_date.span.text)
    experience = job.find('ul', class_='top-jd-dtl clearfix').li.text
    print(experience)
    if 'day' in published_date:
        company_name = job.find('h3', class_ = 'joblist-comp-name').text.replace(' ','').strip()
    # print(company_name.text.replace(' ',''))
        skills = job.find('span', class_ = 'srp-skills').text.replace(' ','')

    # print(skills)
        if unfamiliar_skill.lower() not in skills.lower():
            # print(f'Company : {company_name}')
            print(f'Company : {company_name}')
                # print(f'required skills : {skills.strip()}')
                # print(f'Published Date : {published_date}')
                # print(f'More Info : {more_info}')
            with open(f'posts/{index}.txt', 'w')as f:
                more_info = job.find('a')['href']
                f.write(f'Company : {company_name.strip()} \n')
                f.write(f'required skills : {skills.strip()}\n')
                f.write(f'Published Date : {published_date}\n')
                f.write(f'More Info : {more_info}')
            all.append({
                'company_name': company_name,
                'more_info': more_info,
                })
print(all)
for data in all:
    print(data['company_name'])
    print(data['more_info'])

with open('posts/info.csv', 'w')as f:
    fieldnames= ['company_name','more_info']
    csv_dictwriter = csv.DictWriter(f, fieldnames=fieldnames)
    csv_dictwriter.writeheader()
    for data in all:
        csv_dictwriter.writerow({  
            'company_name': data['company_name'],
            # 'skills': skills,
            # 'publishDate': published_date,
            'more_info': data['more_info']
            })
    
