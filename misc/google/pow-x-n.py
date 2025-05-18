# Pow(x, n)
# https://leetcode.com/problems/powx-n/
def myPow(x, n):
    # if n == 0:
    #     return 1
    # if n < 0:
    #     return 1 / myPow(x, -n)
    # if n % 2 == 0:
    #     return myPow(x * x, n // 2)
    # else:
    #     return x * myPow(x, n - 1)

    # sol2
    if n == 0:
        return 1
    if n < 0:
        x, n = 1 / x, -n
    
    rst = 1
    while n:
        if n & 1:
            rst *= x
        x *= x
        n >>= 1
    return rst

print(myPow(2.00000, 10)) # 1024
print(myPow(2.10000, 3)) # 9.261
print(myPow(1, 0))