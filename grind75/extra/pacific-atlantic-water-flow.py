# 417 Pacific Atlantic Water Flow
# https://leetcode.com/problems/pacific-atlantic-water-flow/
# Given an m x n matrix of non-negative integers representing the height of each unit cell in a continent, the "Pacific ocean" touches the left and top edges of the matrix and the "Atlantic ocean" touches the right and bottom edges.
# Water can only flow in four directions (up, down, left, or right) from a cell to another one with height equal or lower.
# Find the list of grid coordinates where water can flow to both the Pacific and Atlantic ocean.
# Note:
# The order of returned grid coordinates does not matter.
# Both m and n are less than 150.
# Example:
# Given the following 5x5 matrix:
#   Pacific ~   ~   ~   ~   ~ 
#        ~  1   2   2   3  (5) *
#        ~  3   2   3  (4) (4) *
#        ~  2   4  (5)  3   1  *
#        ~ (6) (7)  1   4   5  *
#        ~ (5)  1   1   2   4  *
#           *   *   *   *   * Atlantic
# Return:
# [[0, 4], [1, 3],
#  [1, 4], [2, 2],
#  [3, 0], [3, 1],
#  [4, 0]] (positions with parentheses in above matrix).
# https://leetcode.com/problems/pacific-atlantic-water-flow/discuss/90739/Python-DFS-bests-85.-Tips-for-all-DFS-in-matrix-question.
# https://leetcode.com/problems/pacific-atlantic-water-flow/discuss/90739/Python-DFS-bests-85.-Tips-for-all-DFS-in-matrix-question./93310
def pacificAtlantic(matrix):
    if not matrix or not matrix[0]: return []
    m, n = len(matrix), len(matrix[0])
    p_visited = [[False] * n for _ in range(m)]
    a_visited = [[False] * n for _ in range(m)]
    for i in range(m):
        dfs(matrix, p_visited, i, 0)
        dfs(matrix, a_visited, i, n - 1)
    for j in range(n):
        dfs(matrix, p_visited, 0, j)
        dfs(matrix, a_visited, m - 1, j)
    result = []
    for i in range(m):
        for j in range(n):
            if p_visited[i][j] and a_visited[i][j]:
                result.append([i, j])
    return result

def dfs(matrix, visited, i, j):
    visited[i][j] = True
    for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
        if 0 <= x < len(matrix) and 0 <= y < len(matrix[0]) and not visited[x][y] and matrix[x][y] >= matrix[i][j]:
            dfs(matrix, visited, x, y)

print(pacificAtlantic([[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]])) # [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]]