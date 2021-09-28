strength, amount = [int(a) for a in input().split()]
dragons = [[int(a) for a in input().split()] for b in range(amount)]
# Sort the dragons by their strengths
dragons.sort(key=lambda x: x[0])
for i in range(amount-1, 0, -1):
    if (dragons[i][0] == dragons[i-1][0]) and (dragons[i][1] > dragons[i-1][1]):
        dragons[i][1], dragons[i-1][1] = dragons[i-1][1], dragons[i][1]
for dragon in dragons:
    if dragon[0] < strength:
        strength += dragon[1]
    else:
        print("NO")
        break
else:
    print("YES")
