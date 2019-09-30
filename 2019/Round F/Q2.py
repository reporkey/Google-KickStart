T = int(input())

for case in range(T):

    line = input()
    line = line.split()
    N = int(line[0])
    S = int(line[1])

    employees = []
    for _ in range(N):
        line = input().split()
        C = int(line[0])
        employees.append([int(each) for each in line[1:]])

    motor = 0
    for i in range(len(employees)):
        e1 = employees[i]
        for j in range(len(employees)):
            e2 = employees[j]
            if i != j:
                for s in e1:
                    if s not in e2:
                        motor += 1
                        break
    print("Case #" + str(case+1) + ": " + str(motor))
