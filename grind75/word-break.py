# 139. Word Break
# https://leetcode.com/problems/word-break/
def wordBreak(s, wordDict):
    # dp = [False] * (len(s) + 1)
    # dp[len(s)] = True
    # for i in range(len(s) - 1, -1, -1):
    #     for w in wordDict:
    #         if (i + len(w)) <= len(s) and s[i:i + len(w)] == w:
    #             dp[i] = dp[i + len(w)]
    #         if dp[i]:
    #             break
    # return dp[0]

    dp = [False] * (len(s) + 1) # dp[i] means s[:i] can be segmented into words in the wordDicts
    dp[0] = True
    for i in range(1, len(s) + 1):
        for w in wordDict:
            if i >= len(w) and dp[i - len(w)] and s[i - len(w):i] == w:
                dp[i] = True
    return dp[len(s)]

print(wordBreak("leetcode", ["leet", "code"]))
print(wordBreak("applepenapple", ["apple", "pen"]))
print(wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]))