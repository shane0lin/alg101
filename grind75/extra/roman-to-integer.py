# 13 Roman to Integer
# Example 1:

# Input: s = "III"
# Output: 3
# Explanation: III = 3.
# Example 2:

# Input: s = "LVIII"
# Output: 58
# Explanation: L = 50, V= 5, III = 3.
# Example 3:

# Input: s = "MCMXCIV"
# Output: 1994
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
 

# Constraints:

# 1 <= s.length <= 15
# s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
# It is guaranteed that s is a valid roman numeral in the range [1, 3999].


def romanToInt(s: str) -> int:
    val = {
        'I': 1, 
        'V': 5, 
        'X': 10, 
        'L': 50, 
        'C': 100, 
        'D': 500, 
        'M': 1000}
    index = len(s) - 2
    result = val[s[-1]]
    while index >= 0:
        if val[s[index]] >= val[s[index + 1]]:
            result += val[s[index]]
        else:
            result -= val[s[index]]
        index -= 1
    return result
    return 0

print(romanToInt("III"))
print(romanToInt("LVIII")) #58
print(romanToInt("MCMXCIV"))  #1994
print(romanToInt("IV"))  #4
print(romanToInt("IX"))  #9
print(romanToInt("XL"))  #40
print(romanToInt("XC"))  #90
print(romanToInt("CD"))  #400
print(romanToInt("CM"))  #900
print(romanToInt("MMMCMXCIX"))  #3999