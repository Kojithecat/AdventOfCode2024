import os

with open("input.txt", 'r') as f:
    sumTot = 0
    list = f.read().split('\n')[:-1]
    print(list)

    for line in list:
        ans = int(line.split(':')[0])
        operands = [int(x) for x in line.split(':')[1].strip().split(' ')]
        print(ans, operands)
        n = 3** (len(operands)-1)
        for i in range(n):
            ops = []
            cpi = i
            while cpi > 0:
                if(cpi%3 == 0):
                    ops.append('+')
                elif cpi%3 == 1:
                    ops.append('*')
                else:
                    ops.append('c')
                cpi //= 3
            while(len(ops) < len(operands)-1):
                ops.append('+')
            #print(ops)
            #s='0'*(n-len(s))+s
            res = int(operands[0])
            for j in range(len(ops)):
                if(ops[j] == '*'):
                    res *= operands[j+1]
                elif(ops[j] == '+'):
                    res += operands[j+1]
                elif ops[j] == 'c':
                    res = int(str(res) + str(operands[j+1]))
            if(ans == res):
                sumTot += ans
                #print(s, ans ,operands)
                break;
    print(sumTot)
