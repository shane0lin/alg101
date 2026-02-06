from typing import List


def findDuplicate(nums: List[int]) -> int:
    if not nums or len(nums) < 2:
        return -1
    
    slow = nums[0]
    fast = nums[nums[0]]

    while fast != slow:
        slow = nums[slow]
        fast = nums[nums[fast]]
    
    fast = 0
    while fast != slow:
        slow = nums[slow]
        fast = nums[fast]
    
    return slow

