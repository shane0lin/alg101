# 3 3. Longest Substring Without Repeating Characters
# Given a string s, find the length of the longest substring without duplicate characters.

# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2:

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:

# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

def longest_substring(s):
    if not s:
            return 0
    if len(s) == 1:
        return 1

    l, r = 0, 0
    visited = set()
    max_len = 0
    while r < len(s):
        if s[r] not in visited:
            visited.add(s[r])
            max_len = max(max_len, r-l+1)
        else:
            while s[l] != s[r]:
                visited.remove(s[l])
                l += 1
            l += 1
        r += 1
    return max_len