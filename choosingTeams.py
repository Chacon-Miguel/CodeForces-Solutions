# n is the number of students
# k is the number of times players r needed to play
n, k = [int(a) for a in input().split()]
# List that holds how many times each player has played
PlayedGames = [int(a) for a in input().split()]
# assume all players are eligible
eligiblePlayers = n
# iterate through the PlayedGames list
for index in range(n):
    # If the number of times the player has played is greater
    # than the difference between the max number of times allowed
    # to play and k, then remove one from valid players
    if PlayedGames[index] > (5-k):
        eligiblePlayers -= 1
# if there are less than three eligible players, no team can be formed
if eligiblePlayers < 3:
    print(0)
# since every player can only play once, use integer division to find the
# total number of teams that can be formed
else:
    print(eligiblePlayers//3)