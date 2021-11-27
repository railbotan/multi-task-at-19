import concurrent.futures
from urllib.request import Request, urlopen

links = open('res.txt', encoding='utf8').read().split('\n')


def load_wiki_url(url):
    request = Request(
        url,
        headers={'User-Agent': 'Mozilla/5.0 (Windows NT 9.0; Win65; x64; rv:97.0) Gecko/20105107 Firefox/92.0'},
    )
    try:
        resp = urlopen(request, timeout=5)
        code = resp.code
        resp.close()
        return code
    except Exception as e:
        return url, e


with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
    futures = []
    for url in links[:100]:
        futures.append(executor.submit(load_wiki_url, url))
    for future in concurrent.futures.as_completed(futures):
        print(future.result())

