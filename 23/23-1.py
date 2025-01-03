from collections import defaultdict

with open("input.txt") as f:
    input = f.read().split('\n')
    connections = defaultdict(list)
    toCheckServers = []
    checkedServers = []
    for con in input:
        s1,s2 = con.split('-')
        connections[s1].append(s2)
        connections[s2].append(s1)
        if s1 not in toCheckServers:
            toCheckServers.append(s1)
        if s2 not in toCheckServers:
            toCheckServers.append(s2)
     
    s = 0   
    for s1 in toCheckServers:
        for s2 in connections[s1]:
            if s2 not in checkedServers:
                for s3 in connections[s2]:
                    if(s3 not in checkedServers and s3 in connections[s1] and (s1[0] == 't' or s2[0] == 't' or s3[0] == 't')):
                        s+= 1
                        print(s1, s2, s3)
                    checkedServers.append(s1)


     
    
    print(s)