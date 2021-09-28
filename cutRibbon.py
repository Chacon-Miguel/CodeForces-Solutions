def f(n):
    # Build maximum number of pieces for
    #length 1 upto n in bottom up manner
    dp = [float("-inf")] * (n + 1)
 
    # Base Case
    dp[0] = 0
 
    # dp[i] gives maximum number of pieces that can
    # be obtained by cutting ribbon of length  i into pieces
    # of length a, b or c
    # dp[i] = -inf if it is not possible to cut the ribbon into pieces
    for i in range(1, n + 1):
        for length in l:
            # Cut into pieces if only we dont have negative length of ribbon
            if i - length >= 0:
                dp[i] = max(dp[i], 1 + dp[i - length])
    # return maximum number of pieces possible for ribbon with length n
    return dp[n]
 
 
l = list(map(int, input().split()))
n, l = l[0], l[1:]
print(f(n))