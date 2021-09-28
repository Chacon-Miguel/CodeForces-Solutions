Length, Sum = [int(a) for a in input().split()]
if (Sum == 0):
    if (Length == 1):
        print(0, 0)
    else:
        print(-1, -1)
elif (Sum > Length*9):
    print(-1, -1)
else:
    MaxList = [0] * Length
    MinList = [0] * Length
    Max = ""
    Min = ""
    SumMin = Sum-1
    SumMax = Sum
    for digit in range(Length-1, 0, -1):
        if (SumMin > 9):
            MinList[digit] = 9
            SumMin -= 9
        else:
            MinList[digit] = SumMin
            SumMin = 0
    MinList[0] = SumMin + 1
    for digit in range(Length):
        if SumMax >= 9:
            MaxList[digit] = 9
            SumMax -= 9
        else:
            MaxList[digit] = SumMax
            SumMax = 0
    for x in range(Length):
        Min += str(MinList[x])
        Max += str(MaxList[x])
    print(Min, Max)