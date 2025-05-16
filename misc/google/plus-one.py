# Plus One
# Given a non-negative number represented as an array of digits, plus one to the number.Returns a new array.

# The number is arranged according to the number of digits, with the highest digit at the top of the list.

def plusOne(digits):
    """
    :type digits: List[int]
    :rtype: List[int]
    """
    digits[-1] += 1
    for i in range(len(digits) - 1, 0, -1):
        if digits[i] == 10:
            digits[i] = 0
            digits[i - 1] += 1
    if digits[0] == 10:
        # print(digits)
        digits[0] = 0
        digits.insert(0, 1)
    return digits

print(plusOne([9,9,9])) # [1,0,0,0]
print(plusOne([1,2,3])) # [1,2,4]