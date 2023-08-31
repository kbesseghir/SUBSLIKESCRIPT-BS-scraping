import requests
from  bs4 import BeautifulSoup
import csv 

root='https://subslikescript.com'
result =requests.get('https://subslikescript.com/movies_letter-A')
content =result.content
soup=BeautifulSoup(content,'lxml')

box = soup.find('ul',class_='pagination')
pages =box.find_all('li',class_='page-item')
last_page=pages[-2].text
for page in range(1,int(last_page))[:2]:
    result =requests.get(f'http://subslikescript.com/movies_letter-A?page={page}')
    content =result.content
    soup=BeautifulSoup(content,'lxml')
    box = soup.find('article', class_='main-article')
    links = []
    for link in box.find_all('a', href=True):  # find_all returns a list
        links.append(link['href'])

    for link in links:
        result=requests.get(f'{root}/{link}')
        content=result.content
        soup = BeautifulSoup(content,'lxml')
        box = soup.find('article',class_="main-article")
        titel =box.find('h1').text
        script = box.find('div',class_='full-script').text

        with open(f'{titel}.txt','w')as file :
           file.write(script)
        print ('file created')
