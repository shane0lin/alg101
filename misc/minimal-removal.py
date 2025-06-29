# Create a function that determines the minimum number of bracket removals needed for a valid string.
def min_removals_to_balance(brackets):
    # TODO: Initialize an empty list to act as the stack
    stack = []
    count = 0
    # TODO: Iterate through each bracket in the input string
    for ch in brackets:
    
        # TODO: Add conditions to handle the opening and closing brackets appropriately using stack operations
        if ch == "(":
            stack.append(ch)
        elif ch == ")":
            if not stack or stack[-1] == ')':
                count += 1
            else:
                stack.pop
    while stack and stack[-1] == '(':
        count += 1
        stack.pop()
        
    # TODO: Return the count of brackets that need to be removed to make the string valid
    return count

# Example usage
invalid_parentheses = "()))(()"
removals_needed = min_removals_to_balance(invalid_parentheses)
print(removals_needed)  # Expected output: 3