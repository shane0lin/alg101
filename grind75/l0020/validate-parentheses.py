def isValid(s: str) -> bool:
    if not str:
        return True
    
    stack = []
    hp = { ')' : '(', ']': '[', '}' : '{'}
    for ch in s:
        if ch in '([{':
            stack.append(ch)
        elif ch in ')}]':
            if not stack or stack[-1] != hp[ch]:
                return False
            else:
                stack.pop()
    return not stack

print(isValid(s = "()"))
print(isValid(s = "()[]{}"))
print(isValid(s="(]"))
print(isValid(s="("))
