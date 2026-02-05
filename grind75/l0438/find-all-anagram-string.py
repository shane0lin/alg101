from typing import List
import copy

def findAnagrams(s: str, p: str) -> List[int]:
    rst = []
    if not s or not p:
        return rst
    
    if len(s) < len(p):
        return rst
    
    hm = {}
    for ch in p:
        if ch not in hm:
            hm[ch] = 1
        else:
            hm[ch] += 1

    left, right = 0, 0
    while right < len(s):
        if s[right] not in hm:
            while right < len(s) and s[right] not in hm:
                right += 1
            # if right < len(s):
            #     hm[s[right]] -= 1
            # else:
            #     return rst
        
            while left != right:
                if s[left] in hm:
                    hm[s[left]] += 1
                left += 1        
        
        elif hm[s[right]] == 0:
            if s[left] in hm:
                hm[s[left]] += 1
            left += 1       

        else: # if s[right] in hm and hm[s[right]] > 0:
            hm[s[right]] -= 1
            right += 1
            if right - left == len(p):
                rst.append(left)
                hm[s[left]] += 1
                left += 1
            
    return rst


print(findAnagrams(s = "abab", p = "ab"))
print(findAnagrams( s = "cbaebabacd", p = "abc"))
print(findAnagrams(s="abacbabc", p="abc"))