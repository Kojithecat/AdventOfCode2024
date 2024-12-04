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
    for i in range(len(text)):
        for j in range(len(text[i])):
            word = "XMAS"
            print(i,j)
            if(j < (len(text[i])-3) and i < (len(text)-3)):
                if word == text[i][j] + text[i+1][j+1] + text[i+2][j+2] + text[i+3][j+3] or word == text[i+3][j+3] + text[i+2][j+2] + text[i+1][j+1] + text[i][j]:
                    s += 1
                    print("UDiag ",i,j)
                
            if(j < (len(text[i])-3) and i >2):
                if word == text[i][j] + text[i-1][j+1] + text[i-2][j+2] + text[i-3][j+3] or word == text[i-3][j+3] + text[i-2][j+2] + text[i-1][j+1] + text[i][j]:
                    s += 1
                    print("LDiag ", i,j)
                
            if(j < len(text[i])-3):
                if word == text[i][j] + text[i][j+1] + text[i][j+2] + text[i][j+3] or word == text[i][j+3] + text[i][j+2] + text[i][j+1] + text[i][j]:
                    s += 1   
                    print("Hori ", i,j)
            if(i < len(text)-3):
                if word == text[i][j] + text[i+1][j] + text[i+2][j] + text[i+3][j] or word == text[i+3][j] + text[i+2][j] + text[i+1][j] + text[i][j]:
                    s += 1
                    print("Vert ", i,j)
    return s


import os

with open("input.txt", 'r') as f:
    sampleText = f.read().split('\n')
    #print(sampleText)
    print(countXMAS(sampleText))



text = read_input(4)


print(countXMAS(text))