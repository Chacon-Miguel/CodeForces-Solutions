num = input()
seive = [a for a in range(1000) if '4' in str(a) or '7' in str(a)  ]
print(seive)
if not(int(num)%4) or not(int(num)%7):
    print("YES")
elif '4' in num or '7' in num:
    for digit in '1235689':
        if digit in num:
            print("NO")
            break
    else:
        print("YES")
else:
    print("NO")