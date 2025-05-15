# Sliding Window Maximum
# https://leetcode.com/problems/sliding-window-maximum/
# hard
# Time:  O(n)
# Space: O(n)
# Solution:
# Monotonic Queue
# https://leetcode.com/problems/sliding-window-maximum/discuss/65884/Java-O(n)-solution-using-deque-with-explanation

from collections import deque

def maxSlidingWindow(nums: [int], k: int) -> [int]:
    if not nums:
        return []
    n = len(nums)
    que = deque()
    rst = []
    for i in range(k):
        while que and nums[i] >= nums[que[-1]]:
            que.pop()
        que.append(i)
    
    rst.append(nums[que[0]])
    for i in range(k, n):
        while que and nums[i] >= nums[que[-1]]:
            que.pop()
        que.append(i)
        while que[0] <= i - k:
            que.popleft()
        rst.append(nums[que[0]])
    return rst
    return res

print(maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3)) # [3,3,5,5,6,7])
print(maxSlidingWindow([1], 1)) # [1]
print(maxSlidingWindow([1,2,7,7,8], 3)) # [7, 7, 8]