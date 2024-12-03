import os
import re

def mul(e):
    l = e[4:-1]
    x,y = l.split(',')
    return int(x) * int(y)

with open("./input.txt",'r') as f:
    text = f.read()

    pattern = r"mul\(\d{1,3},\d{1,3}\)"
                      #\d{1,3}\,\d{1,3}\)$

    matches = re.findall(pattern, text)

    s = 0
    for e in matches:
        s += mul(e)

    print(s)
