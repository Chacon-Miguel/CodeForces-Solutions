wheels = int(input())
wheel = "01234567890123456789"
originalPos = input()
combination = input()
moves = 0
for index in range(wheels):
    if int(originalPos[index]) < int(combination[index]):
        moves += min(abs( wheel.find(originalPos[index]) - wheel.find(combination[index]) ), abs(wheel.rfind(originalPos[index]) - wheel.find(combination[index])))
    else:
        moves += min(abs( wheel.find(combination[index]) - wheel.find(originalPos[index]) ), abs(wheel.rfind(combination[index]) - wheel.find(originalPos[index])))
print(moves)
