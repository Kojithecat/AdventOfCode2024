import os

with open("input.txt", 'r') as f:
    sumTot = 0
    list = f.read().split('\n')[:-1]
    print(list)

    for line in list:
        ans = int(line.split(':')[0])
        operands = [int(x) for x in line.split(':')[1].strip().split(' ')]
        print(ans, operands)
        n = 2** (len(operands))
        for i in range(n):
            ops = ['+' if (i >> j) & 1 == 0 else '*' for j in range(len(operands)-1)]
            #print(s)
            #s='0'*(n-len(s))+s
            res = int(operands[0])
            for j in range(len(ops)):
                if(ops[j] == '*'):
                    res *= operands[j+1]
                elif(ops[j] == '+'):
                    res += operands[j+1]
                else:
                    print("WTF")
            if(ans == res):
                sumTot += ans
                #print(s, ans ,operands)
                break;
    print(sumTot)
