word = input()
if len(word) == 1 and not word[0].isupper():
    print(word.upper())
elif not word[0].isupper() and word[1:].isupper():
    print(word.swapcase())
elif word.isupper():
    print(word.lower())
else:
    print(word)