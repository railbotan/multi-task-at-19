from urllib.request import Request, urlopen
from tqdm import tqdm
import concurrent.futures

links = open('res.txt', encoding='utf8').read().split('\n')[0:50]


def load_url(url):
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
        return f"{url} {e}"


with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
    future_to_url = {executor.submit(load_url, url): url for url in links}
    for future in tqdm(concurrent.futures.as_completed(future_to_url)):
        url = future_to_url[future]
        result = future.result()
        print(result)
