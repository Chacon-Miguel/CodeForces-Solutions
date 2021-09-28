x = int(input())
string = input()
if string.count('A') < len(string)/2:
    print("Danik")
elif string.count("A") > len(string)/2:
    print("Anton")
else:
    print("Friendship")