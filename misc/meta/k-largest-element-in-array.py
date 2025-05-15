# 215 Kth Largest Element in an Array
# https://leetcode.com/problems/kth-largest-element-in-an-array/
def findKthLargest(nums, k):
    nums.sort()
    return nums[-k]