total, target = map(int, input().split())
portals = [int(a) for a in input().split()]
cell = 1
while True:
    if cell > target:
        print("NO")
        break
    cell += portals[cell-1]
    if cell == target:
        print("YES")
        break
    