# 76 Minimum Window Substring
import collections


def minWindow(s, t):
    """
    :type s: str
    :type t: str
    :rtype: str
    """
    # sol1
    # if not s or not t:
    #     return ""
    # dict_t = collections.Counter(t)
    # required = len(dict_t)
    # l, r = 0, 0
    # formed = 0
    # window_counts = {}
    # ans = float("inf"), None, None
    # while r < len(s):
    #     character = s[r]
    #     window_counts[character] = window_counts.get(character, 0) + 1
    #     if character in dict_t and window_counts[character] == dict_t[character]:
    #         formed += 1
    #     while l <= r and formed == required:
    #         character = s[l]
    #         if r - l + 1 < ans[0]:
    #             ans = (r - l + 1, l, r)
    #         window_counts[character] -= 1
    #         if character in dict_t and window_counts[character] < dict_t[character]:
    #             formed -= 1
    #         l += 1
    #     r += 1
    # return "" if ans[0] == float("inf") else s[ans[1]:ans[2] + 1]

    # sol2
    if not s or not t:
        return ""
    t_dict = collections.Counter(t)
    required, matched = len(t_dict), 0
    l, r = 0, 0
    rst = float("inf"), None, None # (length, left, right)
    w_dict = {}
    while r < len(s):
        # 1. move right pointer
        # 2. update window dict
        # 3. update matched
        ch = s[r]
        w_dict[ch] = w_dict.get(ch, 0) + 1
        if ch in t_dict and w_dict[ch] == t_dict[ch]:
            matched += 1

        # 4. move left pointer
        while l <= r and matched == required:
            ch = s[l]
            if r - l + 1 < rst[0]:
                rst = (r - l + 1, l, r)
            w_dict[ch] -= 1
            if ch in t_dict and w_dict[ch] < t_dict[ch]:
                matched -= 1
            l += 1
        r += 1

    return "" if rst[0] == float("inf") else s[rst[1]:rst[2] + 1]

print(minWindow("ADOBECODEBANC", "ABC"))
print(minWindow("a", "a"))
print(minWindow("a", "aa"))
print(minWindow("ab", "a"))
print(minWindow("ab", "b"))
print(minWindow("ab", "ab"))
print(minWindow("ab", "ba"))
print(minWindow("ab", "ac"))