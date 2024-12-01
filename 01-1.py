import os

left = []
right = []
with open("input.txt", 'r') as f:
    for l in f:
        x,y = l.split()
        left.append(int(x))
        right.append(int(y))


left.sort()
right.sort()

print(sum(abs(x-y) for x,y in zip(left,right)))
