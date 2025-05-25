# 49 Group Anagrams
# Given an array of strings, group anagrams together.
# For example, given: ["eat", "tea", "tan", "ate", "nat", "bat"], 
# Return:
# [
#   ["ate", "eat","tea"],
#   ["nat","tan"],
#   ["bat"]
# ]
# Note: All inputs will be in lower-case.
from typing import List
def groupAnagrams(strs) -> List[List[str]]:
    """
    :type strs: List[str]
    :rtype: List[List[str]]
    """
    d = {}
    for s in strs:
        key = ''.join(sorted(s))
        if key in d:
            d[key].append(s)
        else:
            d[key] = [s]
    return list(d.values())

# print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))

print(sorted('eat'))
print(''.join(sorted('eat')))