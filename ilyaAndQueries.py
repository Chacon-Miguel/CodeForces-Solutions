string = input()
Length = len(string)
arr = [0]*Length
queries = int(input())
amount = 0
for char in range(1, Length):
    if string[char] == string[char-1]:
        amount += 1
    arr[char] = amount
Dict = {}
for query in range(queries):
    Dict[query] = [int(a) for a in input().split()]
for query in range(queries):
    print(arr[Dict[query][1]-1]-arr[Dict[query][0]-1])
