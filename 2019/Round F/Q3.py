T = int(input())
out = ""

for case in range(T):

    V = int(input())
    B = [int(each) for each in input().split()]
    L = [False for _ in range(V)]
    roads = [[] for _ in range(V)]

    for _ in range(V - 1):
        lines = [int(each) for each in input().split()]
        roads[lines[0]-1].append(lines[1]-1)
        roads[lines[1]-1].append(lines[0]-1)

    # light up if all connections are positive
    for v, connections in enumerate(roads):
        allPos = True
        if B[v] >= 0:
            for connect in connections:
                if B[connect] < 0:
                    allPos = False
                    break
        else:
            allPos = False
        if allPos:
            L[v] = True
            for connect in connections:
                L[connect] = True

    while True:
        toLight = []
        reward = 0
        for v, connections in enumerate(roads):
            # non lighted sum
            r = 0
            if not L[v]:
                r += B[v]
            for connect in connections:
                if not L[connect]:
                    r += B[connect]
            # compare
            if r > reward:
                toLight = [v] + connections
                reward = r
            elif r == reward:
                toLight.append(v)
                for each in connections:
                    toLight.append(each)

        if reward > 0:
            for v in toLight:
                L[v] = True
        else:
            break

    total = 0
    for i, isLight in enumerate(L):
        if isLight:
            total += B[i]

    out += ("Case #"+str(case+1)+": "+str(total)+"\n")

print(out)