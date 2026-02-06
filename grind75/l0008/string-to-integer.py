def myAtoi(s: str) -> int:
    rst = 0
    sign = 1
    number_already = False
    for ch in s:
        if ch.isdigit():
            rst = rst * 10 + int(ch)
            if not number_already:
                number_already = True
        elif ch == " ":
            continue
        else:
            if ch.isalpha():
                return rst * sign
            if ch == '-' and not number_already:
                sign = sign * -1
            else:
                return rst*sign
    return rst*sign

print(myAtoi(s = "42"))
print(myAtoi(s = " -042"))
print(myAtoi(s = "1337c0d342"))
print(myAtoi("words and 987"))

