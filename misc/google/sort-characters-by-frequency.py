# Sort Characters By Frequency
# Given a string, sort it in decreasing order based on the frequency of characters.
# Example 1:
# Input:
# "tree"
# Output:
# "eert"
# Explanation:
# 'e' appears twice while 'r' and 't' both appear once.
# So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
# Example 2:
# Input:
# "cccaaa"
# Output:
# "cccaaa"
# Explanation:
# Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.
# Note that "cacaca" is incorrect, as the same characters must be together.
# Example 3:
# Input:
# "Aabb"
# Output:
# "bbAa"
# Explanation:
# "bbaA" is also a valid answer, but "Aabb" is incorrect.
# Note that 'A' and 'a' are treated as two different characters.
def frequencySort(s):
    d = {}
    for i in s:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1
    d = sorted(d.items(), key=lambda x: x[1], reverse=True)
    res = ''
    for i in d:
        res += i[0] * i[1]
    return res
print(frequencySort('tree'))