def calculate(s: str) -> int:
    ops_stack = []
    num_stack = []
    cur_num = 0

    def calc(ops_stack, num_stack):
        # if not ops_stack or not num_stack or len(num_stack) < 2:
        #     print('empty')
        #     return
            
        op = ops_stack.pop()
        a = num_stack.pop()
        b = num_stack.pop()
        rst = a + b if op == '+' else b - a
        num_stack.append(rst)
        

    # while index < len(s):
    #     if s[index] == '(':
    #         ops_stack.append('(')
    #     elif s[index] == ')':
    #         num_stack.append(cur_num)
    #         while ops_stack and ops_stack[-1] != '(':
    #             calc(ops_stack, num_stack)
    #         if ops_stack and ops_stack[-1] == '(':
    #             ops_stack.pop()
    #         cur_num = num_stack.pop()
    #     elif s[index].isdigit():
    #         cur_num = cur_num*10 + int(s[index])
    #     elif s[index] == '+' or s[index] == '-':
    #         num_stack.append(cur_num)
    #         cur_num = 0    
    #         while ops_stack and ops_stack[-1] != '(':
    #             calc(ops_stack, num_stack)
    #         ops_stack.append(s[index])
    #     index += 1
    
    for ch in s:
        if ch == '(':
            ops_stack.append('(')
        elif ch == ')':
            num_stack.append(cur_num)
            while ops_stack and ops_stack[-1] != '(':
                calc(ops_stack, num_stack)
            if ops_stack and ops_stack[-1] == '(':
                ops_stack.pop()
            cur_num = num_stack.pop()
        elif ch.isdigit():
            cur_num = cur_num*10 + int(ch)
        elif ch == '+' or ch == '-':
            num_stack.append(cur_num)
            cur_num = 0    
            while ops_stack and ops_stack[-1] != '(':
                calc(ops_stack, num_stack)
            ops_stack.append(ch)




    
    num_stack.append(cur_num)

    while ops_stack:
        calc(ops_stack, num_stack)

    return num_stack[-1]

print(calculate("1 + 1"))
print(calculate(" 2-1 + 2 "))
print(calculate("(1 + 1)"))
print(calculate(" 2-(1 + 2 )"))

print(calculate("(1+(4+5+2)-3)+(6+8)"))
print(calculate("0"))
print(calculate("1-(     -2)"))


