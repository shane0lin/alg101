def backspaceCompare(s: str, t: str) -> bool:
    i, j = len(s) - 1, len(t) - 1
    while i>=0 or j>=0:
        skip_count_s = 0
        while i>=0:
            if s[i] == '#':
                skip_count_s += 1
                i -= 1
            elif skip_count_s > 0:
                i -= 1
                skip_count_s -= 1
            else:
                break # find a character, and not backspace now
        skip_count_t = 0
        while j>=0:
            if t[j] == '#':
                skip_count_t += 1
                j -= 1
            elif skip_count_t > 0:
                j -= 1
                skip_count_t -= 1
            else:
                break # find a chacter, and not backspace
        
        if i>=0 and j >= 0 and s[i] != t[j]: # both are not ended
            return False
        elif i>=0 and j < 0 or j>=0 and i <0: # One string ended
            return False
        i -= 1
        j -= 1
    return True

print(backspaceCompare("ab#c", "ad#c"))    
print(backspaceCompare("a", "aa#a"))    