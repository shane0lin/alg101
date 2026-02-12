# Example 1:

# Input: nums = [1,2,3], target = 4
# Output: 7
# Explanation:
# The possible combination ways are:
# (1, 1, 1, 1)
# (1, 1, 2)
# (1, 2, 1)
# (1, 3)
# (2, 1, 1)
# (2, 2)
# (3, 1)
# Note that different sequences are counted as different combinations.
# Example 2:

# Input: nums = [9], target = 3
# Output: 0
from typing import List


def combinationSum4(nums: List[int], target: int) -> int:
    def dfs(num, index, result, results, target, curSum):
        if curSum == target:
            results.append(result)
            return
        
        for i in range(index, len())

