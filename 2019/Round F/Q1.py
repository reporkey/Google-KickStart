

T = int(input())
out = ""

for i in range(T):

    line = input()
    num = line.split()
    N = int(num[0])
    K = int(num[1])

    line = input()
    texts = line.split()
    nums = [int(each) for each in texts]

    change = 0

    while True:
        # check if happy
        diff = 0
        for j in range(N - 1):
            if nums[j + 1] != nums[j]:
                diff += 1
        if diff <= K:
            out += ("Case #" + str(i+1) + ": " + str(change) + "\n")
            break

        # not happy, rebuild

        # find diff section with shortest length
        shortest = 100
        start = 0
        end = 0
        length = 0
        e = nums[0]
        for j in range(len(nums)):
            each = nums[j]
            length += 1
            if each != e:
                if j == len(nums):
                    if length < shortest:
                        shortest = 1
                        end = len(nums)
                else:
                    if length < shortest:
                        shortest = length
                        end = j-1
                    elif length == shortest: # high priority if left = right
                        if nums[end] == nums[j]:
                            shortest = length
                            end = j - 1
                length = 0
                e = each
        # start
        j = end
        same = nums[end]
        while j >= 0:
            if nums[j] != same:
                start = j + 1
                break
            j -= 1

        left = 0
        right = 0
        # left
        if start > 0:
            j = start-1
            same = nums[j]
            while j >= 0:
                if nums[j] == same:
                    left += 1
                else:
                    break
                j -= 1
        # right
        if end < len(nums)-1:
            j = end+1
            same = nums[j]
            while j < len(nums)-1:
                if nums[j] == same:
                    right += 1
                else:
                    break
                j += 1

        # rebuild
        if left < right:    # n becomes N+1; 1122333
            nums[end] = nums[end+1]
        else:               # left > right
            nums[start] = nums[start - 1]
        change += 1
        if change > 5:
            break
print(out)