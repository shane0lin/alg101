# Given two binary strings a and b, return their sum as a binary string.
def addBinary(a, b):
    # sol1
    # return bin(int(a, 2) + int(b, 2))[2:]

    # sol2
    i, j = len(a) - 1, len(b) - 1
    carry = 0
    res = ""
    while i >= 0 or j >= 0 or carry:
        if i >= 0:
            carry += int(a[i])
            i -= 1
        if j >= 0:
            carry += int(b[j])
            j -= 1
        res = str(carry % 2) + res
        carry //= 2
    if carry > 0:
        res = "1" + res
    return res