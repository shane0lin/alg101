from typing import List


def wordBreak(s: str, wordDict: List[str]) -> bool:
    dp = [False] * (len(s) + 1)
    dp[0] = True
    wordSet = set(wordDict)

    max_l = max([len(word) for word in wordDict])

    for i in range(1, len(s)+1):
        for j in range(1, max_l+1):
            if i < j:
                continue
            if not dp[i-j]:
                continue
            word = s[i-j:i]
            if word in wordSet:
                dp[i] = True
                break
    # print(dp)
    return dp[len(s)]
    # return False



print(wordBreak(s = "leetcode", wordDict = ["leet","code"]))
# print(wordBreak())
# print(wordBreak())
# print(wordBreak())
# print(wordBreak())
