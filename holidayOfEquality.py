total = int(input())
wealth = [int(a) for a in input().split()]
"""
The king cannot take away money so the richest guy gets to keep all of his money.
To make everyone equal, we have to make everyone have the same as the richest guy
"""
# Find the richest person
Max = max(wealth)
# Counter variable to keep track of how much is needed
welfare = 0
# Iterate through every person
for numb in wealth:
    # Determine the amount needed to make that person equal to the richest person and add it to welfare
    welfare += (Max-numb)
# Display the welfare number
print(welfare)
