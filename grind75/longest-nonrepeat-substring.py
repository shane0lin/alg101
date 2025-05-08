# 3 3. Longest Substring Without Repeating Characters
# Given a string s, find the length of the longest substring without duplicate characters.

# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2:

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:

# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

import unittest

def longest_substring(s):
    if not s:
            return 0
    if len(s) == 1:
        return 1

    l, r = 0, 0
    visited = set()
    max_len = 0
    while r < len(s):
        if s[r] not in visited:
            visited.add(s[r])
            max_len = max(max_len, r-l+1)
        else:
            while s[l] != s[r]:
                visited.remove(s[l])
                l += 1
            l += 1
        r += 1
    return max_len

class TestLongestSubstring(unittest.TestCase):
    
    def test_empty_string(self):
        self.assertEqual(longest_substring(""), 0)
    
    def test_single_character(self):
        self.assertEqual(longest_substring("a"), 1)
    
    def test_all_same_characters(self):
        self.assertEqual(longest_substring("bbbbb"), 1)
    
    def test_no_repeating_characters(self):
        self.assertEqual(longest_substring("abcdef"), 6)
    
    def test_example_one(self):
        self.assertEqual(longest_substring("abcabcbb"), 3)
    
    def test_example_two(self):
        self.assertEqual(longest_substring("bbbbb"), 1)
    
    def test_example_three(self):
        self.assertEqual(longest_substring("pwwkew"), 3)
    
    def test_repeating_at_end(self):
        self.assertEqual(longest_substring("abcdefd"), 6)
    
    def test_repeating_at_beginning(self):
        self.assertEqual(longest_substring("aabcdef"), 6)
    
    def test_complex_case(self):
        self.assertEqual(longest_substring("dvdf"), 3)
    
    def test_another_complex_case(self):
        self.assertEqual(longest_substring("anviaj"), 5)
    
    def test_with_spaces(self):
        self.assertEqual(longest_substring("hello world"), 6)  # "world " is 6 characters

if __name__ == "__main__":
    unittest.main()