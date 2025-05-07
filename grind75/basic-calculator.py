# 224 Basic Calculator
def calculate(s):
    stack = [] # 
    rst = 0 # current rst
    num = 0 # current number
    sign = 1
 
    for ch in s:
        if ch.isdigit():
            num = num * 10 + int(ch)
        elif ch == '+':
            rst += num * sign
            num = 0
            sign = 1
        elif ch == '-':
            rst += num * sign
            num = 0
            sign = -1
            
        elif ch == '(':
            stack.append(rst)
            stack.append(sign)
            sign = 1
            rst = 0
            num = 0

        elif ch == ')':
            rst += num * sign
            num = 0
            rst *= stack.pop() # sign
            rst += stack.pop() # rst

    print(stack, num, rst)
    return rst + num * sign

    

print(calculate("1 + 1"))
print(calculate(" 2-1 + 2 "))
print(calculate("(1+(4+5+2)-3)+(6+8)"))