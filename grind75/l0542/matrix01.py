from collections import deque

def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
    m, n = len(mat), len(mat[0])
    dist = [[0] * n for _ in range(m)]
    zeros = [(i, j) for i in range(m) for j in range(n) if mat[i][j] == 0]

    que = deque(zeros)
    visited = set(zeros)

    while que:
        i, j = que.popleft()
        for ni, nj in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
            if 0<=ni<m and 0<=nj<n and (ni, nj) not in visited:
                dist[ni, nj] = dict[i][j] + 1
                que.append((ni, nj))
                visited.add((ni, nj))

    return dist