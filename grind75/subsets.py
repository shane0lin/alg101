# 78 Subsets
def subsets(nums):
    # # sol 1
    # res = [[]]
    # for num in nums:
    #     res += [item + [num] for item in res]
    # return res

    # # sol 2
    # res = []
    # def dfs(nums, path):
    #     res.append(path)
    #     for i in range(len(nums)):
    #         dfs(nums[i+1:], path+[nums[i]])
    # nums = sorted(nums)
    # dfs(nums, [])
    # return res
    
    # sol 3
    # res = []
    # def dfs(nums, index, combination, combinations):
    #     combinations.append(list(combination))
    #     for i in range(index, len(nums)):
    #         combination.append(nums[i])
    #         dfs(nums, i+1, combination, combinations)
    #         combination.pop()
    
    # nums = sorted(nums)
    # dfs(nums, 0, [], res)
    # return res

    # sol4
    results = []
    def search(nums, S, index):
        if index == len(nums):
            results.append(list(S))
            return
        
        S.append(nums[index])
        search(nums, S, index + 1)
        S.pop()
        search(nums, S, index + 1)
    search(sorted(nums), [], 0)
    return results



print(subsets([1,2,3]))