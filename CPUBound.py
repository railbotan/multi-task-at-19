from hashlib import md5
from random import choice
import concurrent.futures

if __name__ == "__main__":

    with concurrent.futures.ProcessPoolExecutor(max_workers=8) as executor:
        a = 0
        while True:
            s = "".join([choice("0123456789") for i in range(50)])
            h = md5(s.encode('utf8')).hexdigest()

            if h.endswith("00000"):
                print(s, h)
                a += 1
            if a == 3:
                break
