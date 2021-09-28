accum = 0
letters = int(input())
sequence = list(input())
for colors in range(1, letters):
    if sequence[colors] == sequence[colors-1]:
        accum += 1
print(accum)