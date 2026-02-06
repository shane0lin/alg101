"""
given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.

For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

Given A = [1, 2, 3], the function should return 4.

Given A = [−1, −3], the function should return 1.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [−1,000,000..1,000,000].
"""

def first_missing_positive(nums):
    n = len(nums)

    # Place each number x at index x-1 (if 1 <= x <= n)
    for i in range(n):
        while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
            # Swap nums[i] to its correct position
            correct_idx = nums[i] - 1
            nums[i], nums[correct_idx] = nums[correct_idx], nums[i]

    # Find the first index where nums[i] != i + 1
    for i in range(n):
        if nums[i] != i + 1:
            return i + 1

    # All positions filled correctly, answer is n + 1
    return n + 1


# Test cases
print(first_missing_positive([1, 3, 6, 4, 1, 2]))  # Expected: 5
print(first_missing_positive([1, 2, 3]))           # Expected: 4
print(first_missing_positive([-1, -3]))            # Expected: 1
print(first_missing_positive([3, 4, -1, 1]))       # Expected: 2
print(first_missing_positive([7, 8, 9, 11, 12]))   # Expected: 1