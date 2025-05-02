# 238 Product of Array Except Self

def productExceptSelf(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    n = len(nums)
    res = [1] * n
    # invariant: res[i] = product(nums[0:i])
    for i in range(1, n):
        res[i] = res[i-1] * nums[i-1]
    
    # invariant: right = product(nums[i+1:n])
    right = 1
    for i in range(n-1, -1, -1):
        res[i] *= right
        right *= nums[i]
    return res


print(productExceptSelf([1, 2, 3, 4]))
print(productExceptSelf([1, 2, 0, 4, 5]))
