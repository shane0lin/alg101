# 200. Number of Islands

def numIslands(grid):


    if not grid:
        return 0
    
    m, n = len(grid), len(grid[0])
   
    visited = [[0 for _ in range(n)] for _ in range(m)]
    def bfs_mark(i, j):
        q = [(i, j)]
        visited[i][j] = 1
        while q:
            i, j = q.pop(0)
            for x, y in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == "1" and visited[x][y] == 0:
                    q.append((x, y))
                    visited[x][y] = 1

    count = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == "1" and visited[i][j] == 0:
                bfs_mark(i, j)
                count += 1
    return count
    

print(numIslands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]])) # 1
print(numIslands([["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]])) # 3