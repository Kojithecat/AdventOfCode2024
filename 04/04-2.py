def read_input(day):
    import urllib.request as urllib2
    opener = urllib2.build_opener()
    opener.addheaders.append(('Cookie', 'session=53616c7465645f5f369814b3a0a80177101731d01a65933ab8b1b0f7b0a041791aa608e58bdd2e69e2042453c16d1346e10b941e1c018ddf93ec7bf75647cf71'))
    response = opener.open(f"https://www.adventofcode.com/2024/day/{day}/input")
    content = response.readlines()
    input = []
    for line in content:
        input.append(str(line.decode("utf-8")).replace("\n", ""))
    return input

def countXMAS(text):
    s = 0
    for i in range(1,len(text)-1):
        for j in range(1,len(text[i])-1):
            if(text[i][j] == 'A'):
                if((text[i+1][j+1] == 'M') and (text[i-1][j-1] == 'S') or ((text[i+1][j+1] == 'S') and (text[i-1][j-1] == 'M')))  and ((text[i-1][j+1] == 'M') and (text[i+1][j-1] == 'S') or ((text[i-1][j+1] == 'S') and (text[i+1][j-1] == 'M'))):     
                    print(i,j)
                    s += 1
    return s


import os

with open("input.txt", 'r') as f:
    sampleText = f.read().split('\n')
    #print(sampleText)
    print(countXMAS(sampleText))



text = read_input(4)


print(countXMAS(text))