vowels = ['a', 'e', 'i', 'o', 'u', 'y']
word = list(input().lower())
for letter in vowels:
    if letter in word:
        for vowel in range(word.count(letter)):
            word.remove(letter)
for index in range(0, len(word)*2, 2):
    word.insert(index, '.')
print(''.join(word))