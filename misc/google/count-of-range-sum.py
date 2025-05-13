# Count of Range Sum
# https://leetcode.com/problems/count-of-range-sum/
# hard
# Time:  O(n^2)
# Space: O(n)
# Solution:
# Prefix sum
# Given an integer array nums, return the number of range sums that lie in [lower, upper] inclusive.
# Range sum S(i, j) is defined as the sum of the elements in nums between indices i and j (i ≤ j), inclusive.

def countRangeSum(nums, lower, upper):
    """
    :type nums: List[int]
    :type lower: int
    :type upper: int
    :rtype: int
    """
    n = len(nums)
    sums = [0] * (n + 1)
    for i in range(n):
        sums[i + 1] = sums[i] + nums[i]
    return countWhileMergeSort(sums, 0, n + 1, lower, upper)
def countWhileMergeSort(nums, start, end, lower, upper):
    if end - start <= 1:
        return 0
    mid = start + (end - start) // 2
    count = countWhileMergeSort(nums, start, mid, lower, upper) + countWhileMergeSort(nums, mid, end, lower, upper)
    j = k = mid
    for i in range(start, mid):
        while k < end and nums[k] - nums[i] < lower:
            k += 1
        while j < end and nums[j] - nums[i] <= upper:
            j += 1
        count += j - k
    nums[start:end] = sorted(nums[start:end])
    return count
print(countRangeSum([1,2,3], 0, 2))
print(countRangeSum([0], 0, 0))
print(countRangeSum([-2,5,-1], -2, 2))
print(countRangeSum([2147483647,-2147483648,-1,0], -1, 0))
print(countRangeSum([0,-3, -3,1,1, 2], 3, 5))