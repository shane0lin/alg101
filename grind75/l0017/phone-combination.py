from typing import List


def letterCombinations(digits: str) -> List[str]:
    hm = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9':  'wxyz'
    }
    def dfs(digits, hm, index, cur, results):
        if index == len(digits):
            results.append(''.join(cur))
            return
        
        for i in range(len(hm[digits[index]])):
            cur.append(hm[digits[index]][i])

            dfs(digits, hm, index+1, cur, results)

            cur.pop()
    
    rst = []
    dfs(digits, hm, 0, [], rst)
    print(rst)


letterCombinations("23")

        

