n, m, k = [int(a) for a in input().split()]
friends = 0
soldiers = [0] * (m+1)
for x in range(m+1):
    soldiers[x] = int(input())
Fedor = soldiers[-1]
for x in range(m):
    if len([int(a) for a in bin(Fedor ^ soldiers[x])[2:] if int(a)]) <= k:
        friends += 1
print(friends)