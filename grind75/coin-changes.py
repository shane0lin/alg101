# 322 Coin Change
# You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.
# Example 1:  
# coins = [1, 2, 5], amount = 11
# return 3 (11 = 5 + 5 + 1)
# Example 2:  
# coins = [2], amount = 3
# return -1.    
# Note: You may assume that you have an infinite number of each kind of coin.
def coinChange(coins, amount):
    dp = [0] + [float('inf')] * amount
    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)
    return dp[-1] if dp[-1] != float('inf') else -1