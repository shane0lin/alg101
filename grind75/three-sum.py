# 15. 3Sum
# Medium
# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
# Notice that the solution set must not contain duplicate triplets.
# Example 1:
# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Example 2:
# Input: nums = []
# Output: []
# Example 3:
# Input: nums = [0]
# Output: []
# Constraints:
# 0 <= nums.length <= 3000
# -105 <= nums[i] <= 105
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        def two_sum(nums, target, l, r, res):
            while l < r:
                if nums[l] + nums[r] == target:
                    res.append([-target, nums[l], nums[r]])
                    # ??
                    l += 1
                    r -= 1
                    # while l < r and nums[l] == nums[l - 1]:
                    #     l += 1
                    # while l < r and nums[r] == nums[r + 1]:
                    #     r -= 1
                elif nums[l] + nums[r] < target:
                    l += 1
                else:
                    r -= 1
        
        
        if len(nums) < 3:
            return []
        
        nums.sort()
        res = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l, r = i + 1, len(nums) - 1
            two_sum(nums, -nums[i], l, r, res)