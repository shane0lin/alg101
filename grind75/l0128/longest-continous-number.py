from collections import defaultdict

def longestConsecutive(nums: list[int]) -> int:
        s = set(nums)
        longest = 0
        
        for num in nums:
            if (num-1) not in s:
                cur = num
                count = 1
                while (cur + 1) in s:
                    cur += 1
                    count += 1
                longest = max(longest, count)
        return longest

print(longestConsecutive([2, 100, 1]))