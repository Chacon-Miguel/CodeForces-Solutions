calories = [int(a) for a in input().split()]
Dict = {}
caloriesBurnt = 0
for x in "1234":
    Dict[x] = calories[int(x)-1]
for i in input():
    caloriesBurnt += Dict[i]
print(caloriesBurnt)
