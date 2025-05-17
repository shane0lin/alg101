# Add Strings


# Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.
# The length of both num1 and num2 is < 5100.
# Both num1 and num2 contains only digits 0-9.
# Both num1 and num2 does not contain any leading zero.
# You must not use any built-in BigInteger library or convert the inputs to integer directly.
def addStrings(num1, num2):
    """
    :type num1: str
    :type num2: str
    :rtype: str
    """
    if len(num1) < len(num2):
        num1, num2 = num2, num1
    num1 = list(num1)
    num2 = list(num2)
    for i in range(len(num1) - len(num2)):
        num2.insert(0, '0')
    carry = 0
    for i in range(len(num1) - 1, -1, -1):
        num1[i] = str(int(num1[i]) + int(num2[i]) + carry)
        if int(num1[i]) > 9:
            carry = 1
            num1[i] = str(int(num1[i]) - 10)
        else:
            carry = 0
    if carry == 1:
        num1.insert(0, '1')
    print(num1)
    # print(num1.reverse())
    return ''.join(num1)    
print(addStrings('123', '456')) # '579'
# print(addStrings('123', '4567')) # '4690'   
# print(addStrings('123456789', '987654321')) # '1111111110'