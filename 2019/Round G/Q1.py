T = int(input())
out = ""

for case in range(T):

    N, M, Q = input().split()
    P = input().split()
    R = input().split()

    total = 0
    for i in range(int(Q)):
        total += int(int(N) / int(R[i]))
    for torn in P:
        for r in R:
            if int(torn) % int(r) == 0:
                total -= 1

    out += ("Case #"+str(case+1)+": "+str(total)+"\n")

print(out)