from urllib.request import Request, urlopen
from urllib.parse import unquote
from concurrent.futures import ThreadPoolExecutor, as_completed

def check_link(url):
    try:
        request = Request(
            url,
            headers={'User-Agent': 'Mozilla/5.0 (Windows NT 9.0; Win65; x64; rv:97.0) Gecko/20105107 Firefox/92.0'},
        )
        resp = urlopen(request, timeout=5)
        code = resp.code
        resp.close()
        return code
    except Exception as e:
        print(url, e)

links = open('res.txt', encoding='utf8').read().split('\n')[0:101]

with ThreadPoolExecutor(max_workers=50) as executor:
    futures = []
    for url in links:
        futures.append(executor.submit(check_link, url=url))
    for future in as_completed(futures):
        print(future.result())

