n = [4, 7, 44, 47, 74, 77, 444, 447, 474, 477, 744, 747, 774, 777]
i = input()
for a in n:
    if i.count('4') + i.count('7') == a:
        print("YES")
        break
else:
    print('NO')