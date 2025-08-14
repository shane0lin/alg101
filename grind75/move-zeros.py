# 283 Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

def move_zeros(nums: list[int]) -> None:
   
    if not nums or len(nums) < 2:
            return nums
        
    left, right = 0, 0
    while right < len(nums):
        if nums[right] != 0:
            nums[left] = nums[right]
            left += 1
        right += 1
    while left < len(nums):
        nums[left] = 0
        left += 1
    return nums