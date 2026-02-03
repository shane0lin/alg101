from sys import maxsize
def coinChange(coins: list[int], amount: int) -> int:
    dp = [maxsize] * (amount + 1)
    dp[0] = 0
    for coin in coins:
        for i in range(coin, amount+1):
            dp[i] = min(dp[i], dp[i-coin] + 1) 
    
    return dp[amount] if dp[amount] < maxsize else -1

print(coinChange([1,2,5], 11))