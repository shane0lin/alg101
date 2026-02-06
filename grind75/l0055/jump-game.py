from typing import List


def canJump(nums: List[int]) -> bool:
    dp = [False] * len(nums)
    dp[0] = True
    for i, num in enumerate(nums):
        if dp[i]:
            for j in range(1, num+1):
                if i+j < len(nums):
                    dp[i+j] = True
    return dp[-1]

print(canJump(nums = [2,3,1,1,4]))
print(canJump(nums = [3,2,1,0,4]))