# Given string num representing a non-negative integer num, and an integer k, return the smallest possible integer after removing k digits from num.

 

# Example 1:

# Input: num = "1432219", k = 3
# Output: "1219"
# Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.
# Example 2:

# Input: num = "10200", k = 1
# Output: "200"
# Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.
# Example 3:

# Input: num = "10", k = 2
# Output: "0"
# Explanation: Remove all the digits from the number and it is left with nothing which is 0.

def remove_k_digits(num: str, k: int) -> str:
    stack = []
    for digit in num:
        while k > 0 and stack and stack[-1] > digit:
            stack.pop()
            k -= 1
        stack.append(digit)
    
    # If there are still digits to remove, remove them from the end
    final_stack = stack[:-k] if k > 0 else stack
    
    # Join the stack and remove leading zeros
    result = ''.join(final_stack).lstrip('0')
    
    # If the result is empty, return "0"
    return result if result else "0"

# Test cases
assert remove_k_digits("1432219", 3) == "1219"
assert remove_k_digits("10200", 1) == "200"
assert remove_k_digits("10", 2) == "0"
# Time complexity: O(n) where n is the length of the input string 'num'.
# We iterate through each digit once and each digit can be pushed and popped from the stack at most once.
