# 150. Evaluate Reverse Polish Notation
# https://leetcode.com/problems/evaluate-reverse-polish-notation/

def evalRPN(tokens):
    stack = []
    for token in tokens:
        if token == "+":
            stack.append(stack.pop() + stack.pop())
        elif token == "-":
            stack.append(-stack.pop() + stack.pop())
        elif token == "*":
            stack.append(stack.pop() * stack.pop())
        elif token == "/":
            stack.append(int(1 / stack.pop() * stack.pop()))
        else:
            stack.append(int(token))
    return stack[0]