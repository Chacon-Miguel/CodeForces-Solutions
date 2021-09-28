b = int(input())
boys = [int(a) for a in input().split()]
g = int(input())
girls = [int(a) for a in input().split()]
boys.sort()
girls.sort()
total = 0
for index in range(b):
    for index2 in range(g):
        if abs(boys[index] -  girls[index2]) <= 1:
            girls[index2] = 1000
            total += 1
            break
print(total)
