from bs4 import BeautifulSoup
import requests

pre = 'https://www.lainchan.org/Ω'
html = requests.get('https://www.lainchan.org/Ω/catalog.html')
soup = BeautifulSoup(html.text, 'html.parser')
links = []
for thread in soup.find_all('div', class_='thread'):
    for ref in thread.find_all('a'):
        l = ref.get('href')
        if '/Î©/res/' in l:
            links.append(l.split('Î©')[1])
            
for link in links:
    html = requests.get(pre + link)
    soup = BeautifulSoup(html.text, 'html.parser')
    thread = soup.find_all('div', class_='body')[0]
    print(thread.get_text('\n\n'), '\n\n')
