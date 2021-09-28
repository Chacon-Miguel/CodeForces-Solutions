total = int(input())
numbs = [0]*total
for i in range(total):
    numbs[i] = int(input())
for numb in numbs:
    if numb%2 == 0:
        print((numb-2)//2)
    else:
        print(numb//2)