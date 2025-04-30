#46. Permutations
#Given a collection of distinct integers, return all possible permutations.
#Example:   Input: [1,2,3]    Output:    [ [1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1] ]

def dfs(nums, used, res, cur):
    if len(cur) == len(nums):
        res.append(cur[:])
        return
    
    for i in range(len(nums)):
        if used[i] == 1:
            continue
        used[i] = 1
        cur.append(nums[i])
        dfs(nums, used, res, cur)
        cur.pop()
        used[i] = 0

def permute(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    # if len(nums) == 0:
    #     return []
    # if len(nums) == 1:
    #     return [nums]
    # else:
    #     res = []
    #     for i in range(len(nums)):
    #         for j in permute(nums[:i] + nums[i+1:]):
    #             res.append([nums[i]] + j)
    #     return res
    res = []
    used = [0] * len(nums)
    dfs(nums, used, res, [])
    return res

print(permute([1,2,3]))