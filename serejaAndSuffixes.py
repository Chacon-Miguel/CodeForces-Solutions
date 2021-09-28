n, m = [int(a) for a in input().split()]
arr = [int(a) for a in input().split()]
Dict = {}
Dict[n-1] = 1
Set = set()
Set.add(arr[-1])
Len = 1
for index in range(n-2, 0, -1):
    if arr[index] in Set:
        Dict[index] = Len
    else:
        Set.add(arr[index])
        Len += 1
        Dict[index] = Len
Dict[0] = len(set(arr))
for numb in range(m):
    print(Dict[int(input())-1])