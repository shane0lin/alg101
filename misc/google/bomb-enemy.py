# Bomb Enemy
# Given a 2D grid, each cell is either a wall 'W', an enemy 'E' or empty '0' (the number zero), return the maximum enemies you can kill using one bomb.
# The bomb kills all the enemies in the same row and column from the planted point until it hits the wall since the wall is too strong to be destroyed.
# Note: You can only put the bomb at an empty cell.
# Example:
# For the given grid
# 0 E 0 0
# E 0 W E
# 0 E 0 0
# return 3. (Placing a bomb at (1,1) kills 3 enemies)
# Credits:
# Special thanks to @memoryless for adding this problem and creating all test cases.
# Hide Company Tags Google
# Hide Tags Dynamic Programming
# Hide Similar Problems (M) Number of Islands (M) Walls and Gates
# Goal: find the max number of enemies that can be killed by a bomb placed at an empty cell
# Idea: for each empty cell, we can find the number of enemies that can be killed by a bomb placed at that cell
#       we can do this by finding the number of enemies in the row and column that the cell is in   


def bomb_enemy(grid):
    if not grid or not grid[0]:
        return 0
    m, n = len(grid), len(grid[0])
    left = [[0 for _ in range(n)] for _ in range(m)]
    right = [[0 for _ in range(n)] for _ in range(m)]
    up = [[0 for _ in range(n)] for _ in range(m)]
    down = [[0 for _ in range(n)] for _ in range(m)]
    rst = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 'E':
                left[i][j] = 1 if j == 0 else left[i][j-1] + 1
                up[i][j] = 1 if i == 0 else up[i-1][j] + 1
            elif grid[i][j] == 'W':
                left[i][j] = 0
                up[i][j] = 0
            else:
                left[i][j] = 0 if j == 0 else left[i][j-1]
                up[i][j] = 0 if i == 0 else up[i-1][j]

    for i in range(m-1, -1, -1):
        for j in range(n-1, -1, -1):
            if grid[i][j] == 'E':
                right[i][j] = 1 if j == n-1 else right[i][j+1] + 1
                down[i][j] = 1 if i == m-1 else down[i+1][j] + 1
            elif grid[i][j] == 'W':
                right[i][j] = 0
                down[i][j] = 0
            else:
                right[i][j] = 0 if j == n-1 else right[i][j+1]
                down[i][j] = 0 if i == m-1 else down[i+1][j]
            
    for i in range(m-1, -1, -1):
        for j in range(n-1, -1, -1):
            if grid[i][j] == '0':
                rst = max(rst, left[i][j] + right[i][j] + up[i][j] + down[i][j])
    return rst



print(bomb_enemy([['0', 'E', '0', '0'], ['E', '0', 'W', 'E'], ['0', 'E', '0', '0']])) # 3
print(bomb_enemy([['0', 'E', '0', '0'], ['E', 'E', 'W', 'E'], ['0', 'E', '0', '0']])) # 2
print(bomb_enemy([['0', 'E', '0', '0'], ['E', '0', 'W', 'E'], ['0', 'E', '0', '0'], ['0', 'E', '0', '0']])) # 4
print(bomb_enemy([['0', 'E', '0', '0'], ['E', '0', 'W', 'E'], ['0', 'E', '0', '0'], ['0', 'E', '0', '0'], ['0', 'E', '0', '0']])) # 5