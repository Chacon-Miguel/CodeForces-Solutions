n, m = [int(a) for a in input().split()]
puzzles = [int(b) for b in input().split()]
puzzles.sort()
Min = max(puzzles)
for x in range(0, m-n+1):
    if max(puzzles[x:x+n]) - min(puzzles[x:x+n]) < Min:
        Min = max(puzzles[x:x+n]) - min(puzzles[x:x+n])
print(Min)