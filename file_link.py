from urllib.request import Request, urlopen
import concurrent.futures

def information_about_page_existence(page_url):
    req = Request(
        page_url,
        headers={'User-Agent': 'Mozilla/5.0 (Windows NT 9.0; Win65; x64; rv:97.0) Gecko/20105107 Firefox/92.0'},
    )
    res_req = urlopen(req, timeout = 100)
    code = res_req.code
    res_req.close()
    return code

links_file = open('res.txt', encoding = 'utf8').read().split('\n')

with concurrent.futures.ThreadPoolExecutor(max_work = 100) as executor:
    futures = []
    for url in links_file:
        futures.append(executor.submit(information_about_page_existence, url))
    for future in concurrent.futures.as_completed(futures):
        try:
            print(future.result())
        except Exception as e:
            print(url, e)
            