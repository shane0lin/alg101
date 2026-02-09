from collections import deque

def calculate(s: str) -> int:
    num_s = deque([])
    op_s = deque([])

    cur_num = 0
    for ch in s:
        if ch == '+' or ch == '-':
            if not op_s or op_s[-1] == '+' or op_s[-1] == '-':
                op_s.append(ch)
                num_s.append(cur_num)
                cur_num = 0

            else: # previous "*/"
                prev_num = num_s.pop()
                cur_num = int(prev_num / cur_num) if op_s[-1] == '/' else prev_num * cur_num
                op_s.pop()
                op_s.append(ch)
                num_s.append(cur_num)
                cur_num = 0
        
        elif ch == '*' or ch == '/':
            if op_s and (op_s[-1] == '*' or op_s[-1] == '/'):
                op = op_s.pop()
                prev_num = num_s.pop()
                cur_num = int(prev_num/cur_num) if op == '/' else prev_num * cur_num      
            op_s.append(ch)
            num_s.append(cur_num)
            cur_num = 0
        elif ch.isdigit():
            cur_num = cur_num * 10 + int(ch)
        elif ch == ' ':
            continue

    if op_s[-1] == '*' or op_s[-1] == '/':
        prev_num = num_s.pop()
        op = op_s.pop()
        cur_num = int(prev_num/cur_num) if op == '/' else prev_num * cur_num        
    
    
    num_s.append(cur_num)                                                                                                                                                                                 
    cur_num = num_s.popleft()
    while op_s:
        op = op_s.popleft()
        next_num = num_s.popleft()
        cur_num = cur_num - next_num if op == '-' else next_num + cur_num

        
    return int(cur_num)

# print(calculate(s = "3+2*2"))
# print(calculate(s = " 3/2 "))
# print(calculate(s = " 3+5 / 2 "))
# print(calculate(s ="0-2147483647"))
# print(calculate(s="1-2+3"))
# print(calculate("14/3*2"))
# 7
# 1
# 5
# -2147483647
# 2
# 8
print(calculate("1*2-3/4+5*6-7*8+9/10"))