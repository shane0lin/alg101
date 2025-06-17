# House Rob II
from typing import List


def rob(nums: List[int]) -> int:
    n = len(nums)
    if n == 0:
        return 0
    if n == 1:
        return nums[0]
    dp = [0] * n
    rst = dp[0] = nums[0]
    for i in range(1, n-1):
        dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        rst = max(rst, dp[i])

    dp = [0] * n
    dp[1] = nums[1]
    for i in range(2, n):
        dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        rst = max(rst, dp[i])
    
    return rst


# Example usage
assert rob([2, 3, 2]) == 3
assert rob([1, 2, 3, 1]) == 4
assert rob([1, 2, 3]) == 3