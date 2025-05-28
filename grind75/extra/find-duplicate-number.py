# 287 Find the Duplicate Number
class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # O(n) time, O(1) space
        # Floyd's Tortoise and Hare (Cycle Detection)
        # https://en.wikipedia.org/wiki/Cycle_detection#Floyd's_Tortoise_and_Hare
        # https://discuss.leetcode.com/topic/27981/proof-of-o-n-time-and-o-1-space-solution
        # https://discuss.leetcode.com/topic/27981/share-my-o-n-time-o-1-space-solution

        # tortoise = hare = nums[0]
        # while True:
        #     tortoise = nums[tortoise]
        #     hare = nums[nums[hare]]
        #     if tortoise == hare:
        #         break
        # # find the entrance to the cycle
        # tortoise = nums[0]
        # while tortoise != hare:
        #     tortoise = nums[tortoise]
        #     hare = nums[hare]
        # return hare

        # sol2, same idea, but use idea of slow, fast pointer to find link list cycle
        slow, fast = nums[0], nums[nums[0]]
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
        slow = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow
# OJ: https://leetcode.com/problems/find-the-duplicate-number/
# Author: github.com/nexusuid