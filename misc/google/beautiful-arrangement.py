# Beautiful Arrangement
# https://leetcode.com/problems/beautiful-arrangement/
# medium
# Time:  O(n!)
# Space: O(n)
# Solution:
# Backtracking
def countArrangement(n: int) -> int:
    def backtrack(i, nums):
        if i == 1:  # base case
            return 1
        res = 0
        for j in range(i - 1, len(nums)):
            if nums[j] % i == 0 or i % nums[j] == 0:  # check if nums[j] is a factor of i
                nums[i - 1], nums[j] = nums[j], nums[i - 1]  # swap
                res += backtrack(i - 1, nums)  # backtrack
                nums[i - 1], nums[j] = nums[j], nums[i - 1]  # swap back
        return res
    return backtrack(n, list(range(1, n + 1)))
print(countArrangement(2))