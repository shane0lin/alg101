class TrieNode:
    def __init__(self, val=None):
        self.children = {}
        self.isword=False
        self.val = val

class Trie:

    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node.children:
                new_node = TrieNode(ch)
                node.children[ch] = new_node
            node = node.children[ch]
        node.isword = True
        

    def search(self, word: str) -> bool:
        node = self.root
        for ch in word:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return node.isword
        

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return True