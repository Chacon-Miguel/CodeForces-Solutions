s=[int(numb) for numb in input().split()]
total=0
for digit in s:
    total+=digit
if total%5>0 or total == 0:
    print(-1)
else:
    print(total//5)