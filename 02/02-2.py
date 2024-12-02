import os

with open("input.txt", 'r') as f:
    s = 0
    for l in f:
        list = l.split()
        list = [int(x) for x in list]
        asc = 0
        desc = 0
        err = 0
        fallo = False
        idxPico = -1
        idxValle = -1
        for i in range(1,len(list)-1):
            if list[i-1] <= list[i] >= list[i+1] and idxPico == -1 :
                idxPico = i
            elif list[i-1] <= list[i] >= list[i+1] and idxPico != -1:
                fallo = True
            elif list[i-1] >= list[i] <= list[i+1] and idxPico == -1:
                idxValle = i
            elif list[i-1] >= list[i] <= list[i+1] and idxPico != -1:
                fallo = True

        for i in range(1,len(list)):
            if(list[i] - list[i-1] <= 0 ):
                desc += 1
            elif(list[i] - list[i-1] >= 0):
                asc += 1


        consecutiveSinValle = True
        consecutiveSinPico = True
        listSinValle = [list[i] for i in range(len(list)) if i != idxValle]
        listSinPico = [list[i] for i in range(len(list)) if i != idxPico]
        print(listSinPico)

        for i in range(1,len(listSinValle)):
            if((asc > desc and listSinValle[i] - listSinValle[i-1] <= 0 or listSinValle[i] - listSinValle[i-1] > 3 ) or ( asc <= desc and listSinValle[i] - listSinValle[i-1] >= 0 or listSinValle[i] - listSinValle[i-1] < -3)):
                consecutiveSinValle = False
        for i in range(1,len(listSinPico)):
            if((asc > desc and listSinPico[i] - listSinPico[i-1] <= 0 or listSinPico[i] - listSinPico[i-1] > 3 ) or ( asc <= desc and listSinPico[i] - listSinPico[i-1] >= 0 or listSinPico[i] - listSinPico[i-1] < -3)):
                consecutiveSinPico = False
        if(consecutiveSinPico or consecutiveSinValle):
            s += 1
    print(s)
