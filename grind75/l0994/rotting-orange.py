"""_summary_You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.
_Examples_
Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4
Example 2:

Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
"""

from collections import deque
from typing import List


def orangesRotting(grid: List[List[int]]) -> int:
    m, n = len(grid), len(grid[0])
    visited = set()

    que = deque([])

    for i in range(m):
        for j in range(n):
            if grid[i][j] == 2:
                que.append((i, j))
                visited.add((i, j))

    def isValid(x, y, grid, visited):
        if (x, y) not in visited and 0<=x<len(grid) and 0<= y<len(grid[0]):
            return True
        return False
    
    mins = -1
    while que:
        mins += 1
        for _ in range(len(que)):
            x, y = que.popleft()
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nx, ny = x+dx, y+dy
                if isValid(nx, ny, grid, visited) and grid[nx][ny] == 1:
                    que.append((nx, ny))
                    visited.add((nx, ny))
                    grid[nx][ny] = 2
    
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                return -1
    return mins

print(orangesRotting(grid = [[2,1,1],[1,1,0],[0,1,1]]))
print(orangesRotting(grid = [[2,1,1],[0,1,1],[1,0,1]]))
print(orangesRotting(grid=[[0]]))