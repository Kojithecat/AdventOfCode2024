import os
import copy

def countScore(map, y, x):
    seenMap = copy.deepcopy(map)
    score = searchNextStep(map, 1, y, x)
    print(score)
    return score


def searchNextStep(map, nextNum, y, x):
    score = 0
    if str(nextNum) == '10':
        return 1
    if y+1 < len(map) and map[y+1][x] == str(nextNum):
        score += searchNextStep(map, nextNum +1, y+1, x)
    if x+1 < len(map[0]) and map[y][x+1] == str(nextNum):
        score += searchNextStep(map, nextNum +1, y, x+1)
    if y-1 >= 0 and map[y-1][x] == str(nextNum):
        score += searchNextStep(map, nextNum +1, y-1, x)
    if x-1 >= 0 and map[y][x-1] == str(nextNum):
        score += searchNextStep(map, nextNum +1, y, x-1)
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