from concurrent.futures import ProcessPoolExecutor as PPE
from random import choice
from hashlib import md5
import time


def gen_digit_and_hash(_):
    result=""
    hash="11111111"
    while not hash.endswith("00000"):
        string = "".join([choice("0123456789") for i in range(50)])
        hash = md5(string.encode('utf8')).hexdigest()
        result=f"{string} - {hash}"
    return result

def main():
    with PPE(max_workers=10) as executor:
        for string in executor.map(gen_digit_and_hash, [0 for _ in range(4)]):
            print(string)

if __name__ == '__main__':
    start = time.time()
    main()
    print(time.time()-start)