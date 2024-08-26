from bs4 import BeautifulSoup
import requests

# print(f'Type your unfamiliar skill here:')
# unfamiliar_skill = input('>')
# print(f'\n Filtering "{unfamiliar_skill}"...')

content = requests.get('https://hk.jobsdb.com/software-jobs').text
soup = BeautifulSoup(content, 'lxml')
# print(soup)
# job_cards = soup.find('div', class_="_1ullll00 _13mb3jhaq _13mb3jhak _13mb3jh7e _13mb3jhn _13mb3jh4y _13mb3jhfm mxwgy91")
job_cards = soup.findAll('div', class_="_1ullll00 _13mb3jh6m")
# print(job_cards)
# a = soup.findAll('a')
# for link in a:
#     print(link['href'])
for index ,job_card in enumerate(job_cards):
    # get the page url and enter it
    job_div = job_card.findAll('div', class_='_1ullll00 _13mb3jh5g _13mb3jh52')
    try:
        for job in job_div:
            print(job.a['href'])
    except TypeError as e:
        # if job.a['href'] == None:
            print(job.text)

    # job_page = job_div.find('a')
#     if job_page!= None:
#         job_page = job_card.find('a')['href']
#         job_website = 'https://hk.jobsdb.com'
#         job_url = job_website + job_page
# #     job_detail = requests.get(job_url).text
# #     soup2 = BeautifulSoup(job_detail, 'lxml')
#         print(job_url)
    # job_main = soup2.find('div', class_="_4603vi0 _9l8a1v70")
    # # print(job_cards)
    # title = job_main.find('h1', class_="_4603vi0 _9l8a1v4y _1wqtj1z0 _1wqtj1zl _1rhqcq74 _1wqtj1zs _1wqtj1z21")
    # job_company = job_main.find('span', class_='_4603vi0 _9l8a1v4y _1wqtj1z0 _1wqtj1z1 _1wqtj1z21 _1rhqcq74 _1wqtj1za')
    # # the same function as the previous line, but this time get its parent 'div' and try if i can get the text directly
    # a = job_main.find('div', class_='_4603vi0 _9l8a1vr _9l8a1vem _9l8a1vej _9l8a1vba _9l8a1vb7 _9l8a1v4y _9l8a1vfm')
    # print(a.text)

    # with open(f'jobsdbposts/{index}.txt','w') as f:
    #     f.write(f'job_page: {job_page} \n')
    #     f.write(f'job title: {title.text}\n')
    #     f.write(f'job_company: {job_company.text}\n')