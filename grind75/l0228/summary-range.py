from typing import List


def summaryRanges(nums: List[int]) -> List[str]:
    n = len(nums)
    left = 0
    rst = []
    while left < n:
        right = left
        while right + 1 < n and nums[right+1] == nums[right] + 1:
            right += 1
        
        s = str(nums[left]) if left == right else str(nums[left]) + "->" + str(nums[right])
        rst.append(s)
        left = right + 1
    return rst