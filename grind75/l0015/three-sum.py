from typing import List


def threeSum(nums: List[int]) -> List[List[int]]:
    rst = []

    if not nums or len(nums) <= 2:
        return rst
    
    nums.sort()
    print(nums)
    
    def find_2_sum(nums, left, right, target, rst):
        last_pair = None
        while left < right:
            if nums[left] + nums[right] == target:
                if (nums[left], nums[right]) != last_pair:
                    rst.append([-target, nums[left], nums[right]])
                    last_pair = (nums[left], nums[right])
                left += 1
                right -=1
            elif nums[left] + nums[right] > target:
                right -= 1
            else:
                left += 1
    for i in range(len(nums)):
        if i>0 and nums[i] == nums[i-1]:
            continue
        find_2_sum(nums, i+1, len(nums)-1, -nums[i], rst)
    return rst

# print(threeSum(nums=[2, 7,11,15]))
# print(threeSum(nums=[-1, 0, 1,2,-1,-4]))
# print(threeSum(nums=))
# print(threeSum(nums=))
print(threeSum(nums=[1,2,0,1,0,0,0,0]))