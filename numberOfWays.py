n = int(input())
arr = [int(a) for a in input().split()]
thirds = sum(arr)/3
if n < 3:
    print(0)
elif n == 3:
    if sum(arr) == arr[0]*3:
        print(1)
    else:
        print(0)
else:
    answer = 0
    count = 0
    total = 0
    for index in range(n-1):
        total += arr[index]
        if total == 2 * thirds:
            answer += count
        if total == thirds:
            count += 1
    print(answer)

