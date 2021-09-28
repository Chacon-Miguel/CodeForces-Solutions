a, b, n = [int(a) for a in input().split()]
player = 0
def gcd(a, b):
    if a == 0 or b == 0:
        return 0
    elif a > b:
        if a%b == 0:
            return b
        return 1
    else:
        if b%a == 0:
            return a
        return 1
while n > 0:
    GCD = gcd(a, n)
    if GCD < n:
        n-= GCD
    else:
        print(0)
        break
    player += 1
    GCD = gcd(b, n)
    if GCD < n:
        n -= GCD
    else:
        print(1)
        break
    player -= 1