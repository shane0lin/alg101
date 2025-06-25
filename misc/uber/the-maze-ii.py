# # 505 The Maze II
# You are tasked with solving a problem involving a maze represented as a grid. The maze is defined by a 2D array where `0` represents an open cell and `1` represents a blocked cell. You are given a starting point and an ending point in the maze. Your goal is to determine if there is a path from the starting point to the ending point, and if so, find the shortest path.
# Here is a detailed breakdown of the problem:To solve this problem, we can use the Breadth-First Search (BFS) algorithm. BFS is well-suited for finding the shortest path in an unweighted grid like this maze. Here's a step-by-step approach to implement the solution:
# 1. **Initialize the Grid and Points**: Define the maze grid and the starting and ending points.
# 2. **BFS Implementation**: Use a queue to explore each cell level by level. Mark visited cells to avoid cycles.
# 3. **Path Reconstruction**: Keep track of the path to reconstruct it if a solution is found.To implement the solution, we will use Python. Below is the complete code to solve the problem:    


import collections
import math

DIRECTIONS = {
    'U': [0, -1],
    'R': [1, 0],
    'D': [0, 1],
    'L': [-1, 0]
}

class Solution:
    """
    @param maze: the maze
    @param start: the start
    @param destination: the destination
    @return: the shortest distance for the ball to stop at the destination
    """
    def shortestDistance2(self, maze, start, destination):
        # (x, y, direction)
        queue = collections.deque()
        distance = {}

        start = (start[0], start[1], None)
        destination = (destination[0], destination[1], None)

        queue.append(start)
        distance[start] = 0

        while queue:
            (curr_x, curr_y, curr_dire) = queue.popleft()
            if (curr_x, curr_y, curr_dire) == destination:
                return distance[(curr_x, curr_y, curr_dire)]

            if curr_dire != None:
                new_dire = curr_dire
                new_x, new_y = curr_x + DIRECTIONS[new_dire][0], curr_y + DIRECTIONS[new_dire][1]
                # is vaild -> 按当前方向走
                # not vaild -> 方向改成 None 
                if self.is_vaild(maze, new_x, new_y):
                    if (new_x, new_y, new_dire) in distance:
                        continue
                    queue.append((new_x, new_y, new_dire))
                    distance[(new_x, new_y, new_dire)] = distance[(curr_x, curr_y, curr_dire)] + 1
                else:
                    if (curr_x, curr_y, None) in distance:
                        continue
                    queue.append((curr_x, curr_y, None))
                    distance[(curr_x, curr_y, None)] = distance[(curr_x, curr_y, curr_dire)]
            else:
                for new_dire in DIRECTIONS:
                    new_x, new_y = curr_x + DIRECTIONS[new_dire][0], curr_y + DIRECTIONS[new_dire][1]
                    if self.is_vaild(maze, new_x, new_y):
                        if (new_x, new_y, new_dire) in distance:
                            continue
                        queue.append((new_x, new_y, new_dire))
                        distance[(new_x, new_y, new_dire)] = distance[(curr_x, curr_y, curr_dire)] + 1

        return -1
    
    def is_vaild(self, maze, x, y):
        n, m = len(maze), len(maze[0])

        if x < 0 or x >= n:
            return False
        if y < 0 or y >= m:
            return False
        
        return not maze[x][y]
    
    def shortestDistance(self, maze, start, destination):
        DIR = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        que = collections.deque([start])
        m, n = len(maze), len(maze[0])
        distance = [[math.inf]*n for _ in range(m)]
        visited = set()
        visited.add(start)
        # print(start)
        distance[start[0]][start[1]] = 0
        
        
        while que:
            cx, cy = que.popleft()
            for dx, dy in DIR:
                nx, ny = cx, cy
                
                while self.is_vaild(maze, nx+dx, ny+dy):
                    distance[nx+dx][ny+dy] = min(distance[nx][ny]+1, distance[nx+dx][ny+dy])
                    if (nx+dx, ny+dy) == destination:
                        return distance[nx+dx][ny+dy] 
                    nx += dx
                    ny += dy
                
                if not (nx, ny) in visited:
                    que.append((nx, ny))
                    visited.add((nx, ny))
                    # print("f({nx}, {ny})")
                    # print(distance[nx][ny] )

                

                
                

        return -1


maze = [[0, 0, 1, 0, 0], 
        [0, 0, 0, 0, 0], 
        [0, 0, 0, 1, 0], 
        [1, 1, 0, 1, 1], 
        [0, 0, 0, 0, 0]]

sol = Solution()
print(sol.shortestDistance(maze, (0, 4), (4, 4))) # 12
print(sol.shortestDistance(maze, (0, 4), (0, 0))) # 6