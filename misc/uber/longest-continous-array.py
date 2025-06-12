# Longest Continuous Subarray with Absolute Diff less than or equal to Limit
# Given an array of integers nums and an integer limit, return the size of the longest non-empty subarray such that the absolute difference between any two elements of this subarray is less than or equal to limit.
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
def longestSubarray(nums: List[int], limit: int) -> int:

    from collections import deque
    min_deque = deque()
    max_deque = deque()
    left = 0
    max_length = 0
    for right in range(len(nums)):
        # Maintain the min_deque
        while min_deque and nums[right] < min_deque[-1]:
            min_deque.pop()
        min_deque.append(nums[right])
        # Maintain the max_deque
        while max_deque and nums[right] > max_deque[-1]:
            max_deque.pop()
        max_deque.append(nums[right])
        
        # Check if the current window is valid
        while max_deque[0] - min_deque[0] > limit:
            if nums[left] == min_deque[0]:
                min_deque.popleft()
            if nums[left] == max_deque[0]:
                max_deque.popleft()
            left += 1
        
        # Update the maximum length of the valid window
        max_length = max(max_length, right - left + 1)
    
    return max_length
 