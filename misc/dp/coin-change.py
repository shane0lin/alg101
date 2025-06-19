# 669 Coin Change
from typing import List
def coinChange(coins: List[int], amount: int) -> int:
    # Initialize dp array with a large number (infinity)
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0  # Base case: 0 coins needed to make amount 0
    for i in range(1, amount + 1):
        for coin in coins:
            if i - coin >= 0:
                dp[i] = min(dp[i], dp[i - coin] + 1)
    return dp[amount] if dp[amount] != float('inf') else -1


# Example usage
assert coinChange([1, 2, 5], 11) == 3  # Output: 3 (11 = 5 + 5 + 1)
assert coinChange([2], 3) == -1        # Output: -1 (not possible to make 3 with coin 2)
assert coinChange([1], 0) == 0         # Output: 0 (no coins needed for amount 0)
assert coinChange([1], 1) == 1          # Output: 1 (1 = 1)
assert coinChange([1], 2) == 2          # Output: 2 (2 = 1 + 1)