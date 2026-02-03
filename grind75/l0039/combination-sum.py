from typing import List


def combinationSum(candidates: List[int], target: int) -> List[List[int]]:
    candidates.sort()
    # print(candidates)

    def dfs(candidates, index, target, combination, results):
        if target == 0:
            return results.append(list(combination))
        
        for i in range(index, len(candidates)):
            if candidates[i] > target:
                continue
            combination.append(candidates[i])
            dfs(candidates, i, target-candidates[i], combination, results)
            combination.pop()

    results = []
    dfs(candidates, 0, target, [], results)

    return results


print(combinationSum(candidates=[2, 3, 6, 7], target=7))