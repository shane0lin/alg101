# 338 counting bits
# https://leetcode.com/problems/counting-bits/discuss/79539/Three-solutions-with-one-short-and-simple-solution
def countBits(num):
    # sol 1
    # res = [0]
    # while len(res) <= num:
    #     res += [i + 1 for i in res]
    # return res[:num+1]

    # sol2
    # 当i为奇数，它比i-1在最低位上多1，其包含1的个数是i-1包含1的个数+1（i/2包含1的个数与i-1包含1的个数相同）

    # 若i为偶数，其最低位上是0，包含1的个数为i右移一位包含1的个数，即为i/2包含1的个数


    dp = [0] * (num + 1)
    for i in range(1, num + 1):
        dp[i] = dp[i >> 1] + (i & 1)
    return dp


print(countBits(5))
print(countBits(2))
print(countBits(1))