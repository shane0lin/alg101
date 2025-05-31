# Shortest Path to Get Food
# https://leetcode.com/problems/shortest-path-to-get-food/
# medium
# Time:  O(m*n)
# Space: O(m*n)
# Solution:
# BFS
from typing import List
from collections import deque
def getFood(self, grid: List[List[str]]) -> int:
    m, n = len(grid), len(grid[0])
    q = deque()
    for i in range(m):
        for j in range(n):
            if grid[i][j] == '*':
                q.append((i, j, 0))
                break
    while q:
        i, j, d = q.popleft()
        for x, y in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
            if 0 <= x < m and 0 <= y < n and grid[x][y] != 'X':
                if grid[x][y] == '#':
                    return d + 1
                grid[x][y] = 'X'
                q.append((x, y, d+1))
    return -1