k = int(input())
months = [int(a) for a in input().split()]
months.sort(reverse = True)
totalMonths = 0
if k == 0:
    print(0)
else:
    for month in months:
        k -= month
        totalMonths += 1
        if k <= 0:
            print(totalMonths)
            break
    else:
        print(-1)
