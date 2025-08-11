# data structure that acts like an in-memory file system. This file system should be able to handle various commands similar to those found in a Unix-style file system. Specifically, the file system should:

# Initialize with no files or directories upon instantiation.

# List all the files and directories at a given directory path, returned in lexicographic order.

# Create new directories given a path, and if necessary, create any intermediate directories along that path.

# Add content to a file at a given path, creating the file if it does not exist, or appending to it if it does.
# Read and return the content from a file at a given path.
# The system must be able to distinguish between file and directory paths and perform actions accordingly.


from typing import List

class TrieNode:
    def __init__(self):
        # Initialize a Trie node with the appropriate attributes
        self.name = None
        self.is_file = False
        self.content = []
        self.children = {}
  
    def insert(self, path: str, is_file: bool) -> 'TrieNode':
        # Insert a path into the Trie and return the final node
        node = self
        parts = path.split('/')
        for part in parts[1:]:  # Skip empty root part
            if part not in node.children:
                node.children[part] = TrieNode()
            node = node.children[part]
        node.is_file = is_file
        if is_file:
            node.name = parts[-1]
        return node
  
    def search(self, path: str) -> 'TrieNode':
        # Search for a node given a path in the Trie
        node = self
        if path == '/':
            return node
        parts = path.split('/')
        for part in parts[1:]: # Skip empty root part
            if part not in node.children:
                return None
            node = node.children[part]
        return node


class FileSystem:
    def __init__(self):
        self.root = TrieNode()

    def ls(self, path: str) -> List[str]:
        # List directory or file
        node = self.root.search(path)
        if node is None:
            return []
        if node.is_file:
            # If it's a file, return a list with its name
            return [node.name]
        # If it's a directory, return the sorted list of children's names
        return sorted(node.children.keys())

    def mkdir(self, path: str) -> None:
        # Create a directory given a path
        self.root.insert(path, False)

    def addContentToFile(self, filePath: str, content: str) -> None:
        # Add content to a file, creating the file if it doesn't exist
        node = self.root.insert(filePath, True)
        node.content.append(content)

    def readContentFromFile(self, filePath: str) -> str:
        # Read content from a file
        node = self.root.search(filePath)
        if node is None or not node.is_file:
            raise FileNotFoundError(f"File not found: {filePath}")
        return ''.join(node.content)