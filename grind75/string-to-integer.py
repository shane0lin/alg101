# 8 String to Integer (atoi)
# https://leetcode.com/problems/string-to-integer-atoi/
def myAtoi(s: str) -> int:
    s = s.strip()
    if not s:
        return 0
    sign = 1
    if s[0] == '-':
        sign = -1
        s = s[1:]
    elif s[0] == '+':
        s = s[1:]
    res = 0
    for c in s:
        if not c.isdigit():
            break
        res = res * 10 + int(c)
    res *= sign
    if res > 2 ** 31 - 1:
        return 2 ** 31 - 1
    elif res < -2 ** 31:
        return -2 ** 31
    else:
        return res
print(myAtoi("42"))
print(myAtoi("   -42"))
print(myAtoi("4193 with words"))
print(myAtoi("words and 987"))
print(myAtoi("-91283472332"))