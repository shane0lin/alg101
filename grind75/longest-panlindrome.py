# 409. Longest Palindrome

# Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.

# Letters are case sensitive, for example, "Aa" is not considered a palindrome.
def longestPalindrome(s):
    # count = 0
    # odd = False
    # for i in set(s):
    #     if s.count(i) % 2 == 0:
    #         count += s.count(i)
    #     else:
    #         count += s.count(i) - 1
    #         odd = True
    # if odd:
    #     count += 1
    # return count
    mp = {}
    for ch in s:
        mp[ch] = mp.get(ch, 0) + 1
    count = 0
    odd = False
    for ch in mp:
        if mp[ch] % 2 == 0:
            count += mp[ch]
        else:
            count += mp[ch] - 1
            odd = True
    if odd:
        count += 1
    return count
print(longestPalindrome("abccccdd"))