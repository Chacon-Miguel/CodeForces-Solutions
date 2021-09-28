def Sorted(arr):
    return arr[0]
n = int(input())
Dict = [0] * n
for numb in range(n):
    Dict[numb] = [int(a) for a in input().split()]
Dict = sorted(Dict,key=Sorted)
inOrder = True
for x in range(1, n):
    if Dict[x][1] < Dict[x-1][1]:
        inOrder = False
if inOrder:
    print("Poor Alex")
else:
    print("Happy Alex")
    