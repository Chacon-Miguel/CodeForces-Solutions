count = 0
coord = int(input())
for x in range(5, 0, -1):
    count += coord//x
    coord -= (coord//x*x)
print(count)