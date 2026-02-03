from typing import List


def spiralOrder(matrix: List[List[int]]) -> List[int]:
    rst = []
    if not matrix or not matrix[0]:
        return rst
    
    up, left = 0, 0
    down, right = len(matrix)-1, len(matrix[0])-1
    di = 0; # 0: left; 1: down; 2: right; 3: go up
    
    while True:
        if di == 0:
            for i in range(left, right + 1):
                rst.append(matrix[up][i])
            up += 1
        elif di == 1:
            for i in range(up, down + 1):
                rst.append(matrix[i][right])
            right -= 1
        elif di == 2:
            for i in range(right, left - 1, -1):
                rst.append(matrix[down][i])
            down -= 1
        elif di == 3:
            for i in range(down, up - 1, -1):
                rst.append(matrix[i][left])
            left += 1
        
        if up > down or left > right:
            return rst
        di = (di + 1) % 4


# print(spiralOrder([[ 1, 2, 3 ], [ 4, 5, 6 ], [ 7, 8, 9 ]])) # [1,2,3,6,9,8,7,4,5]
# print(spiralOrder([[ 6,4,1 ], [ 7,8,9 ]])) # [6,4,1,9,8,7]
print(spiralOrder([[7],[9],[6]]))