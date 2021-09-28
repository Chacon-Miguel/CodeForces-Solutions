year = int(input())+1
while True:
    for char in str(year):
        if str(year).count(char) > 1:
            break
    else:
        break
    year += 1
print(year)