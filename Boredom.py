x = int(input())
a = [int(a) for a in input().split()]
modes = [0]*(100001)
dp = [0] * (100001)
for numb in a:
    modes[numb] += 1
dp[1] = modes[1]
for numb in range(2, max(a)+1):
    dp[numb] = max(dp[numb-1], dp[numb-2]+modes[numb]*numb)
print(dp[max(a)])