def isPalindrome(x: int) -> bool:
    
    reversed, origin = 0, x

    while x != 0:
        reversed = reversed * 10 + x % 10
        x = x // 10
    
    return origin == reversed 

print(isPalindrome(121))
print(isPalindrome(10))