total = int(input())
numbers = [0] * total
for i in range(total):
    numbers[i] = int(input())
for number in numbers:
    if number%4 == 0:
        print("YES")
        arr = []
        for evens in range(2, (number)+1, 2):
            arr.append(evens)
        for odds in range(1, (number), 2):
            arr.append(odds)
        arr[len(arr)-1] += (number//2)
        for numb in arr:
            print(numb, end=" ")
        print(end = "\n")
    else:
        print("NO")
