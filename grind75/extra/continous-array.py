# 525 Contiguous Array
from typing import List

def findMaxLength(nums: List[int]) -> int:
    ones = 0
    zeros = 0
    longest = 0
    for i in range(len(nums)):
        if i == 0 or nums[i] != nums[i-1]:
            # reset current
            if nums[i] == 1:
                ones = 1
            else:
                zeros = 1
        else:
            if nums[i] == 1:
                ones += 1
            else:
                zeros += 1
        longest = max(longest, 2 * min(zeros, ones))
    return longest

print(findMaxLength([0,1,0,1])) # 4