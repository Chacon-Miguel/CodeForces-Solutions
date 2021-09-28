k = list(range(1, int(input())+1))
x = [int(a) for a in input().split()]
y = [int(a) for a in input().split()]
for num in k:
    if not (num in x or num in y):
        print("Oh, my keyboard!")
        break
else:
    print("I become the guy.")