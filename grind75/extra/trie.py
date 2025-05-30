# 211 Design Add and Search Words Data Structure

class WordDictionary(object):
    def __init__(self):
        self.root = {}


    def addWord(self, word):
        node = self.root
        for c in word:
            if c not in node:
                node[c] = {}
            node = node[c]
        node['#'] = True


    def search(self, word):
        return self.searchHelper(self.root, word)
    

    def searchHelper(self, node, word):
        if not word:
            return '#' in node
        c = word[0]
        if c == '.':
            for key in node:
                if self.searchHelper(node[key], word[1:]):
                    return True
        else:
            if c in node:
                return self.searchHelper(node[c], word[1:])
        return False


import unittest
from trie import WordDictionary

class TestWordDictionary(unittest.TestCase):
    def setUp(self):
        self.word_dict = WordDictionary()

    def test_add_and_search_single_word(self):
        self.word_dict.addWord("hello")
        self.assertTrue(self.word_dict.search("hello"))
        self.assertFalse(self.word_dict.search("hell"))
        self.assertFalse(self.word_dict.search("helloo"))

    def test_add_and_search_multiple_words(self):
        words = ["bad", "dad", "mad"]
        for word in words:
            self.word_dict.addWord(word)
        
        for word in words:
            self.assertTrue(self.word_dict.search(word))
        
        self.assertFalse(self.word_dict.search("pad"))
        self.assertFalse(self.word_dict.search("ba"))

    def test_empty_word(self):
        self.word_dict.addWord("")
        self.assertTrue(self.word_dict.search(""))

    def test_case_sensitivity(self):
        self.word_dict.addWord("Hello")
        self.assertTrue(self.word_dict.search("Hello"))
        self.assertFalse(self.word_dict.search("hello"))

    def test_word_with_special_characters(self):
        self.word_dict.addWord("hello!")
        self.assertTrue(self.word_dict.search("hello!"))
        self.assertFalse(self.word_dict.search("hello"))

    # The following tests will fail with the current implementation
    # because it doesn't support wildcard searches
    
    def test_search_with_dot_wildcard(self):
        """Test searching with dot as wildcard - will fail with current implementation"""
        self.word_dict.addWord("bad")
        self.word_dict.addWord("dad")
        self.word_dict.addWord("mad")
        
        # These should match but will fail with current implementation
        self.assertTrue(self.word_dict.search(".ad"))
        self.assertTrue(self.word_dict.search("b.."))
        self.assertTrue(self.word_dict.search("..."))

    def test_search_with_multiple_wildcards(self):
        """Test searching with multiple wildcards - will fail with current implementation"""
        self.word_dict.addWord("hello")
        self.word_dict.addWord("world")
        
        # These should match but will fail with current implementation
        self.assertTrue(self.word_dict.search("h.ll."))
        self.assertTrue(self.word_dict.search("w..ld"))


if __name__ == "__main__":
    unittest.main()