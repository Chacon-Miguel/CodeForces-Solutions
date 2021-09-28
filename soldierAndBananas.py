k, n, w = [int(a) for a in input().split()]
if k < n and :
    print(0)
else:
    total = 0
    for x in range(1, w+1):
        total += (k*x)
    print(total-n)
