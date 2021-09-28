bills = [100, 20, 10, 5, 1]
withdrawl = int(input())
minBills = 0
for bill in bills:
    minBills += withdrawl//bill
    withdrawl -= (withdrawl//bill)*bill
print(minBills)