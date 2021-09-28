people = list(input() + input())
disorder = list(input())
people.sort()
disorder.sort()
if people == disorder:
    print("YES")
else:
    print("NO")