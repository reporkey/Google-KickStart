def test(A, k, M):
    ans = 0
    for a in A:
        ans += int(a) ^ k
        if ans > int(M):
            return False

    return True


T = int(input())
out = ""

for case in range(T):

    N, M = input().split()
    A = input().split()
    A = [int(a) for a in A]

    k_low = max(A)
    k_high = max(A) * 4

    k_low_pass = k_low

    while not (k_low == k_high == k_low_pass):
        if test(A, k_low, M) and test(A, k_high, M): # all pass
            k_low = k_high
            k_high = int(k_high * 2)
            k_low_pass = k_low

        elif test(A, k_low, M) and not test(A, k_high, M): # low pass, high not pass
            k_low_pass = k_low
            k_low = int(k_low + (k_high - k_low) / 2)

        else: # all not pass
            k_high = k_low
            k_low = int(k_low + (k_low - k_low_pass) / 2)

        if k_high == 0:
            k_low_pass = -1
            break


    out += ("Case #"+str(case+1)+": "+str(k_low_pass)+"\n")

print(out)


