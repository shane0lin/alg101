# Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

# You must write an algorithm with O(log n) runtime complexity.

def search(nums, target):
    if not nums:
            return -1
        
    start, end = 0, len(nums) - 1
    while start < end -1:
        mid = start + (end - start) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    if nums[start] == target:
        return start
    if nums[end] == target:
        return end
    return -1