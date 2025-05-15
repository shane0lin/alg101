# Binary Tree Iterator
# Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.
# Calling next() will return the next smallest number in the BST.
# Note: next() and hasNext() should run in average O(1) time and uses O(h) memory, where h is the height of the tree.
# Credits:
# Special thanks to @ts for adding this problem and creating all test cases.
# Hide Company Tags LinkedIn
# Hide Tags Tree Stack Design
# Hide Similar Problems (M) Binary Search Tree Iterator II (M) Flatten 2D Vector (M) Zigzag Iterator (M) Peeking Iterator (M) Inorder Successor in BST
# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class BSTIterator(object):
    def __init__(self, root):
        self.stack = []
        while root:
            self.stack.append(root)
            root = root.left
    def hasNext(self):
        return len(self.stack) > 0
    def next(self):
        node = self.stack.pop()
        x = node.right
        while x:
            self.stack.append(x)
            x = x.left
        return node