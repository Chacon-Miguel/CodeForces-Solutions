array = []
maximum = 0
for lists in range(int(input())):
    array.append([int(a) for a in input().split()])
for lists in range(len(array)):
    for elements in array[lists]:
        if maximum < elements:
            maximum = elements
print(array.index(maximum))