# 383. Ransom Note

# Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

# Each letter in magazine can only be used once in ransomNote.
def canConstruct(ransomNote: str, magazine: str) -> bool:
    mp = {}
    for i in magazine:
        if i in mp:
            mp[i] += 1
        else:
            mp[i] = 1
    for i in ransomNote:
        if i in mp and mp[i] > 0:
            mp[i] -= 1
        else:
            return False
    return True

