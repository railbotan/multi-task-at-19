from concurrent.futures.process import ProcessPoolExecutor
from concurrent.futures import as_completed
from hashlib import md5
from random import choice


def find_coin():
    while True:
        s = "".join([choice("0123456789") for i in range(50)])
        h = md5(s.encode('utf8')).hexdigest()

        if h.endswith("00000"):
            return f"{s} {h}"

if __name__ == "__main__":
    with ProcessPoolExecutor(max_workers=50) as executor:
        futures = []
        for i in range(3):
            futures.append(executor.submit(find_coin))
        for future in as_completed(futures):
            print(future.result())