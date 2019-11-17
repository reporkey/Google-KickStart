T = int(input())
out = ""

for case in range(T):

    N = input()
    C = list(map(int, input().split()))
    C_sorted = []
    h = 0
    hs = ""
    for each in C:
        C_sorted = C_sorted + [each]
        C_sorted.sort(reverse=True)
        while True:
            h += 1
            if h > len(C_sorted) or h > C_sorted[h-1]:
                h -= 1
                hs = hs + " " + str(h)
                break

    out += ("Case #"+str(case+1)+":"+str(hs)+"\n")

print(out)