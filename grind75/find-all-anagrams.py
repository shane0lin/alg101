# 438 Find All Anagrams in a String
def findAnagrams(s, p):
    """
    :type s: str
    :type p: str
    :rtype: List[int]
    """
    res = []
    if len(s) < len(p):
        return res
    p_dict = {}
    for c in p:
        p_dict[c] = p_dict.get(c, 0) + 1
    s_dict = {}
    for i in range(len(p)):
        s_dict[s[i]] = s_dict.get(s[i], 0) + 1
    if s_dict == p_dict:
        res.append(0)
    for i in range(len(p), len(s)):
        s_dict[s[i]] = s_dict.get(s[i], 0) + 1
        s_dict[s[i - len(p)]] -= 1
        if s_dict[s[i - len(p)]] == 0:
            del s_dict[s[i - len(p)]]
        if s_dict == p_dict:
            res.append(i - len(p) + 1)
    return res


def findAnagrams2(s, p):
    """
    :type s: str
    :type p: str
    :rtype: List[int]
    """

    rst = []
    if len(s) < len(p):
        return rst
    pd = {}
    for c in p:
        pd[c] = pd.get(c, 0) + 1
    
    l, r = 0, 0
    unmatched = len(pd)
    while r < len(s):
        # print(l,r, s[l:r+1], unmatched)
        # print(pd, rst)

        if s[r] in pd:
            pd[s[r]] -= 1
            if pd[s[r]] == 0:
                unmatched -= 1
            if unmatched == 0:
                rst.append(l)

        # print(pd, rst) 
        r += 1
        if r -l + 1 > len(p):
            if s[l] in pd:
                if pd[s[l]] == 0:
                    unmatched += 1
                pd[s[l]] += 1
            l += 1
    return rst
            
# print(findAnagrams("cbaebabacd", "abc"))
# print(findAnagrams("abab", "ab"))

print(findAnagrams2("cbaebabacd", "abc"))
print(findAnagrams2("abab", "ab"))