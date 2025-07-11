#300. Longest Increasing Subsequence
#Given an integer array nums, return the length of the longest strictly increasing subsequence
#A subsequence is a sequence that can be derived from an array by deleting some or no elements without changing the order of the remaining elements. For example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].
import bisect


def lengthOfLIS(nums):
    dp = [1] * len(nums)
    for i in range(len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)
print(lengthOfLIS([10,9,2,5,3,7,101,18])) #4
print(lengthOfLIS([0,1,0,3,2,3])) #4
print(lengthOfLIS([7,7,7,7,7,7,7])) #1


# sol2 ologn
def lengthOfLIS2(nums):
    sub = [nums[0]]
    for num in nums[1:]:
        if num > sub[-1]:
            sub.append(num)
        else:
            idx = bisect.bisect_left(sub, num)
            sub[idx] = num
    return len(sub)
print(lengthOfLIS2([10,9,2,5,3,7,101,18])) #4
print(lengthOfLIS2([0,1,0,3,2,3])) #4
print(lengthOfLIS2([7,7,7,7,7,7,7])) #1

# similar to sol2
    # def longestIncreasingSubsequence(self, nums):
    #     if not nums:
    #         return 0
        
    #     lis = [float('inf')] * (len(nums) + 1)
    #     lis[0] = -float('inf')
        
    #     longest = 0
    #     for num in nums:
    #         index = self.first_gte(lis, num)
    #         lis[index] = num
    #         longest = max(longest, index)
        
    #     return longest
        
    # # find first index that the number greater than or equal to num
    # def first_gte(self, nums, target):
    #     start, end = 0, len(nums) - 1
    #     while start + 1 < end:
    #         mid = (start + end) // 2
    #         if nums[mid] >= target:
    #             end = mid
    #         else:
    #             start = mid
    #     if nums[start] >= target:
    #         return start
    #     return end