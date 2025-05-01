# 75 - Sort Colors
# https://leetcode.com/problems/sort-colors/
def sortColors(nums):
    """
    Do not return anything, modify nums in-place instead.
    """

    # Invariance:
    # nums[:left] == 0
    # nums[right + 1:] == 2
    left, index, right = 0, 0, len(nums) - 1
    while index <= right:
        if nums[index] == 0:
            nums[left], nums[index] = nums[index], nums[left]
            left += 1
            index += 1
        elif nums[index] == 2:
            nums[right], nums[index] = nums[index], nums[right]
            right -= 1
        else:
            index += 1
    return nums

print(sortColors([2,0,2,1,1,0]))
print(sortColors([2,0,1]))