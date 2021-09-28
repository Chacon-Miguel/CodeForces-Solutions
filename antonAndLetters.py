Set = input()[1:-1]
Set = set(Set.split(', '))
if '' in Set:
    print(len(Set)-1)
else:
    print(len(Set))