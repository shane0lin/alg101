from typing import List


def permute(nums: List[int]) -> List[List[int]]:

    def helper(nums, visited, results, result):
        # print(results)
        # print(result)
        # print('-----')
        if len(result) == len(nums):
            results.append(list(result))
            return
        for num in nums:
            if num in visited:
                continue
            result.append(num)
            visited.add(num)
            helper(nums, visited, results, result)
            visited.remove(num)
            result.pop()
            
    if not nums:
        return [[]]
    results = []
    helper(nums, set(), results, [])
    return results 

print(permute([1,2,3]))