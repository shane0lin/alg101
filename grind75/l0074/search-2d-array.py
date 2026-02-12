from typing import List

def searchMatrix(matrix: List[List[int]], target: int) -> bool:
    m = len(matrix)
    n = len(matrix[0])

    left, right = 0, m*n-1
    while left + 1 < right:
        mid = left + (right - left) // 2
        x = mid // n 
        y = mid % n
        if matrix[x][y] == target:
            return True
        elif matrix[x][y] > target:
            right = mid - 1
        else:
            left = mid + 1
    
    x, y = left // n, left % n
    if matrix[x][y] == target:
        return True
    
    x, y = right // n, right % n
    if matrix[x][y] == target:
        return True
    
    return False

    
    