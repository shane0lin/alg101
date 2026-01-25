from typing import List
from collections import deque

def floodFill(image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
    if not image or not image[0]:
        return image
    m, n = len(image), len(image[0])

    print(m, n)
    visited = set()
    

    def isValid(x, y):
        if 0 <= x < m and 0 <= y < n and (x, y) not in visited:
            return True
        return False
    
    if not isValid(sr, sc):
        return image
    
    original = image[sr][sc]

    if original == color:
        return image
    
    # done with sanity check
    que = deque()
    visited.add((sr, sc))
    que.append((sr, sc))

    # BFS
    while que:
        x, y = que.popleft()
        image[x][y] = color
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = x + dx, y + dy
            # print(visited)
            # print(nx, ny, isValid(nx, ny),  image[nx][ny] == original)
            if isValid(nx, ny) and image[nx][ny] == original:
                visited.add((nx, ny))
                que.append((nx, ny))
    
    return image

image = [[1,1,1],[1,1,0],[1,0,1]]

print(floodFill(image, 1, 1, 2))

