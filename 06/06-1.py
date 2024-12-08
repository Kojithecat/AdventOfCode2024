import os

with open("input.txt", 'r') as f:

    list = f.read().split('\n')[:-1]
    print(list)
        #Scan for inital pos
    posI = -1
    posJ = -1
    for i in range(len(list)):
        for j in range(len(list[i])):
            if(list[i][j] == '^'):
                posI = i
                posJ = j
                break;
    print(posI, posJ)

    deltaI = -1
    deltaJ = 0
    while(posI + deltaI >= 0 and posI+deltaI < len(list) and posJ+deltaJ >= 0 and posJ+deltaJ < len(list[posI])):
        print(posJ, posI)
        list[posI] = list[posI][:posJ] + 'X' + list[posI][posJ+1:]
        if(list[posI+deltaI][posJ+deltaJ] == "#"):
            if(deltaI == -1):
                deltaI = 0
                deltaJ = 1
            elif(deltaI == 1):
                deltaI = 0
                deltaJ = -1
            elif(deltaJ == -1):
                deltaJ = 0;
                deltaI = -1
            elif(deltaJ == 1):
                deltaJ = 0
                deltaI = 1

        elif list[posI+deltaI][posJ+deltaJ] == '.' or list[posI+deltaI][posJ+deltaJ] == 'X':
            posI += deltaI
            posJ += deltaJ

    s = 1
    for l in list:
        for c in l:
            if(c == 'X'):
                s+= 1
    print(s)
