from hashlib import md5
from random import choice
import concurrent.futures
import time
t = time.time()


def mining():
    while True:
        s = "".join([choice("0123456789") for i in range(50)])
        h = md5(s.encode('utf8')).hexdigest()

        if h.endswith("00000"):
            print(s, h)
            return (s, h)

def main():
    with concurrent.futures.ProcessPoolExecutor(max_workers=60) as executor:
        for _ in range(4):
            executor.submit(mining)
            

if __name__ == '__main__':
    main()
    print(time.time() - t)

    