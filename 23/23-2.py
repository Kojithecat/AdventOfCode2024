from collections import defaultdict
from itertools import product

connections = defaultdict(list)
toCheckServers = []
checkedServers = []

with open("input.txt") as f:
    input = f.read().split('\n')

    for con in input:
        print(con)
        s1,s2 = con.split('-')
        connections[s1].append(s2)
        connections[s2].append(s1)
        if s1 not in toCheckServers:
            toCheckServers.append(s1)
        if s2 not in toCheckServers:
            toCheckServers.append(s2)
     
     

def isClique(servers):
    for i in servers:
        for j in servers:
            if i == j:
                continue
            if i not in connections[j]:
                return False
    return True

bigClique = []

for node in toCheckServers:
    nbrs = connections[node]
    for mask in product((False, True), repeat=len(nbrs)):
        nodes = [node]
        for i, x in enumerate(mask):
            if x:
                nodes.append(nbrs[i])
        if len(nodes) > len(bigClique) and isClique(nodes):
            bigClique = nodes

print(len(bigClique))
print(",".join(sorted(bigClique)))
        