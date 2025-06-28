# There is a new alien language which uses the latin alphabet. 
# However, the order among letters are unknown to you. You receive a list of non-empty words from the dictionary, 
# where words are sorted lexicographically by the rules of this new language. 
# Derive the order of letters in this language.
# ex1
# Input:
# [
#   "wrt",
#   "wrf",
#   "er",
#   "ett",
#   "rftt"
# ]

# Output: "wertf"

# Example 2:

# Input:
# [
#   "z",
#   "x"
# ]

# Output: "zx"
# Example 3:

# Input:
# [
#   "z",
#   "x",
#   "z"
# ]

# Output: "" 

# Explanation: The order is invalid, so return "".

from collections import defaultdict, deque

def alien_order(words):
    # from collections import defaultdict, deque
    # # Step 1: Create a graph and in-degree map
    # graph = defaultdict(set)
    # in_degree = {char: 0 for word in words for char in word}
    # # Step 2: Build the graph
    # for i in range(len(words) - 1):
    #     word1, word2 = words[i], words[i + 1]
    #     min_length = min(len(word1), len(word2))
    #     for j in range(min_length):
    #         if word1[j] != word2[j]:
    #             if word2[j] not in graph[word1[j]]:
    #                 graph[word1[j]].add(word2[j])
    #                 in_degree[word2[j]] += 1
    #             break
    #     else:
    #         # If we didn't find a differing character and word1 is longer than word2, it's invalid
    #         if len(word1) > len(word2):
    #             return ""
    # # Step 3: Topological sort using Kahn's algorithm
    # queue = deque([char for char in in_degree if in_degree[char] == 0])
    # result = []
    # while queue:
    #     char = queue.popleft()
    #     result.append(char)
    #     for neighbor in graph[char]:
    #         in_degree[neighbor] -= 1
    #         if in_degree[neighbor] == 0:
    #             queue.append(neighbor)
    # # If the result contains all characters, return it; otherwise, there's a cycle
    # return ''.join(result) if len(result) == len(in_degree) else ""
    if not words:
        return ''
    if len(words) == 1:
        return words[0]

    graph = defaultdict(set)
    indegree = {char: 0 for word in words for char in word}
    prev = words[0]
    for i in range(1, len(words)):
        next_ = words[i]
        j = 0
        l = min(len(prev), len(next_))
        while j < l and prev[j] == next_[j]:
            j += 1
        if j < l:
            if prev[j] in graph[next_[j]]:
                return ''
            graph[prev[j]].add(next_[j])
            indegree[next_[j]] += 1
        else:
            if len(prev) > len(next_):
                return ''
        prev = next_
    
    # print(graph)
    # print(indegree)
    
    source = deque()
    for k, v in indegree.items():
        if v == 0:
            source.append(k)
    # print(source)
    
    rst = []
    while source:
        parent = source.popleft()
        rst.append(parent)
        for child in graph[parent]:
            indegree[child] -= 1
            if indegree[child] == 0:
                source.append(child)
    if len(rst) != len(indegree):
        return ''
    return ''.join(rst)

print(alien_order(["z", "o"]))
print(alien_order(words=["wrtkj","wrt"]))
print(alien_order(words=["mnop","nopq","opqr","pqrs","qrst","rstu","stuv","tuvw","uvwx","vwxy","wxyz","xyz","yz","z","mnopqr","nopqrs","opqrst","pqrstu","qrstuv","rstuvw","stuvwx","tuvwxy","uvwxyz","vwxyz","wxyza","xyzab","yzabc","zabcd"]))