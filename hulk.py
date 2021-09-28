x = int(input())
odds = "I hate that"
evens = 'I love that'
string = [odds]*x
if x != 1:
    for word in range(1, x, 2):
        string[word] = evens
string = ' '.join(string)
print(string[:-4] + 'it')