x = int(input())
word = input().lower()
if x < 26:
    print("NO")
else:
    alphabet = 'qwertyuiopasdfghjklzxcvbnm'
    for letter in alphabet:
        if letter not in word:
            print("NO")
            break
    else:
        print("YES")