from urllib.request import Request, urlopen
import concurrent.futures


def get_wiki_page_existence(wiki_page_url):
    request = Request(
        wiki_page_url,
        headers={'User-Agent': 'Mozilla/5.0 (Windows NT 9.0; Win65; x64; rv:97.0) Gecko/20105107 Firefox/92.0'},
    )
    resp = urlopen(request, timeout=100)
    code = resp.code
    resp.close()
    return code


links = open('res.txt', encoding='utf8').read().split('\n')

with concurrent.futures.ThreadPoolExecutor(max_workers=61) as executor:
    futures = []
    for url in links:
        futures.append(executor.submit(get_wiki_page_existence, url))
    for future in concurrent.futures.as_completed(futures):
        try:
            print(future.result())
        except Exception as e:
            print(url, e)
