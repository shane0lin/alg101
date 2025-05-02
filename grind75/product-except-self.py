# 238 Product of Array Except Self

def productExceptSelf(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    # n = len(nums)
    # res = [1] * n
    # # invariant: res[i] = product(nums[0:i])
    # for i in range(1, n):
    #     res[i] = res[i-1] * nums[i-1]
    
    # # invariant: right = product(nums[i+1:n])
    # right = 1
    # for i in range(n-1, -1, -1):
    #     res[i] *= right
    #     right *= nums[i]
    # return res
    n = len(nums)
    ans = [1] * n # ans[i] = product(0:i)
    for i in range(1, n):
        ans[i] = nums[i-1] * ans[i-1]
    
    rproducts = [1] * n # rproducts[i] = product(i+1:n)
    for i in range(n-2, -1, -1):
        rproducts[i] = rproducts[i+1] * nums[i+1]
    # rproducts = product(i+1:)
    for i in range(n):
        ans[i] *= rproducts[i]
    
    return ans

print(productExceptSelf([1, 2, 3, 4]))
# print(productExceptSelf([1, 2, 0, 4, 5]))
