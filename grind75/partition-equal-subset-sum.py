# 416. Partition Equal Subset Sum
# Medium
# 10.6K
# 142
# Companies
# Given an integer array nums, return true if you can partition the array into two subsets such that the sum of the elements in both subsets is equal or false otherwise.
 

# Example 1:
# Input: nums = [1,5,11,5]
# Output: true
# Explanation: The array can be partitioned as [1, 5, 5] and [11].
# Example 2:
# Input: nums = [1,2,3,5]
# Output: false
# Explanation: The array cannot be partitioned into equal sum subsets.
 

# Constraints:
# 1 <= nums.length <= 200
# 1 <= nums[i] <= 100

from typing import List
def canPartition(nums: List[int]) -> bool:
    total = sum(nums)
    if total % 2 != 0:
        return False
    target = total // 2
    dp = [False] * (target + 1)
    dp[0] = True
    # solution 1, better
    # for num in nums:
    #     for i in range(target, num - 1, -1):
    #         dp[i] = dp[i] or dp[i - num]

    # solution 2
    dp = [False] * (target + 1)
    dp[0] = True
    for num in nums:
        for i in range(target+1):
            if dp[i] and i < target+1 - num:
                dp[i + num] = True
    return dp[target]

print(canPartition([1,5,11,5]))
print(canPartition([1,2,3,5]))