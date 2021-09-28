x = int(input())
home = []
away = []
for number in range(x):
    game = [int(a) for a in input().split()]
    home.append(game[0])
    away.append(game[1])
answer = 0
for numb in range(1, 101):
    answer += (home.count(numb)*away.count(numb))
print(answer)