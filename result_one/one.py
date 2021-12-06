import concurrent.futures
import urllib.request
from urllib.request import Request, urlopen
from urllib.parse import unquote
import time

#ThreadPoolExecutor - ПОТОКИ
t = time.time()
links = open('res.txt', encoding='utf8').read().split('\n')


def load_url(url, timeout):
    request = Request(
            url,
            headers={'User-Agent': 'Mozilla/5.0 (Windows NT 9.0; Win65; x64; rv:97.0) Gecko/20105107 Firefox/92.0'},  
        )
    with urllib.request.urlopen(request, timeout=timeout) as conn:
        return conn.code

with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
    future_to_url = {executor.submit(load_url, url, 60): url for url in links}
    for future in concurrent.futures.as_completed(future_to_url):
        url = future_to_url[future]
        try:
            data = future.result()
        except Exception as e:
            print('%r generated an exception: %s' % (url, e))
        else:
            print('%r page is code %d ' % (url, data))


print(time.time() - t)