# 189 Rotate Array
# Given an array, rotate the array to the right by k steps, where k is non-negative.
# Example 1:
# Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]
# Example 2:
# Input: nums = [-1,-100,3,99], k = 2
# Output: [3,99,-1,-100]
# Explanation:
# rotate 1 steps to the right: [99,-1,-100,3]
# rotate 2 steps to the right: [3,99,-1,-100]
# Constraints:
# 1 <= nums.length <= 105
# -231 <= nums[i] <= 231 - 1
# 0 <= k <= 105
# Follow up:
# Try to come up with as many solutions as you can. There are at least three different ways to solve this problem.
# Could you do it in-place with O(1) extra space?
# Related Topics: Array
def rotate(nums, k):
    # sol 1
    k %= len(nums)
    nums[:] = nums[-k:] + nums[:-k]
    return nums

print(rotate([1,2,3,4,5,6,7], 3))

# a = [1,2,3,4,5,6,7]
# print(a[-3:])
# print(a[:-3])
# nums[:] - This is a slice notation that refers to the entire array. Using this syntax allows you to modify the original array in-place rather than creating a new array.

# nums[-k:] - This gets the last k elements of the array. The negative index -k starts counting from the end of the array.

# nums[:-k] - This gets all elements except the last k elements.

# nums[-k:] + nums[:-k] - This concatenates the last k elements with all elements except the last k, effectively rotating the array to the right by k positions.

 