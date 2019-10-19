T = int(input())
out = ""

for case in range(T):

    V = int(input())
    B = [int(each) for each in input().split()]


    out += ("Case #"+str(case+1)+": "+str(total)+"\n")

print(out)