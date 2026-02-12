from typing import List

def findMin(nums: List[int]) -> int:
    n = len(nums)
    if nums[0] <= nums[n-1]:
        return nums[0]
    

    left, right = 0, n-1
    while left + 1 < right:
        mid = left + (right -left) // 2
        if nums[0] <= nums[mid]:
            left = mid + 1
        else:
            right = mid
    
    return nums[left] if nums[left] < nums[right] else nums[right]
