# 997 Find the Town Judge
# In a town, there are n people labeled from 1 to n. There is a rumor that one of these people is secretly the town judge.

# If the town judge exists, then:

# The town judge trusts nobody.
# Everybody (except for the town judge) trusts the town judge.
# There is exactly one person that satisfies properties 1 and 2.
# You are given an array trust where trust[i] = [ai, bi] representing that the person labeled ai trusts the person labeled bi. If a trust relationship does not exist in trust array, then such a trust relationship does not exist.

# Return the label of the town judge if the town judge exists and can be identified, or return -1 otherwise.

 

# Example 1:

# Input: n = 2, trust = [[1,2]]
# Output: 2
# Example 2:

# Input: n = 3, trust = [[1,3],[2,3]]
# Output: 3
# Example 3:

# Input: n = 3, trust = [[1,3],[2,3],[3,1]]

from typing import List
def find_judge(n: int, trust: List[List[int]]) -> int:
    # Initialize trust counts
    trust_count = [0] * (n + 1)

    # Process each trust relationship
    for a, b in trust:
        trust_count[a] -= 1  # Person a trusts someone, so decrement their count
        trust_count[b] += 1  # Person b is trusted, so increment their count
    # Find the person who is trusted by everyone else and trusts nobody
    for i in range(1, n + 1):
        if trust_count[i] == n - 1:
            return i
    return -1


# Example usage
assert find_judge(2, [[1, 2]]) == 2
assert find_judge(3, [[1, 3], [2, 3]]) == 3
assert find_judge(3, [[1, 3], [2, 3], [3, 1]]) == -1