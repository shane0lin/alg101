#  Simplify simple mathematical expressions by removing all parentheses For example: `"-(a+b-(c-d))"` 
# should be simplified to `"-a-b+c-d"`

# Input:"(a - (b + c) + d)"
# Output: "a- b - c + d"
# Explanation: a - (b + c) + d simplifies to a - b - c + d

# Input:"a - (b - c - (d + e )) - f"
# Output: "a - b + c + d + e - f" 
# Explanation: c - (d + e), to get (c - d - e) The outer - flips the signs, resulting in a - b + c + d + e - f
def simplify_expression(expression: str) -> str:
    rst = ""
    stack = []
    stack.append(1)
    expression = ''.join(expression.split())
    print(expression)


    for i  in range(len(expression)):
        if expression[i] == '(':
            if i > 0 and expression[i-1] == '-':
                stack.append(-stack[-1])
            else:
                stack.append(stack[-1])
        elif expression[i] == ')':
            stack.pop()
        elif expression[i] == '-':
            rst += '-' if stack[-1] == 1 else '+'
        elif expression[i] == '+':
            rst += '+' if stack[-1] == 1 else '-'
        else:
            rst += expression[i]
        # print(rst, stack)
    return rst


def test_simplify_expression():
    # Test case 1: Basic parentheses removal
    assert simplify_expression("(a - (b + c) + d)") == "a - b - c + d"
    
    # Test case 2: Nested parentheses with sign changes
    assert simplify_expression("a - (b - c - (d + e)) - f") == "a - b + c + d + e - f"
    
    # Test case 3: Expression starting with a negative
    assert simplify_expression("-(a+b-(c-d))") == "-a-b+c-d"
    
    # Test case 4: Simple expression
    assert simplify_expression("(a+b)") == "a+b"
    
    # Test case 5: Multiple nested parentheses
    assert simplify_expression("(a-(b-(c-(d-e))))") == "a-b+c-d+e"
    
    # Test case 6: Expression with spaces
    assert simplify_expression("( a + b ) - ( c - d )") == "a + b - c + d"
    
    print("All tests passed!")

# Run the tests
test_simplify_expression()
# print(simplify_expression("(a - (b + c) + d)") )
# print(simplify_expression("a - (b - c - (d + e)) - f"))

