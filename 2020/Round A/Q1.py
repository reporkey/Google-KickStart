T = int(input())
out = ""

for case in range(T):

    line = input()
    N = int(line.split()[0])
    B = int(line.split()[1])

    line = input()
    texts = line.split()
    price = [int(each) for each in texts if int(each) <= B]
    price = sorted(price)

    num = 0
    for each in price:
        if (B - each) >= 0:
            B -= each
            num += 1
        else:
            break

    out += "Case #" + str(case+1) + ": " + str(num) + "\n"

print(out)
