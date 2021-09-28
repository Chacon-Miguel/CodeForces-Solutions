x = int(input())
fractions = (sum([int(a)/100 for a in input().split()])/x)*100
print(fractions)