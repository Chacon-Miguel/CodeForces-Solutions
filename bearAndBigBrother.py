bear, bigBrother = [int(a) for a in input().split()]
count = 0
while bear <= bigBrother:
    bear *= 3
    bigBrother *=2
    count += 1
print(count)