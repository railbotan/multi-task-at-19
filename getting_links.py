from bs4 import BeautifulSoup as BS
import tqdm
from urllib.request import urlopen

url = 'https://ru.wikipedia.org/wiki/%D0%A1%D0%BB%D1%83%D0%B6%D0%B5%D0%B1%D0%BD%D0%B0%D1%8F:%D0%A1%D0%BB%D1%83%D1%87%D0%B0%D0%B9%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0'

with open('urls.txt', 'w', encoding='utf8') as result_file:
    for i in tqdm.tqdm(range(20)):
        html = urlopen(url).read().decode('utf8')
        soup = BS(html, 'html.parser')
        links = soup.find_all('a')

        for link in links:
            href = link.get('href')
            if href and (href.startswith('http://') or href.startswith('https://'))  and 'wiki' not in href:
                print(href, file=result_file)