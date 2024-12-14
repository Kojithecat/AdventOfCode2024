import os
import copy

list = []
width = 101
height = 103

with open("input.txt", 'r') as f:
    sumTot = 0
    list = f.read().split('\n')[:-1]
    print(list)

robots = []
for e in list:
    rawp,rawv = e.split(' ')
    print(rawp, rawv)
    px,py = rawp[2:].split(',')
    vx, vy = rawv[2:].split(',')

    print(px, py, vx, vy)
    robots.append([int(px), int(py), int(vx), int(vy)])

print(robots)

for i in range(100):
    if i%100 == 0:
        print(i)
    mapcp = copy.deepcopy(map)
    density = 0
    for r in robots:
        r[0] = (r[0] + r[2]) % width
        r[1] = (r[1] + r[3]) % height
    map = mapcp

q1 = 0
q2 = 0
q3 = 0
q4 = 0
for r in robots:
#    print(robot)
    if r[0] < width//2 and r[1] < height //2:
        q1 += 1
    if r[0] < width//2 and r[1] > height //2:
        q2 += 1
    if r[0] > width//2 and r[1] < height //2:
        q3 += 1
    if r[0] > width//2 and r[1] > height //2:
        q4 += 1

print(q1*q2*q3*q4)


#Testing area
#map = [['0']*11, ['0']*11, ['0']*11, ['0']*11, ['0']*11, ['0']*11, ['0']*11]


#for r in robots:
#    map[r[1]][r[0]] = str(int(map[r[1]][r[0]])+1)

#for l in map:
#    print(l)
