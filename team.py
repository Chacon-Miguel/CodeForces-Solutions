accum = 0
problem = 0
for x in range(int(input())):
    problem = [int(a) for a in input().split()]
    if problem.count(1) >= 2:
        accum += 1
print(accum)
    