from hashlib import md5
from random import choice
import concurrent.futures
import math

PRIMES = [0,0,0,0]

def is_prime(n):
    while True:
        s = "".join([choice("0123456789") for i in range(50)])
        h = md5(s.encode('utf8')).hexdigest()
        if h.endswith("00000"):
            n = str(s) + ' ' + str(h)
            break
    return n

def main():
    with concurrent.futures.ProcessPoolExecutor(max_workers=61) as executor:
        for prime in zip(PRIMES, executor.map(is_prime, PRIMES)):
            print(prime)

if __name__ == '__main__':
    main()
