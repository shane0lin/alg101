from typing import List


def sortedSquares(nums: List[int]) -> List[int]:
    if not nums:
        return []
    rst = [0] * len(nums)
    left, right, pos = 0, len(nums) - 1, len(nums) - 1
    while left <= right:
        if nums[left] * nums[left] > nums[right] * nums[right]:
            rst[pos] = nums[left] * nums[left]
            left += 1
        else:
            rst[pos] = nums[right] * nums[right]
            right -= 1
        pos -= 1
    return rst

print(sortedSquares([-4,-1,0,3,10]))

