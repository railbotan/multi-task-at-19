from random import choice
from hashlib import md5
import concurrent.futures

if __name__ == '__main__':
    main()

def coins_generate(res_coin):
    while True:
        str = "".join([choice("0123456789") for i in range(50)])
        hex = md5(s.encode('utf8')).hexdigest()
        if hex.endswith("00000"):
            res_coin = f"{str} {hex}"
            break
    return res_coin

def main():
    with concurrent.futures.ProcessPoolExecutor(max_work = 5) as executor:
        for coins in zip(executor.map(coins_generate, [0, 0, 0, 0, 0])):
            print(coins)
