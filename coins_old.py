from hashlib import md5
from random import choice

lst = []
while len(lst) < 5:
    s = "".join([choice("0123456789") for i in range(50)])
    h = md5(s.encode('utf8')).hexdigest()
    if h.endswith("00000"):
        lst.append("{} {}".format(s, h))
print(lst)

