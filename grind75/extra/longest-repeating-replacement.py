# 424. Longest Repeating Character Replacement
# Medium
# 8.9K
# 355
# Companies
# You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.
# Return the length of the longest substring containing the same letter you can get after performing the above operations.






def character_replacement(s: str, k: int) -> int:
    max_length = 0
    max_count = 0
    left = 0
    char_count = {}
    for right in range(len(s)):
        ch = s[right]

        char_count[ch] = char_count.get(ch, 0) + 1
        max_count = max(max_count, char_count[ch])
        while (right - left + 1) - max_count > k:
            char_count[s[left]] -= 1
            
            left += 1
        max_length = max(max_length, right - left + 1)
    return max_length



print(character_replacement("AABABBA", 1))  # Output: 4