d1, d2, d3 = [int(a) for a in input().split()]
print(min(2*(d1+d2), (d1+d2+d3), 2*(d1+d3), 2*(d2+d3)))
