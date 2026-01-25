def climbStairs(n: int) -> int:
    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 1
    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]

def climbStairs2(n: int) -> int:
    if n <= 1:
        return n
    prev, prev2 = 1, 1
    cur = 0
    for i in range(2, n+1):
        cur = prev + prev2
        prev2 = prev
        prev = cur

    return cur