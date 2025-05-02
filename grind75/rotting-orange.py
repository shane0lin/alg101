# 994 Rotting Oranges
# BFS
import collections
from typing import List

def orangesRotting(grid: List[List[int]]) -> int:
    m, n = len(grid), len(grid[0])
    q = collections.deque()
    fresh = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 2:
                q.append((i, j))
            elif grid[i][j] == 1:
                fresh += 1
    if fresh == 0:
        return 0
    time = 0
    while q:
        size = len(q)
        for _ in range(size):
            i, j = q.popleft()
            for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if 0 <= x < m and 0 <= y < n and grid[x][y] == 1:
                    grid[x][y] = 2
                    q.append((x, y))
                    fresh -= 1
        time += 1
    return time - 1 if fresh == 0 else -1

print(orangesRotting([[2,1,1],[1,1,0],[0,1,1]]))
print(orangesRotting([[2,1,1],[0,1,1],[1,0,1]]))
print(orangesRotting([[0,2]]))  
#####
print(orangesRotting([[2,1,1],[1,1,1],[1,1,1]])) # 4