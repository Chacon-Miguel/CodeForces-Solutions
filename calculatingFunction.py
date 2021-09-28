x = int(input())
if x%2:
    print(((x//2)*((x//2)+1))-(x//2+1)**2)
else:
    print(((x//2)*((x//2)+1))-(x//2)**2)