def minRemoveToMakeValid(s: str) -> str:
    stack = []
    balanced = 0
    for ch in s:
        if ch == ')' and balanced == 0:
            continue
        if ch == '(':
            balanced += 1
        elif ch == ')':
            balanced -= 1
        stack.append(ch)
    
    rst = []
    balanced = 0
    for ch in stack[::-1]:
        if ch == '(' and balanced == 0:
            continue
        if ch == ')':
            balanced += 1
        elif ch == '(' :
            balanced -=1
        rst.append(ch)
    return ''.join(rst[::-1])

print(minRemoveToMakeValid(s ="))(("))