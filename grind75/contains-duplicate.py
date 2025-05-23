# 217. Contains Duplicate
# Easy
# 10.5K
# 1.1K
# Companies
# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
 

# Example 1:
# Input: nums = [1,2,3,1]    
# Output: true
# Example 2:
# Input: nums = [1,2,3,4]
# Output: false
# Example 3:
# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: true
 

# Constraints:
# 1 <= nums.length <= 105
# -109 <= nums[i] <= 109
def containsDuplicate(nums):
    # return len(nums) != len(set(nums))

    # sol2
    s = set()
    for num in nums:
        if num in s:
            return True
        s.add(num)
    return False
print(containsDuplicate([1,2,3,1]))