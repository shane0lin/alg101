# 53. Maximum Subarray
# https://leetcode.com/problems/maximum-subarray/
def maxSubArray(nums):
    max_sum = nums[0]
    current_sum = 0
    for num in nums:
        current_sum += num
        max_sum = max(max_sum, current_sum)
        if current_sum < 0:
            current_sum = 0
    return max_sum