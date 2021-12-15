import concurrent.futures as fut
from urllib.request import urlopen
import time

links = open('urls.txt', encoding='utf8').read().split('\n')


def load_url(url, timeout):
    with urlopen(url, timeout=timeout) as conn:
        return conn.read()

start = time.time()
with fut.ThreadPoolExecutor(max_workers=100) as executor:
    future_to_url = dict()

    for url in links:
        future_to_url[executor.submit(load_url, url, 20)] = url

    for future in fut.as_completed(future_to_url):
        url = future_to_url[future]
        try:
            data=future.result()
        except Exception as exception:
            print(url," generated an exception", exception)
        else:
            print(f"{url} - {len(data)}")

print(time.time()-start)