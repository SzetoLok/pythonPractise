from bs4 import BeautifulSoup
import requests

# print(f'Type your unfamiliar skill here:')
# unfamiliar_skill = input('>')
# print(f'\n Filtering "{unfamiliar_skill}"...')
content = requests.get('https://szetolok.github.io/').text
soup = BeautifulSoup(content, 'lxml')
home = soup.find('section', class_='home')
print(home)
print('=======')
home_content = home.find('div', class_='home-content')
print(home_content)