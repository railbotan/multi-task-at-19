import datetime
from concurrent.futures import ThreadPoolExecutor
from urllib.request import Request, urlopen

import certifi

print(datetime.datetime.now())
links = open('wiki_urls.txt', encoding='utf8').read().split('\n')


def try_open(url):
    try:
        request = Request(
            url,
            headers={'User-Agent': 'Mozilla/5.0 (Windows NT 9.0; Win65; x64; rv:97.0) Gecko/20105107 Firefox/92.0'},
        )
        resp = urlopen(request, timeout=100, cafile=certifi.where())
        code = resp.code
        resp.close
        return code
    except Exception as e:
        return url + " " + str(e)


with ThreadPoolExecutor(max_workers=100) as executor:
    for i in executor.map(try_open, links):
        print(i)

print(datetime.datetime.now())
