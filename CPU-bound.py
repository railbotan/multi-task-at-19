from hashlib import md5
from random import choice
import concurrent.futures

def get_coin():
    while True:
        s = "".join([choice("0123456789") for i in range(50)])
        h = md5(s.encode('utf8')).hexdigest()
        res = ""
        if h.endswith("00000"):
            return s, h

def find_coin(workers, count):
    with concurrent.futures.ProcessPoolExecutor(max_workers=workers) as executor:
        for i in range(count):
            executor.submit(get_coin)

if __name__ == '__main__':
    find_coin(61, 4)