from typing import List
from sys import maxsize


def maxSubArray(nums: List[int]) -> int:
    cur, max_sum = 0, -maxsize 
    for num in nums:
        cur += num
        max_sum = max(cur, max_sum)
        cur = max(cur, 0)
    return max_sum