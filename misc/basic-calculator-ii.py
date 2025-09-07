# Basic Calculator II

def calculate(s):
    stack = []
    num = 0
    sign = '+'
    # invariance : stack is always positive, num is always positive
    # sign is always the sign of the next number
    for i in range(len(s)):
        if s[i].isdigit():
            num = num * 10 + int(s[i])
        # print(s[i], num, sign)
        if s[i] in '+-*/' or i == len(s) - 1:
            print(s[i], num, stack, sign)
            if sign == '+':
                stack.append(num)
            elif sign == '-':
                stack.append(-num)
            elif sign == '*':
                print("---")
                print(num, stack)
                stack.append(stack.pop() * num)
            elif sign == '/':
                stack.append(int(stack.pop() / num))
            sign = s[i]
            num = 0
        # print(stack)
    return sum(stack)


print(calculate("3+2*5"))
# print(calculate(" 3/2 "))
# print(calculate(" 3+5 / 2 "))