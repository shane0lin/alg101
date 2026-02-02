def hammingWeight(n: int) -> int:
    rst = 0
    while n:
        rst += n & 1 
        n = n >> 1
    return rst