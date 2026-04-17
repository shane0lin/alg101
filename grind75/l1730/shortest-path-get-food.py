# You are placed in a grid and need to find the shortest path to reach any food cell. The grid is an m x n character matrix containing four types of cells:

# '*' represents your starting location (there is exactly one such cell)
# '#' represents a food cell (there can be multiple food cells)
# 'O' represents free space that you can travel through
# 'X' represents an obstacle that blocks your path
# You can move in four directions from any cell: north (up), east (right), south (down), or west (left). You can only move to an adjacent cell if it's within the grid boundaries and is not an obstacle.

# The goal is to find the length of the shortest path from your starting position to any food cell. If no path exists to reach any food, return -1.

# For example, if you start at '*' and the nearest food '#' is 3 moves away (moving through free spaces 'O'), you would return 3. The path length counts the number of moves needed, not the number of cells visited.

from typing import List
from collections import deque


def getFood(grid: List[List[str]]) -> int:
    if not grid or not grid[0]:
        return -1
    
    m, n = len(grid), len(grid[0])
    i, j = next((i,j) for i in range(m) for j in range(n) if grid[i][j] == '*')
    que = deque([(i, j)])

    rst = 0

    while que:
        rst += 1
        for _ in range(len(que)):
            x, y = que.popleft()
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nx = x + dx
                ny = y + dy
                if 0<=nx<m and 0<=ny<n:
                    if grid[nx][ny] == '#':
                        return rst
                    elif grid[nx][ny] == 'O':
                        grid[nx][ny] == 'V'
                        que.append((nx, ny))
    return -1