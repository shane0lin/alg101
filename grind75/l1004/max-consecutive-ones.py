from typing import List


def longestOnes(nums: List[int], k: int) -> int:
    zero_count, left = 0, 0
    for num in nums:
        if num == 0:
            zero_count += 1
        if zero_count > k:
            if nums[left] == 0:
                zero_count -= 1
            left += 1
    return len(nums) - left

print(longestOnes(nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2))