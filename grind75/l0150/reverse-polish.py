# Example 1:

# Input: tokens = ["2","1","+","3","*"]
# Output: 9
# Explanation: ((2 + 1) * 3) = 9
# Example 2:

# Input: tokens = ["4","13","5","/","+"]
# Output: 6
# Explanation: (4 + (13 / 5)) = 6
# Example 3:

# Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
# Output: 22

def evalRPN(tokens: list[str]) -> int:
    stack = []
    for token in tokens:
        if token.lstrip('-').isdigit():
            stack.append(int(token))
        else:
            a = stack.pop()
            b = stack.pop()
            if token == '+':
                stack.append(int(a) + int(b))
            elif token == '-':
                stack.append(int(b) - int(a))
            
            elif token == '*':
                stack.append(int(a) * int(b))
            elif token == '/':
                stack.append(int(b/a))
    return stack[-1] 

# print(evalRPN(tokens=["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))
print(evalRPN(["4","13","5","/","+"]))