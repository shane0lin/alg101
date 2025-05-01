# 11 Container With Most Water
# https://leetcode.com/problems/container-with-most-water/
# why it works? proof is here: https://www.jiuzhang.com/problems/info/383

from typing import List

def maxArea(self, height: List[int]) -> int:
    left = 0
    right = len(height) - 1
    max_area = 0
    while left < right:
        max_area = max(max_area, min(height[left], height[right]) * (right - left))
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return max_area


print(maxArea(0, [1,8,6,2,5,4,8,3,7]))
print(maxArea(0, [1,1]))