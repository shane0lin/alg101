from typing import List


def subsets(nums: List[int]) -> List[List[int]]:
    def dfs(nums, index, subset, results):
        results.append(list(subset))
        for i in range(index, len(nums)):
            subset.append(nums[i])
            dfs(nums, i + 1, subset, results)
            del subset[-1]
    
    results = []
    dfs(nums, 0, [], results)
    return results

print(subsets([1, 2, 3]))