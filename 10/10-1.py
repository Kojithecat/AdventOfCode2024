import os
import copy

def countScore(map, y, x):
    seenMap = copy.deepcopy(map)
    score = searchNextStep(map, 1, y, x, seenMap)
    print(score)
    return score


def searchNextStep(map, nextNum, y, x, seenMap):
    score = 0
    if str(nextNum) == '10' and seenMap[y][x] != 'v':
        seenMap[y] = seenMap[y][:x] +'v' + seenMap[y][x+1:]
        return 1
    if y+1 < len(map) and map[y+1][x] == str(nextNum):
        score += searchNextStep(map, nextNum +1, y+1, x, seenMap)
    if x+1 < len(map[0]) and map[y][x+1] == str(nextNum):
        score += searchNextStep(map, nextNum +1, y, x+1, seenMap)
    if y-1 >= 0 and map[y-1][x] == str(nextNum):
        score += searchNextStep(map, nextNum +1, y-1, x, seenMap)
    if x-1 >= 0 and map[y][x-1] == str(nextNum):
        score += searchNextStep(map, nextNum +1, y, x-1, seenMap)
    return score

with open("input.txt", 'r') as f:
    sampleText = f.read().split("\n")
    
    print(sampleText)
    
    score = 0
    
    for y in range(len(sampleText)):
        for x in range(len(sampleText[y])):
            if(sampleText[y][x] == '0'):
                score += countScore(sampleText, y, x)
    
    
    print(score)