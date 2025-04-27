# 542 01 Matrix
import collections

def  updateMatrix(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: List[List[int]]
    """
    # sol1

    # def bfs(matrix, i, j):
    #     m = len(matrix)
    #     n = len(matrix[0])
    #     queue = [(i, j)]
    #     visited = set()
    #     visited.add((i, j))
    #     step = 0
    #     while queue:
    #         size = len(queue)
    #         for i in range(size):
    #             x, y = queue.pop(0)
    #             if matrix[x][y] == 0:
    #                 return step
    #             for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
    #                 if 0 <= x + dx < m and 0 <= y + dy < n and (x + dx, y + dy) not in visited:
    #                     queue.append((x + dx, y + dy))
    #                     visited.add((x + dx, y + dy))
    #         step += 1

    # m = len(matrix)
    # n = len(matrix[0])
    # res = [[0 for i in range(n)] for j in range(m)]
    # for i in range(m):
    #     for j in range(n):
    #         # if matrix[i][j] == 0:
    #         #     res[i][j] = 0
    #         # else:
    #         #     res[i][j] = bfs(matrix, i, j)
    #         res[i][j] = bfs(matrix, i, j)

    
    # return res
    zeros = [(i, j) for i in range(len(matrix)) for j in range(len(matrix[0])) if matrix[i][j] == 0]
    que = collections.deque(zeros)
    res = [[0 for i in range(len(matrix[0]))] for j in range(len(matrix))]
    visited = set(zeros)
    while que:
        i, j = que.popleft()
        for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
            if 0 <= x < len(matrix) and 0 <= y < len(matrix[0]) and (x, y) not in visited:
                res[x][y] = res[i][j] + 1
                que.append((x, y))
                visited.add((x, y))
    return res

print(updateMatrix([[0,0,0],[0,1,0],[1,1,1]]))