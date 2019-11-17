"""
Wrongly implemented, misunderstand the question.

The rule for testing 11 is 0 modulo by 11 of alternative digit sum i.e. +-+-+-+
But this implementation is 0 modulo of digit sum i.e. ++++++
This rule works for testing number 3.

"""

# return false if cannot find a combo
def findCombo(a, below, target):
    if target == 0:
        return a[:below-1]
    if below == 0:
        return False
    nextInt = below-1
    multiplier = a[nextInt-1] if a[nextInt-1] < 11 else 11
    while True:
        result = findCombo(a, nextInt, (target + nextInt * multiplier) % 11)
        if result is False:
            multiplier -= 1
            if multiplier < 0: # no solution
                return False
        else:
            break

    return result + [a[nextInt-1] - multiplier]


# print(findCombo([1,1,1,1,1,1,1,1,1], 10, 3))

T = int(input())
out = ""

for case in range(T):
    A = list(map(int, input().split()))
    flag = True

    for digit in reversed(range(10)):
        A[digit-1] = A[digit-1] % 11
        result = findCombo(A, digit, A[digit-1]*digit)
        if result is False:
            flag = False
            break
        else:
            A = result

    if flag:
        out += ("Case #"+str(case+1)+": YES\n")
    else:
        out += ("Case #"+str(case+1)+": NO\n")

print(out)
