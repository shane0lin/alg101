
def twoSum(nums: list[int], target: int) -> list[int]:
    hm = {} # num, index
    for i, num in enumerate(nums):
        if target - num in hm:
            return [hm[target-num], i]
        hm[num] = i

print(twoSum(nums = [2,7,11,15], target = 9)) # 0, 1
print(twoSum(nums = [3,2,4], target = 6)) # 1, 2
print(twoSum(nums = [3,3], target = 6)) # 0, 1