# You are climbing a staircase. It takes n steps to reach the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

def climbStairs(self, n: int) -> int:
    # sol 1
    # if n == 1:
    #     return 1
    # if n == 2:
    #     return 2
    # dp = [0] * (n+1)
    # dp[1] = 1
    # dp[2] = 2
    # for i in range(3, n+1):
    #     dp[i] = dp[i-1] + dp[i-2]
    # return dp[n]

    # sol 2
    if n == 1:
        return 1
    if n == 2:
        return 2
    
    return self.climbStairs(n-1) + self.climbStairs(n-2)