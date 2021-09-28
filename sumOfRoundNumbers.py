total = int(input())
for i in range(total):
    numb = input()[::-1]
    roundNumbs = []
    for digit in range(len(numb)):
        if numb[digit] != "0":
            roundNumbs.append( numb[digit] + "0"*digit )
    print(len(roundNumbs))
    for number in roundNumbs:
        print(number, end=" ")
    print(end= "\n")
