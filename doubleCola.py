chars = ['Sheldon', 'Leonard', 'Penny', "Rajesh", "Howard"]
x = int(input())
exponent = 0
if x <= 5:
    print(chars[x-1])
else:
    while (5*(2**exponent)) < x:
        x -= 5*2**exponent
        exponent += 1
    print(chars[x//(2**exponent)])