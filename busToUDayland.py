rows = int(input())
bus = []
answer = "NO"
for row in range(rows):
    seats = input()
    if "OO" in seats and answer == "NO":
        seats = seats.replace("OO", "++", 1)
        answer = "YES"
    bus.append(seats)
if answer == "YES":
    print(answer)
    for row in bus:
        print(row)
else:
    print("NO")