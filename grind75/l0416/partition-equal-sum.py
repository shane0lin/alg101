from typing import List


def canPartition(nums: List[int]) -> bool:
    sum_ = sum(nums)
    if sum_ % 2 > 0:
        return False
    
    target = sum_ // 2

    dp = [False] * (target + 1)
    dp[0] = True
    for num in nums:
        for j in range(target, num-1, -1):
            dp[j] |= dp[j - num]
    return dp[target]

# print(canPartition(nums = [1, 2, 5]))
print(canPartition(nums = [1, 5, 11, 5]))