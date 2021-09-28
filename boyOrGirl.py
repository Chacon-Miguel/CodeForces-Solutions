username = list(input())
distinctChars = []
for char in username:
    if char not in distinctChars:
        distinctChars.append(char)
if len(distinctChars)%2:
    print("IGNORE HIM!")
else:
    print("CHAT WITH HER!")