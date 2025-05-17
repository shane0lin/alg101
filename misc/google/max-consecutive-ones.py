# max consecutive ones
# https://leetcode.com/problems/max-consecutive-ones/
def max_consecutive_ones(nums):
    max_count = 0
    count = 0
    for i in nums:
        if i == 1:
            count += 1
        else:
            count = 0
        max_count = max(max_count, count)
    return max_count
print(max_consecutive_ones([1,1,0,1,1,1]))
print(max_consecutive_ones([1,0,1,1,0,1]))