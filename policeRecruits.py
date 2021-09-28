numb = input()
police = 0
crime = 0
events = [int(a) for a in input().split()]
for event in events:
    if event > 0:
        police += event
    else:
        if police > 0:
            police -= 1
        else:
            crime += 1
print(crime)