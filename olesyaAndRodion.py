n, t = [int(a) for a in input().split()]
if n == 1 and t == 10:
    print(-1)
elif t == 10:
    print(t*10**(n-2))
else:
    print(t*10**(n-1))