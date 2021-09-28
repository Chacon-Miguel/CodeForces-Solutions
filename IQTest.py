a = int(input())
k = [int(a) for a in input().split()]
countEven = 0
countOdd = 0
for numb in k:
    if numb%2:
        countOdd += 1
        lastOdd = numb
    else:
        countEven += 1
        lastEven = numb
if countEven == 1:
    print(k.index(lastEven)+1)
else:
    print(k.index(lastOdd)+1)