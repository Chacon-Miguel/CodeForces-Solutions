from itertools import permutations

totalFlowers = int(input())
flower = sorted([int(a) for a in input().split()])
MaxFlower = max(flower)
MinFlower = min(flower)
MaxMode = 0
MinMode = 0
for x in range(totalFlowers):
    if flower[x] == MinFlower:
        MinMode += 1
    else:
        break
for x in flower[::-1]:
    if x == MaxFlower:
        MaxMode += 1
    else:
        break
answer = permutations(([MaxFlower]*MaxMode) + [MinFlower])