from typing import List


def combinationSum4(self, nums: List[int], target: int) -> int:
    dp = [1] + [0] * target

    for i in range(1, target+1):
        for j in range(len(nums)):
            if i >= nums[j]:
                dp[i] += dp[i-nums[j]]
    
    return dp[target]