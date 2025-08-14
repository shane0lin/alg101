
#  17   24    1    8   15
#  23    5    7   14   16
#   4    6   13   20   22
#  10   12   19   21    3
#  11   18   25    2    9


def siamese(n=5):
    M = [[0]*n for _ in range(n)]
    i, j = 0, n//2
    for k in range(1, n*n+1):
        M[i][j] = k
        ni, nj = (i-1) % n, (j+1) % n
        if M[ni][nj] != 0:  # 冲突则下移
            i = (i+1) % n
        else:
            i, j = ni, nj
    return M

base = siamese(5)
target = [[x-11 for x in row] for row in base]
for row in target:
    print(" ".join(f"{v:>3}" for v in row))
