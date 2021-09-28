numbers = int(input())
a = [0] * numbers
b = [0] * numbers
for numb in range(numbers):
    a[numb], b[numb] = [int(a) for a in input().split()]
for i in range(numbers):
    if a[i]%b[i] == 0:
        print(0)
    else:
        print(b[i] - a[i]%b[i])