# 692 Top K Frequent Words
# Given a non-empty list of words, return the k most frequent elements.
# Your answer should be sorted by frequency from highest to lowest. If two words have the same frequency, then the word with the lower alphabetical order comes first.
# Example 1:
# Input: ["i", "love", "leetcode", "i", "love", "coding"], k = 2
# Output: ["i", "love"]
# Explanation: "i" and "love" are the two most frequent words.
#     Note that "i" comes before "love" due to a lower alphabetical order.
# Example 2:
# Input: ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k = 4
# Output: ["the", "is", "sunny", "day"]
# Explanation: "the", "is", "sunny" and "day" are the four most frequent words,
#     with the number of occurrence being 4, 3, 2 and 1 respectively.
# Note:
# You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
# Input words contain only lowercase letters.
# Follow up:
# Try to solve it in O(n log k) time and O(n) extra space.
# Solution 1: Using a heap
# Time: O(nlogk)
# Space: O(n)
import heapq
from collections import Counter
from typing import List
from functools import cmp_to_key

def compare(a, b):
    if a[0] > b[0] or a[0] == b[0] and a[1] < b[1]:
        return -1
    elif  a[0] == b[0] and a[1] == b[1]:
        return 0
    else:
        return 1

def topKFrequent(words: List[str], k: int) -> List[str]:
    count = Counter(words)
    tmp = []
    for word, freq in count.items():
        tmp.append((freq, word))
    
    # tmp.sort(key =lambda x: compare(x))
    tmp = sorted(tmp, key = cmp_to_key(compare))
    rst = []
    for i in range(k):
        rst.append(tmp[i][1])
    return rst
    
print(topKFrequent(["i", "love", "leetcode", "i", "love", "coding"], 2)) # ["i", "love"]
print(topKFrequent(["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], 4))