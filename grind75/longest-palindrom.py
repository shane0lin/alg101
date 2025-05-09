# 5 Longest Palindromic Substring
# Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.
# Example 1:
# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
# Example 2:
# Input: "cbbd"
# Output: "bb"
# https://leetcode.com/problems/longest-palindromic-substring/
def longestPalindrome(s):
    """
    :type s: str
    :rtype: str
    """
    # # sol 1
    # if len(s) == 0:
    #     return ""
    # if len(s) == 1:
    #     return s
    # if len(s) == 2:
    #     if s[0] == s[1]:
    #         return s
    #     else:
    #         return s[0]
    # max_len = 0
    # max_str = ""
    # for i in range(len(s)):
    #     for j in range(i+1, len(s)+1):
    #         if s[i:j] == s[i:j][::-1] and len(s[i:j]) > max_len:
    #             max_len = len(s[i:j])
    #             max_str = s[i:j]
    # return max_str

    # sol 2
    if len(s) == 0:
        return ""
    if len(s) == 1:
        return s
    if len(s) == 2:
        if s[0] == s[1]:
            return s
        else:
            return s[0]
    max_len = 0
    max_str = ""


    def max_palindrome(s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l+1:r]
    
    for mid in range(len(s)):
        s1 = max_palindrome(s, mid, mid)
        s2 = max_palindrome(s, mid, mid+1)
        if len(s1) > max_len:
            max_len = len(s1)
            max_str = s1
        if len(s2) > max_len:
            max_len = len(s2)
            max_str = s2
    return max_str

    # sol 3 : Manacher's Algorithm 
    # https://blog.csdn.net/ggggiqnypgjg/article/details/6645824
    # https://www.felix021.com/blog/read.php?2040
    def manacher(s):
        s = '#' + '#'.join(s) + '#'
        p = [0] * len(s)
        mx = 0
        id = 0
        for i in range(len(s)):
            if i < mx:
                p[i] = min(p[2*id-i], mx-i)
            else:
                p[i] = 1
            while i-p[i] >= 0 and i+p[i] < len(s) and s[i-p[i]] == s[i+p[i]]:
                p[i] += 1
            if i + p[i] > mx:
                mx = i + p[i]
                id = i
        return p
    p = manacher(s)
    max_len = max(p)
    max_str = s[p.index(max_len)//2:p.index(max_len)//2+max_len]
    return max_str

print(longestPalindrome("babad"))
print(longestPalindrome("cbbd"))
print(longestPalindrome("a"))
print(longestPalindrome("ac"))
print(longestPalindrome("aacabdkacaa"))