from urllib.request import Request, urlopen
from urllib.parse import unquote
from urllib.request import urlopen
from urllib.parse import unquote
from bs4 import BeautifulSoup
from tqdm import tqdm
import concurrent.futures

if __name__ == "__main__":
    links = open('res.txt', encoding='utf8').read().split('\n')

    with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
        for url in links:
            try:
                request = Request(
                    url,
                    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 9.0; Win65; x64; rv:97.0) Gecko/20105107 Firefox/92.0'},
                )
                resp = urlopen(request, timeout=5)
                code = resp.code
                print(code)
                resp.close()
            except Exception as e:
                print(url, e)
