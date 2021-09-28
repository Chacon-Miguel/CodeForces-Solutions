x = int(input())
xBinary = str(bin(x))
print(xBinary)
total = 0
for x in xBinary:
    if x == '1':
        total += 1
print(total)