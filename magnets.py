num = int(input())
if num == 1:
    print(1)
else:
    string = ''
    for x in range(num):
        string += input()
    print(1+string.count('00')+string.count('11'))