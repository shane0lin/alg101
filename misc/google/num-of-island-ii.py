# Number of Islands

# Given a n,m which means the row and column of the 2D matrix and an array of pair A( size k). 
# Originally, the 2D matrix is all 0 which means there is only sea in the matrix. 
# The list pair has k operator and each operator has two integer A[i].x, A[i].y means that you can change the grid matrix[A[i].x][A[i].y] from sea to island. 
# Return how many island are there in the matrix after each operator.
# You need to return an array of size K.

def numIslands2(n, m, operators):
    DIRECTIONS = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    results = []
    island = set()
    size = 0
    father = {}
    
    def union(point_a, point_b):
        nonlocal father, size
        root_a = find(point_a)
        root_b = find(point_b)
        if root_a != root_b:
            father[root_a] = root_b
            size -= 1
    
    def find(spoint):
        nonlocal father
        path = []
        while point != father[point]:
            path.append(point)
            point = father[point]
            
        for p in path:
            father[p] = point
            
        return point
        
    for operator in operators:
        x, y = operator.x, operator.y
        if (x, y) in island:
            results.append(size)
            continue
        
        island.add((x, y))
        father[(x, y)] = (x, y)
        size += 1
        for delta_x, delta_y in DIRECTIONS:
            x_ = x + delta_x
            y_ = y + delta_y
            if (x_, y_) in island:
                union((x_, y_), (x, y))
            
        results.append(size)
        
    return results

