
def isPalindrome(self, s: str) -> bool:
    if not str:
        return True
    
    left, right = 0, len(s) - 1 

    while left < right:
        if not s[left].isalpha() and not s[left].isdigit():
            left +=1
            continue
        if not s[right].isalpha() and not s[right].isdigit():
            right -=1
            continue

        if s[left].lower() != s[right].lower():
            return False
        else:
            left += 1
            right -= 1
    
    return True
