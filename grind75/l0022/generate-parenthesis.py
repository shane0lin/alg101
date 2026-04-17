from typing import List


def generateParenthesis(n: int) -> List[str]:
    def dfs(l, r, cur, results):
        nonlocal n
        if l>n or r > n or r>l:
            return
        if l==n and r==n:
            results.append(''.join(cur))
        
        cur.append('(')
        dfs(l+1, r, cur, results)
        cur.pop()
        cur.append(')')
        dfs(l, r+1, cur, results)
        cur.pop()
    
    rst = []
    dfs(0,0,[], rst)
    return rst


print(generateParenthesis(1))
print(generateParenthesis(3))
