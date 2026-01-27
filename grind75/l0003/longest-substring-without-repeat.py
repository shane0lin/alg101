def lengthOfLongestSubstring(s: str) -> int:
    l, r =0, 0
    unqiue = set([])
    rst = 0
    while r < len(s):
        if s[r] not in unqiue:
            unqiue.add(s[r])
            rst = max(rst, r - l + 1)
 
        else:
            # print(l, r, rst)
            # print(unqiue)
            while s[l] != s[r] and l < r:
                unqiue.remove(s[l])
                l += 1
            if l != r:
                l += 1

        r += 1


    # print(l, r)
    return rst

print(lengthOfLongestSubstring('abcabcbb'))
#abcabcbb
#01234567