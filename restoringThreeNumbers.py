numbs = [int(a) for a in input().split()]
ABC = sum(numbs)//3
results = [0] * 4
for index in range(4):
    results[index] = ABC - numbs[index]
for numb in results:
    if numb == 0:
        continue
    else:
        print(numb, end=' ')