# 53 Maximum Subarray

# sol 1
    # def maxSubArray(self, nums: List[int]) -> int:
    #     if len(nums) == 1:
    #         return nums[0]
        
    #     def dp(i):
    #         if i == 0:
    #             return nums[i]
    #         return max(dp(i-1) + nums[i], nums[i])
        
    #     return max(dp(i) for i in range(len(nums)))

from typing import List
    # sol 2
# def maxSubArray(nums: List[int]) -> int:

#     # Initialize variables to store the maximum sum and the current sum
#     max_sum = nums[0]
#     current_sum = nums[0]
    
#     # Iterate through the array starting from the second element
#     for num in nums[1:]:
#         # Update the current sum to be the maximum of the current number or the current sum plus the current number
#         current_sum = max(num, current_sum + num)
#         # Update the maximum sum if the current sum is greater
#         max_sum = max(max_sum, current_sum)
    
    # return max_sum



def maxSubArray(nums: List[int]) -> int:
    # Initialize variables to store the maximum sum and the current sum
    dp = [0] * len(nums)
    rst = nums[0]
    for i in range(len(nums)):
        if i == 0:
            dp[i] = nums[i]
        else:
            dp[i] = max(dp[i-1] + nums[i], nums[i])
        rst = max(dp[i], rst)
    return




# Example usage
assert maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
