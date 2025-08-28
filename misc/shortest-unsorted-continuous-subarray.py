# 581 Shortest Unsorted Continuous Subarray
# Given an integer array nums, you need to find one continuous subarray such that if you only sort this subarray in non-decreasing order, then the whole array will be sorted in non-decreasing order.

# Return the shortest such subarray and output its length.
 
# Example 1:

# Input: nums = [2,6,4,8,10,9,15]
# Output: 5
# Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.
# Example 2:

# Input: nums = [1,2,3,4]
# Output: 0
# Example 3:

# Input: nums = [1]
# Output: 0

from typing import List

# Explanation:
# 1. **Sorting the Array**: First, we create a sorted version of the input array. This helps us identify the positions where the original array differs from the sorted array.
# 2. **Finding the Unsorted Subarray**: We then iterate through the original array and compare each element with the corresponding element in the sorted array. The first and last positions where the elements differ mark the boundaries of the unsorted subarray.
# 3. **Calculating the Length**: The length of the unsorted subarray is calculated as the difference between the end and start indices plus one. If the array is already sorted, the function returns 0.
# This approach efficiently identifies the shortest unsorted continuous subarray by leveraging sorting and a single pass through the array. The time complexity is dominated by the sorting step, which is O(n log n), where n is the number of elements in the array. The space complexity is O(n) due to the additional space required for the sorted array.
def findUnsortedSubarray(nums: List[int]) -> int:
    sorted_nums = sorted(nums)
    start, end = -1, -2  # Initialize to invalid indices
    for i in range(len(nums)):
        if nums[i] != sorted_nums[i]:
            if start == -1:
                start = i
            end = i
    return end - start + 1 if start != -1 else 0


def find_unsorted_subarray1(nums: List[int]) -> int:
        n = len(nums)
        maxn, right = float("-inf"), -1
        minn, left = float("inf"), -1

        for i in range(n):
            if maxn > nums[i]:
                right = i
            else:
                maxn = nums[i]

            if minn < nums[n - i - 1]:
                left = n - i - 1
            else:
                minn = nums[n - i - 1]

        return 0 if right == -1 else right - left + 1

print(findUnsortedSubarray([2,6,4,8,10,9,15]))  # Output: 5
print(findUnsortedSubarray([1,2,3,4]))  # Output: 0
print(findUnsortedSubarray([1]))  # Output: 0