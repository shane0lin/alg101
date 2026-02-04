from typing import List


def exist(board: List[List[str]], word: str) -> bool:
    def dfs(board, word, index, x, y, m, n, visited):
        if index == len(word) - 1:
            return True
        
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx = x + dx
            ny = y + dy
            if 0<=nx<m and 0<=ny<n and not visited[nx][ny] and board[nx][ny] == word[index+1]:
                visited[nx][ny] = True
                found = dfs(board, word, index+1, nx, ny, m, n, visited)
                if found:
                    return True
                visited[nx][ny] = False
        return False
    
    if not board or not board[0] or not word:
        return False
    
    m, n = len(board), len(board[0])
    visited = [[False] * n for _ in range(m)]

    for i in range(m):
        for j in range(n):
            if board[i][j] == word[0]:
                visited[i][j] = True
                found = dfs(board, word, 0, i, j, m, n, visited)
                if found:
                    return True
                visited[i][j] = False
    return False


