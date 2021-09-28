t = int(input())
angles = {}
for angle in range(1, 180):
    angles[angle] = -360/(angle-180)
testCases = []
for x in range(t):
    testCases.append(int(input()))
for x in testCases:
    if angles[x] == int(angles[x]):
        print("YES")
    else:
        print("NO")