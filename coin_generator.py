from concurrent.futures import ProcessPoolExecutor
from hashlib import md5
from random import choice


def validate_coin():
    while True:
        s = "".join([choice("0123456789") for i in range(50)])
        h = md5(s.encode('utf8')).hexdigest()

        if h.endswith("00000"):
            return s, h


def find_coin(workers):
    with ProcessPoolExecutor(max_workers=workers) as executor:
        for i in range(4):
            executor.submit(validate_coin)


if __name__ == '__main__':
    find_coin(8)
