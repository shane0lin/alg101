# Example 1:

# Input: a = "11", b = "1"
# Output: "100"
# Example 2:

# Input: a = "1010", b = "1011"
# Output: "10101"
def addBinary(a: str, b: str) -> str:
    def add(a: int, b: int, carryover: int):
        rst = a + b + carryover
        if rst==3:
            return (1, 1)
        elif rst == 2:
            return (1, 0)
        elif rst == 0:
            return (0, 0)
        else:
            return (0, 1)
        
    cha = list(a)[::-1]
    chb = list(b)[::-1]
    la = len(cha)
    lb = len(chb)
    rst = []

    carryover = 0
    i = 0
    while i < min(la, lb):
        carryover, num = add(int(cha[i]), int(chb[i]), carryover)
        rst.append(num)
        i += 1
    
    if i < len(a):
        for j in range(i, len(a)):
            carryover, num = add(int(cha[j]), 0, carryover)
            rst.append(num)
    else:
        for j in range(i, len(b)):
            carryover, num = add(int(chb[j]), 0, carryover)
            rst.append(num)

    
    if carryover:
        rst.append(carryover)
        
    rst = rst[::-1]

    return ''.join(str(n) for n in rst)

# print(addBinary(a = "11", b = "1"))
# print(addBinary(a = "1010", b = "1011"))
# print(addBinary(a = "1", b = "111"))
print(addBinary(a = "1111", b = "1111"))

