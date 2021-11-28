import urllib
from urllib.request import Request
import concurrent.futures


def load_url(url, timeout):
    with urllib.request.urlopen(url, timeout=timeout) as conn:
        return conn.code


links = open('res.txt', encoding='utf8').read().split('\n')


with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
    future_to_url = {executor.submit(load_url, url, 5): url for url in links}
    for future in concurrent.futures.as_completed(future_to_url):
        url = future_to_url[future]
        try:
            code = future.result()
        except Exception as exception:
            print('%r generated an exception: %s' % (url, exception))
        else:
            print(f'{code:d} code')