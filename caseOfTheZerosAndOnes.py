n = int(input())
string = input()
zeros = 0
ones = 0
for numb in string:
    if numb == "1":
        ones += 1
    else:
        zeros += 1
print(n-(2*min(ones, zeros)))