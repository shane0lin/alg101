from typing import List


def rotate(nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        print(nums)
        if not nums:
            return
        
        left = len(nums) - k - 1
        right = len(nums) - 1
        for _ in range(k):
            nums[left], nums[right] = nums[right], nums[left]
            left -= 1
            right -= 1 
        print(nums)

rotate(nums = [1,2,3,4,5,6,7], k = 3)