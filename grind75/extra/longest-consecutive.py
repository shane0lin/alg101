# 128 Longest Consecutive Sequence

def longestConsecutive(nums):
    # sol 1, O(nlogn) time, O(1) space
    # if not nums:
    #     return 0
    # nums.sort()
    # longest = 1
    # cur = 1
    # for i in range(1, len(nums)):
    #     if nums[i] == nums[i-1]:
    #         continue
    #     elif nums[i] == nums[i-1] + 1:
    #         cur += 1
    #     else:
    #         longest = max(longest, cur)
    #         cur = 1
    # return max(longest, cur)

    # sol 2, O(n) time, O(n) space
    longest = 0
    numSet = set(nums)
    for n in nums:
        if n-1 not in numSet:
            length = 1
            while n + length in numSet:
                length += 1
            longest = max(longest, length)
    return longest

print(longestConsecutive([100,4,200,1,3,2])) # 4
print(longestConsecutive([0,3,7,2,5,8,4,6,0,1])) # 9
print(longestConsecutive([1,2,0,1])) # 3
print(longestConsecutive([1,2,0,1,3])) # 4