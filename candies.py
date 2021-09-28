total = int(input())
for i in range(total):
    n = int(input())
    k = 1
    coefficient = 3
    while n%coefficient != 0:
        k += 1
        coefficient += 2**k
    print(n//coefficient)
