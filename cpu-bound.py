from hashlib import md5
from random import choice
from concurrent.futures import ProcessPoolExecutor


def get_token():
    while True:
        s = "".join([choice("0123456789") for i in range(50)])
        h = md5(s.encode('utf8')).hexdigest()

        if h.endswith("00000"):
            return s, h


def print_token(workers_count, tokens_count):
    with ProcessPoolExecutor(max_workers=workers_count) as executor:
        for i in range(tokens_count):
            executor.submit(get_token)


if __name__ == '__main__':
    print_token(10, 10)
