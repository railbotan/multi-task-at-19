import datetime
from concurrent.futures import ProcessPoolExecutor
from hashlib import md5
from random import choice

print(datetime.datetime.now())


def gen_print(z):
    while True:
        s = "".join([choice("0123456789") for i in range(50)])
        h = md5(s.encode('utf8')).hexdigest()
        if h.endswith("00000"):
            print(s, h)
            print(datetime.datetime.now())
            break


def main():
    with ProcessPoolExecutor(max_workers=61) as executor:
        for c in executor.map(gen_print, range(100)):
            pass


if __name__ == '__main__':
    main()
