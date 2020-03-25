
def rec(diff, k):
    if k == 0:
        return diff[0]
    if k > 0:
        result = []
        for i in range(1, k+1):
            new = divide(diff[0], i)
            l = diff[1:] + new
            l.sort(reverse=True)
            result.append(rec(l, k-i))
            # print(diff, i, k, l)
        return min(result)

T = int(input())

def divide(n, k):
    k += 1
    return [n//k] * (k-1) + [n//k + n%k]

for case in range(T):

    line = input()
    N = int(line.split()[0])
    K = int(line.split()[1])
    line = input().split()
    M = [int(each) for each in line]
    diff = [M[i+1]-M[i] for i in range(N-1)]
    diff.sort(reverse=True)


    print("Case #"+str(case+1)+": "+str(rec(diff, K))+"\n")
