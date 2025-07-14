# 4. Median of Two Sorted Array
# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

# The overall run time complexity should be O(log (m+n)).

 

# Example 1:

# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.
# Example 2:

# Input: nums1 = [1,2], nums2 = [3,4]
# Output: 2.50000
# Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
 

# Constraints:

# nums1.length == m
# nums2.length == n
# 0 <= m <= 1000
# 0 <= n <= 1000
# 1 <= m + n <= 2000
# -106 <= nums1[i], nums2[i] <= 106
from typing import List
import math


def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
    def findKth(index1: int, index2: int, k:int):
        if index1 >= len(nums1):
            return nums2[index2 + k - 1]
        if index2 >= len(nums2):
            return nums1[index1 + k - 1]
        if k == 1:
            return min(nums1[index1], nums2[index2])
        half = k // 2
        new_index1 = min(index1 + half, len(nums1)) - 1
        new_index2 = min(index2 + half, len(nums2)) - 1
        pivot1, pivot2 = nums1[new_index1], nums2[new_index2] 

        if pivot1 <= pivot2:
            k -= (new_index1 - index1 + 1)
            index1 = new_index1 + 1
        else:
            k -= (new_index2 - index2 + 1)
            index2 = new_index2 + 1

        return findKth(index1, index2, k)
    
    m, n = len(nums1), len(nums2)
    total = m + n
    if total % 2 == 1:
        return findKth(0, 0, total // 2 + 1)
    else:
        return (findKth(0, 0, total // 2) + findKth(0, 0, total // 2 + 1)) / 2



print(findMedianSortedArrays([1,3], [2])) # 2
print(findMedianSortedArrays([1,2], [3,4])) # 2.5