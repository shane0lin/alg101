from typing import List


def rotate(matrix: List[List[int]]) -> None:
    n = len(matrix)

    # flip up side down
    for i in range(n >> 1):
        for j in range(n):
            matrix[i][j], matrix[n-i-1][j] = matrix[n-i-1][j], matrix[i][j]
    
    for i in range(n):
        for j in range(i):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    print(matrix)



rotate(matrix=[[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]])  #[[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
