# 490 The Maze
def solve_maze(maze: list[str]) -> str:
    """
    You are given a maze represented as a grid of characters. Each cell in the grid
    can either be empty (denoted by '.') or blocked (denoted by '#'). The maze has
    a single entrance at the top-left corner (0, 0) and a single exit at the
    bottom-right corner (N-1, M-1). You can move up, down, left, or right, but you
    cannot move into blocked cells or outside the grid. Your task is to determine if
    there is a path from the entrance to the exit. If such a path exists, output
    "YES"; otherwise, output "NO".
    """
    if not maze or not maze[0]:
        return "NO"
    N, M = len(maze), len(maze[0])
    if maze[0][0] == '#' or maze[N-1][M-1] == '#':
        return "NO"
    
    from collections import deque
    
    queue = deque([(0, 0)])
    visited = set((0, 0))
    
    while queue:
        x, y = queue.popleft()
        
        if (x, y) == (N-1, M-1):
            return "YES"
        
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and maze[nx][ny] == '.' and (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append((nx, ny))
    
    return "NO"