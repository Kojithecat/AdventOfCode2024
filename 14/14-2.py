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
map = []
for i in range(height):
    map.append(['0']*width)

print(map)

for i in range(10000):
    if i%100 == 0:
        print(i)
    mapcp = copy.deepcopy(map)
    density = 0
    for r in robots:
        r[0] = (r[0] + r[2]) % width
        r[1] = (r[1] + r[3]) % height
        map[r[1]][r[0]] = str(int(map[r[1]][r[0]])+1)
    if i > 6000: #Easter egg is not in the first 6000 seconds
        for x in range(1,len(map)-1):
            for y in range(1,len(map[x])-1):
                if map[x][y] != '0' and map[x+1][y] != '0' and map[x-1][y] != '0' and map[x][y+1] != '0' and map[x][y-1] != '0':
                    density += 1
        if density > 15:
            for l in map:
                s = ""
                for c in l:
                    if c == '0':
                        s += '.'
                    else:
                        s += c
                print(s)
            print('\n',i+1,'\n')
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
