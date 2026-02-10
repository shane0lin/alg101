from typing import List


def rotate(nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse(nums, left, right):
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        
        if not nums:
            return
        
        n = len(nums)

        reverse(nums, 0, n-k-1)
        reverse(nums, n-k, n-1)
        reverse(nums, 0, n-1)
        print(nums)

rotate(nums = [1,2,3,4,5,6,7], k = 3)