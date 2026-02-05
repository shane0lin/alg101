def reverseBits(n: int) -> int:
    rst = 0
    count = 32

    while n:
        bit = n & 1
        rst = (rst << 1) + bit
        n = n >> 1
        count -= 1
        print(bit, rst, n)
    
    while count > 0:
        rst = rst << 1
        count -= 1
    

    return rst

print(reverseBits(43261596))