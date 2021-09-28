cardT = input()
rank, suit = cardT[0], cardT[1]
cards = [a for a in input().split()]
for card in cards:
    if card[0] == rank or card[1] == suit:
        print("YES")
        break
else:
    print("NO")