import os

with open("input.txt", 'r') as f:
    s = 0
    for l in f:
        list = l.split()
        list = [int(x) for x in list]
        if list[0] == list[1]:
            continue
        elif list[0] < list[1]:
            asc = True
        else:
            asc = False
        consecutive = True
        for i in range(1,len(list)):
            if((asc and list[i] - list[i-1] <= 0 or list[i] - list[i-1] > 3 ) or (not asc and list[i] - list[i-1] >= 0 or list[i] - list[i-1] < -3)):
                consecutive = False
        if(consecutive):
            s += 1
    print(s)
