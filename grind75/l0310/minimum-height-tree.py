# https://github.com/doocs/leetcode/blob/main/solution/0300-0399/0310.Minimum%20Height%20Trees/README_EN.md

from collections import deque
from typing import List


def findMinHeightTrees(n: int, edges: List[List[int]]) -> List[int]:
    if n==1:
        return [0]

    indegree = [0] * n
    graph = {i: [] for i in range(n)}

    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)
        indegree[a] += 1
        indegree[b] += 1
    
    que = deque([])
    for i in range(n):
        if indegree[i] == 1:
            que.append(i)
    
    rst = []
    while que:
        rst.clear()
        for _ in range(len(que)):
            a = que.popleft()
            rst.append(a)
            for b in graph[a]:
                indegree[b] -= 1
                if indegree[b] == 1:
                    que.append(b)
    return rst
