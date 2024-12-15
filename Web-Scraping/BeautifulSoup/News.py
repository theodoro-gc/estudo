import requests
from bs4 import BeautifulSoup

responce = requests.get('https://g1.globo.com/')   

content = responce.content

site = BeautifulSoup(content, 'html.parser')

post = site.find('div', attrs={'class': 'feed-post-body'})


titulo = post.find('a', attrs={'class': 'feed-post-link'})

print(titulo.text)