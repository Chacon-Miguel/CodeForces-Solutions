mPoints = 0
cPoints = 0
for round in range(int(input())):
    m, c = [int(a) for a in input().split()]
    if m > c:
        mPoints += 1
    elif c > m:
        cPoints += 1
if mPoints > cPoints:
    print("Mishka")
elif cPoints > mPoints:
    print("Chris")
else:
    print("Friendship is magic!^^")