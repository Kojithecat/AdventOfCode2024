def count_ways(blocks, word, memo):
    if word in memo:
        return memo[word]
    if word == "":
        return 1  # Only one way to construct an empty word: use zero blocks.

    total_ways = 0
    for b in blocks:
        if word.startswith(b):
            total_ways += count_ways(blocks, word[len(b):], memo)

    memo[word] = total_ways
    return total_ways

blocks = []
words = []

with open("input.txt") as f:
    input = f.read()
    blocks, words = input.split('\n\n')
    blocks = blocks.split(', ')
    words = words.split('\n')

s = 0
for word in words:
    memo = {}
    ways = count_ways(blocks, word, memo)
    s += ways

print(s)