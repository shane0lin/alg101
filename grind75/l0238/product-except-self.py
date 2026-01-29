from typing import List


def productExceptSelf(self, nums: List[int]) -> List[int]:
    product = [1] * len(nums)

    product[len(nums)-1] = nums[len(nums)-1]
    for i in range(len(nums)-2, -1, -1):
        product[i] =  nums[i] * product[i+1]
    
    left_to_right = 1
    for i in range(0, len(nums)-1):
        product[i] = product[i+1] * left_to_right 
        left_to_right *= nums[i]

    product[len(nums)-1] = left_to_right
    return product