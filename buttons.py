buttons = int(input())
moves = 0
for x in range(1, buttons):
    moves += (buttons-x)*x
print(moves+buttons)
