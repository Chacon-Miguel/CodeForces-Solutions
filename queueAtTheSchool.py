numbOfKids, seconds = [int(a) for a in input().split()]
order = list(input())
count = 1
for second in range(seconds):
    while count < numbOfKids:
        if order[count] == "G" and order[count-1] == "B":
            order[count], order[count-1] = "B", "G"
            count += 1
        count += 1
    count = 1
print(''.join(order))