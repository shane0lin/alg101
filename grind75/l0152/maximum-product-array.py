from typing import List


def maxProduct(nums: List[int]) -> int:
    if not nums:
        return
    
    global_max = prev_max = prev_min = nums[0]
    for num in nums[1:]:
        if num > 0:
            cur_max = max(num, prev_max * num)
            cur_min = min(num, prev_min * num)
        else:
            cur_max = max(num, prev_min * num)
            cur_min = min(num, prev_max * num)
        global_max = max(global_max, cur_max)
        prev_max, prev_min = cur_max, cur_min
    
    return global_max