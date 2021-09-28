from math import factorial
n = int(input())
def nCr(n, r):
    return factorial(n)//factorial(n-r)//factorial(r)
print(nCr((2*n)-2, n-1))