n = int(input())
arr = [int(a) for a in input().split()]
b = [0] * n
c = []
currentP = sum(arr)
for index in range(n):
    if arr[index] == 0:
        b[index] = 1
    else:
        b[index] = -1

for i in range(n):
    for j in range(i, n):
        c.append( currentP + sum(b[i:j+1]))
print(max(c))