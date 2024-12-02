import os

left = []
right = []
with open("input.txt", 'r') as f:
    for l in f:
        x,y = l.split()
        left.append(int(x))
        right.append(int(y))

s = 0
for e in left:
    s += e*right.count(e)
print(s)
