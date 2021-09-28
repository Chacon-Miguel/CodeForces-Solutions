database = {}
for number in range(int(input())):
    name = input()
    if name not in database:
        print('OK')
        database[name] = 1
    else:
        print(name+str(database[name]))
        database[name] += 1
