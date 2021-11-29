import concurrent.futures
from urllib.request import Request, urlopen


links = open('res.txt', encoding='utf8').read().split('\n')


def get_respond(url):
    request = Request(
        url,
        headers={'User-Agent': 'Mozilla/5.0 (Windows NT 9.0; Win65; x64; rv:97.0) Gecko/20105107 Firefox/92.0'},
    )
    resp = urlopen(request, timeout=5)
    return resp.code


with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
    future_to_url = {executor.submit(get_respond, url): url for url in links}
    for future in concurrent.futures.as_completed(future_to_url):
        url = future_to_url[future]
        try:
            code = future.result()
        except Exception as exc:
            print(url, exc)
        else:
            print(code)
