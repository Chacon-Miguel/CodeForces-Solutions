n, m = [int(a) for a in input().split()]
color = "#Black&White"
for x in range(n):
    rowOfPixels = input().split()
    if 'C' in rowOfPixels or 'M' in rowOfPixels or 'Y' in rowOfPixels:
        color = "#Color"
print(color)