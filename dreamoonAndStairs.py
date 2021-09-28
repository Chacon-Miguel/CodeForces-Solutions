steps, multiple = [int(a) for a in input().split()]
if multiple > steps:
    print(-1)
elif multiple == steps:
    print(steps)
else:
    moves = steps//2 + steps%2
    if moves%multiple > multiple:
        print(-1)
    else:
        while moves%multiple != 0:
            moves += 1
        print(moves)
