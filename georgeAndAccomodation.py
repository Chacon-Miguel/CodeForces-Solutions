k, i, count = 0, 0, 0
for x in range(int(input())):
    k, i = [int(a) for a in input().split()]
    if i-k >= 2:
        count += 1
print(count)