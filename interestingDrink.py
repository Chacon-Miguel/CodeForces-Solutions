# total number of stores
n = int(input())
# the prices of each store
shops = [int(a) for a in input().split()]
# shop with the highest price
HighestP = max(shops)
# make an array money where the index is the amount of stores that have that price. 
# For instance if money[2] = 2, then the person can buy in 2 stores with 2 coins. 
money = [0] * (HighestP+1)
# For every price given, add one to that index. Saves time by avoiding sorting the list
for shop in shops:
    money[shop] += 1
# To make the array accurate, make the next value i equal to i + (i-1)
for i in range(1, HighestP+1):
    money[i] += money[i-1] 
# Get the number of days the person is going to spend money 
days = int(input())
# Make array as large as the amount of days
results = [0]*days
# For every day given...
for day in range(days):
    # Accept the amount of money that's going to be spent on that day
    m = int(input())
    # If it's greater than the highest price, you can just return the greatest value in the array
    if m >= HighestP:
        results[day] = money[HighestP]
    # Otherwise, just get the value from the money array
    else:
        results[day] = money[m]
# Display results. 
for numb in results:
    print(numb)
