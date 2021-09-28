keyboard = " qwertyuiopasdfghjkl;zxcvbnm,./"
Dict = {}
for i in range(31):
    Dict[keyboard[i]] = i
    Dict[i] = keyboard[i]
L_or_R = input()
message = input()
if L_or_R == 'L':
    for char in message:
        print(Dict[Dict[char]+1], end='')
else:
    for char in message:
        print(Dict[Dict[char]-1], end='')