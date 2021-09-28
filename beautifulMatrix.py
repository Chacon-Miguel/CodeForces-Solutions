arr = []
row = 0
answer = 0
for rows in range(1, 6):
    row = [int(a) for a in input().split()]
    arr.append(row)
    if 1 in row:
        answer = abs(3-(row.index(1)+1))+(abs(3-rows))
print(answer)