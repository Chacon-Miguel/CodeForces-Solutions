last, rows = [int(a) for a in input().split()]
Rows = [0] * rows
Dict = {}
for x in range(rows):
    Pair = input().split()
    if len(Pair[0]) > len(Pair[1]):
        Min = Pair[1]
    else:
        Min = Pair[0]
    Dict[Pair[0]] = Min
    Dict[Pair[1]] = Min
Words = input().split()
for word in Words:
    print(Dict[word], end = " ")