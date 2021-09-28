n, m = [int(a) for a in input().split()]
List = ["#"*m]
right = True
for x in range(n):
    if right:
        List.append('.'*(m-1)+"#")
        right = False
    else:
        List.append("#"+'.'*(m-1))
        right = True
    List.append('#'*m)
for i in List[:n]:
    print(i)