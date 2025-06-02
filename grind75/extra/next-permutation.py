# 31 Next Permutation
def nextPermutation(nums):
    i = len(nums) - 2
    # 1. find the first decreasing number from the right
    while i >= 0 and nums[i] >= nums[i+1]:
        i -= 1
    # 2. find the first number from the right that is larger than nums[i]
    if i >= 0:
        j = len(nums) - 1
        while j >= 0 and nums[j] <= nums[i]:
            j -= 1
        nums[i], nums[j] = nums[j], nums[i]

    # 3. reverse the numbers from i+1 to the end
    i += 1
    j = len(nums) - 1
    while i < j:
        nums[i], nums[j] = nums[j], nums[i]
        i += 1
        j -= 1
    return nums

print(nextPermutation([1,2,3])) # [1,3,2]
print(nextPermutation([3,2,1])) # [1,2,3]
print(nextPermutation([1,1,5])) # [1,5,1]
print(nextPermutation([1,3,2])) # [2,1,3]
print(nextPermutation([1,2,3,4])) # [1,2,4,3]
print(nextPermutation([1,2,3,4,5])) # [1,2,3,5,4]
print(nextPermutation([1,2,3,4,5,6])) # [1,2,3,4,6,5]
print(nextPermutation([1,2,3,4,5,6,7])) # [1,2,3,4,5,7,6]