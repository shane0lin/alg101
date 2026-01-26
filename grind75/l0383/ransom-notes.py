from collections import defaultdict


def canConstruct(ransomNote: str, magazine: str) -> bool:
    hm = defaultdict(int)
    for ch in magazine:
        hm[ch] += 1
    
    for ch in ransomNote:
        if ch not in hm or hm[ch] == 0:
            return False
        else:
            hm[ch] -= 1
    
    return True
