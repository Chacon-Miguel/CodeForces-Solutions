n, m, a, b = [int(a) for a in input().split()]
# Check if the special ticket is cheaper
if m*a < b:
    total = n*a
else:
    total = (n//m)*b
    # Choose between buying a ticket every time or buying a special ticket and not
    # using it fully
    total += min(a*(n%m), b)
print(total)