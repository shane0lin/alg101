from collections import deque
from typing import List


def numIslands(grid: List[List[str]]) -> int:
    m, n = len(grid), len(grid[0])
    visited = set()
    rst = 0
    def bfs(grid, x, y, visited, m, n):
        que = deque([(x, y)])
        visited.add((x, y))
        while que:
            cx, cy = que.popleft()
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nx, ny = cx + dx, cy + dy
                if (nx, ny) not in visited and 0<=nx<m and 0<=ny<n and grid[nx][ny] == "1":
                    que.append((nx, ny))
                    visited.add((nx, ny))

    for i in range(m):
        for j in range(n):
            if (i, j) not in visited and grid[i][j] == "1":
                rst += 1
                bfs(grid, i, j, visited, m, n) 
    return rst


grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
print(numIslands(grid)) # 1

grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
print(numIslands(grid)) # 3