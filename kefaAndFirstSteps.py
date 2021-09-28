length = int(input())
k = [int(a) for a in input().split()]
segments = []
count = 1
for numb in range(1, length):
    if k[numb] >= k[numb-1]:
        count += 1
    else:
        segments.append(count)
        count = 1
segments.append(count)
print(max(segments))