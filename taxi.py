numb = input()
groups = [int(a) for a in input().split()]
count = groups.count(4) + groups.count(3)
singles = groups.count(1) - groups.count(3)
if singles <= 0:
    singles = 0
count += groups.count(2)*2//4
singles += (groups.count(2)*2)%4
count += singles//4
if singles%4:
    count += 1
print(count)