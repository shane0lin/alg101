"""
Given a list where each index is the max height a tower can be built,
return a list of unique heights where each height <= its max.

[2,3,5,5,5] -> [1,2,3,4,5] (or any valid assignment like [2,3,4,1,5])
[1,2,3] -> [1,2,3]
"""


# Approach 1: Sort by max height, assign ranks
# O(n log n) time, O(n) space
def unique_towers(heights):
    # Sort by max height, keeping original index
    indexed = sorted(enumerate(heights), key=lambda x: x[1])
    result = [0] * len(heights)

    for rank, (orig_idx, max_h) in enumerate(indexed, 1):
        if max_h < rank:
            return None  # impossible
        result[orig_idx] = rank

    return result


# Approach 2: Greedy left-to-right with set
# O(n * max_h) time, O(n) space — simpler to explain in interview
def unique_towers_greedy(heights):
    used = set()
    result = []

    for max_h in heights:
        h = max_h
        while h in used:
            h -= 1
        if h <= 0:
            return None  # impossible
        used.add(h)
        result.append(h)

    return result


print(unique_towers([2, 3, 5, 5, 5]))       # [1, 2, 3, 4, 5]
print(unique_towers([1, 2, 3]))              # [1, 2, 3]

print(unique_towers_greedy([2, 3, 5, 5, 5])) # [2, 3, 5, 4, 1]
print(unique_towers_greedy([1, 2, 3]))        # [1, 2, 3]
