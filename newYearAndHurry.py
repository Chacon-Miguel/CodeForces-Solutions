problems, time = [int(a) for a in input().split()]
count = 0
timeForProblems = 240-time
for x in range(problems):
    if timeForProblems <= 0:
        break
    timeForProblems -= (count*5)
    count += 1
print(count)