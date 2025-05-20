# Generate Parentheses
# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
# For example, given n = 3, a solution set is:
# [
#   "((()))",
#   "(()())",
#   "(())()",
#   "()(())",
#   "()()()"
# ]
# https://leetcode.com/problems/generate-parentheses/
def helper(result, s, left, right):
    if left == 0 and right == 0:
        result.append(s)
        return
    if left > 0:
        helper(result, s + "(", left - 1, right)
    if right > left:
        helper(result, s + ")", left, right - 1)

def generateParenthesis(n):
    """
    :type n: int
    :rtype: List[str]
    """
    result = []
    helper(result, "", n, n)
    return result
print(generateParenthesis(3))   
