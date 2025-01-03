def validword(blocks, word, memo):
    if word in memo:
        return memo[word]
    if word == "":
        return True
    for b in blocks:
        if word.startswith(b):
            # Recursively check for the rest of the word
            if validword(blocks, word[len(b):], memo):
                memo[word] = True
                return True
    memo[word] = False
    return False

blocks = []
words = []

with open("input.txt") as f:
    input = f.read()
    blocks, words = input.split('\n\n')
    blocks = blocks.split(', ')
    words = words.split('\n')

s = 0
memo = {}
for word in words:
    if validword(blocks, word, memo):
        s += 1
        print(word)

print(s)