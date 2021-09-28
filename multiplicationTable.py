from functools import reduce
n, x = [int(a) for a in input().split()]
if n == 1:
    if x == 1:
        print(1)
    else:
        print(0)
elif x == 1:
    print(1)
else:
    total = 0
    def factors(n):    
        return set(reduce(list.__add__, 
                    ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))
    factorsX = sorted(factors(x))
    limit = len(factorsX)//2-1
    if len(factorsX)%2:
        limit += 1
        if factorsX[(len(factorsX))//2] <= n:
            total += 1
    for factor in range(len(factorsX)-1, limit, -1):
        if factorsX[factor] <= n:
            total += 2
    print(total)
