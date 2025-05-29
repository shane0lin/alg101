# 152 . Maximum Product Subarray
# https://leetcode.com/problems/maximum-product-subarray/
# Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.
# Example 1:
# Input: [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.
# Example 2:
# Input: [-2,0,-1]
# Output: 0
# Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
def maxProduct(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if len(nums) == 0:
        return 0
    max_product = nums[0]
    min_product = nums[0]
    result = max_product
    for i in range(1, len(nums)):
        temp = max_product
        max_product = max(nums[i], max(nums[i] * max_product, nums[i] * min_product))
        min_product = min(nums[i], min(nums[i] * temp, nums[i] * min_product))
        result = max(result, max_product)
    return result
print(maxProduct([2,3,-2,4])) # 6
print(maxProduct([-2,0,-1])) # 0
print(maxProduct([-2,3,-4])) # 24
print(maxProduct([-2,3,-4,5])) # 120