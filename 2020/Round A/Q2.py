
def rec(stacks, remainP):
    if stacks != []:
        if remainP > 0:
            return max([stacks[0][i] + rec(stacks[1:], remainP-i) for i in range(min(len(stacks[0]), remainP+1))])
    return 0


T = int(input())

for case in range(T):

    line = input()
    N = int(line.split()[0])
    K = int(line.split()[1])
    P = int(line.split()[2])

    stacks = [] # cumulative list
    for _ in range(N):
        line = input().split()
        temp = [int(each) for each in line][:P]
        s = [0]
        for i in range(len(temp)):
            s.append(s[i] + temp[i])
        stacks.append(s)

    print("Case #" + str(case+1) + ": " + str(rec(stacks, P)))
