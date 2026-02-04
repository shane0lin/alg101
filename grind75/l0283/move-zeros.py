from typing import List


def moveZeroes(nums: List[int]) -> None:
    left = 0
    n = len(nums)
    
    while left < n and nums[left] !=0: # right point to first 0
        left += 1
    right = left + 1
    while right < n:
        if nums[right] == 0:
            right +=1
            continue

        nums[left], nums[right] = nums[right], nums[left]

        left += 1
        right += 1
    
    while left < n:
        nums[left] = 0
        left += 1 
        
        
        
        
    
    
    print(nums)


moveZeroes(nums = [0,1,0,3,12])
moveZeroes(nums = [0])