#1436 Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit
# tGiven an array of integers nums and an integer limit, return the size of the longest non-empty subarray such that the absolute difference between any two elements of this subarray is less than or equal to limit.

# Example 1:

# Input: nums = [8,2,4,7], limit = 4
# Output: 2 
# Explanation: All subarrays are: 
# [8] with maximum absolute diff |8-8| = 0 <= 4.
# [8,2] with maximum absolute diff |8-2| = 6 > 4. 
# [8,2,4] with maximum absolute diff |8-2| = 6 > 4.
# [8,2,4,7] with maximum absolute diff |8-2| = 6 > 4.
# [2] with maximum absolute diff |2-2| = 0 <= 4.
# [2,4] with maximum absolute diff |2-4| = 2 <= 4.
# [2,4,7] with maximum absolute diff |2-7| = 5 > 4.
# [4] with maximum absolute diff |4-4| = 0 <= 4.
# [4,7] with maximum absolute diff |4-7| = 3 <= 4.
# [7] with maximum absolute diff |7-7| = 0 <= 4. 
# Therefore, the size of the longest subarray is 2.
# Example 2:

# Input: nums = [10,1,2,4,7,2], limit = 5
# Output: 4 
# Explanation: The subarray [2,4,7,2] is the longest since the maximum absolute diff is |2-7| = 5 <= 5.
# Example 3:

# Input: nums = [4,2,2,2,4,4,2,2], limit = 0
# Output: 3
from typing import List
from collections import deque
def longestSubarray(nums: List[int], limit: int) -> int:
    rst = 0
    start, end = 0, 0
    minQue = deque()
    maxQue = deque()
    while end < len(nums):
        while minQue and nums[end] < minQue[-1]:
            minQue.pop()
        while maxQue and nums[end] > maxQue[-1]:
            maxQue.pop()
        minQue.append(nums[end])
        maxQue.append(nums[end])
        # print(maxQue)
        # print(minQue)
        # print("---")

        if maxQue[0] - minQue[0] <= limit:
            rst = max(rst, end - start + 1)
        else:
            while maxQue[0] - minQue[0] > limit:
                if nums[start] == minQue[0]:
                    minQue.popleft()
                if nums[start] == maxQue[0]:
                    maxQue.popleft()
                start += 1

        end +=1
    return rst

nums = [10,1,2,4,7,2]
limit = 5
print(longestSubarray(nums, limit)) # 4
nums = [4,2,2,2,4,4,2,2]
limit = 0
print(longestSubarray(nums, limit)) # 3
