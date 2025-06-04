# 662 Maximum Width of Binary Tree

import unittest
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Note: Since the function is defined as a method, I'll create a Solution class to hold it
class Solution:
    def widthOfBinaryTree(self, root):
        # if not root: return 0
        # queue = [(root, 0, 0)]
        # cur_depth = left = ans = 0
        # for node, depth, pos in queue:
        #     if node:
        #         queue.append((node.left, depth+1, pos*2))
        #         queue.append((node.right, depth+1, pos*2 + 1))
        #         if cur_depth != depth:
        #             cur_depth = depth
        #             left = pos
        #         ans = max(pos - left + 1, ans)
        # return ans


        # sol2
        if not root:
            return 0
        que = [(root, 0, 0)] # node, depth, pos
        cur_depth = left = rst = -1
        while que:
            size = len(que)
            for i in range(size):
                node, depth, pos = que.pop(0)
                if node.left:
                    que.append((node.left, depth+1, pos*2))
                if node.right:
                    que.append((node.right, depth+1, pos*2+1))
                if cur_depth != depth: # first node in this level
                    cur_depth = depth
                    left = pos
                rst = max(rst, pos-left+1)
        return rst

class TestMaxWidthBinaryTree(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_empty_tree(self):
        """Test with an empty tree"""
        self.assertEqual(self.solution.widthOfBinaryTree(None), 0)
    
    def test_single_node(self):
        """Test with a single node tree"""
        root = TreeNode(1)
        self.assertEqual(self.solution.widthOfBinaryTree(root), 1)
    
    def test_complete_binary_tree(self):
        """Test with a complete binary tree
              1
             / \
            3   2
           / \
          5   3
        """
        root = TreeNode(1)
        root.left = TreeNode(3)
        root.right = TreeNode(2)
        root.left.left = TreeNode(5)
        root.left.right = TreeNode(3)
        self.assertEqual(self.solution.widthOfBinaryTree(root), 2)
    
    def test_full_binary_tree(self):
        """Test with a full binary tree
              1
             / \
            3   2
           / \  / \
          5  3 9  7
        """
        root = TreeNode(1)
        root.left = TreeNode(3)
        root.right = TreeNode(2)
        root.left.left = TreeNode(5)
        root.left.right = TreeNode(3)
        root.right.left = TreeNode(9)
        root.right.right = TreeNode(7)
        self.assertEqual(self.solution.widthOfBinaryTree(root), 4)
    
    def test_skewed_tree(self):
        """Test with a left-skewed tree
              1
             /
            3
           /
          5
        """
        root = TreeNode(1)
        root.left = TreeNode(3)
        root.left.left = TreeNode(5)
        self.assertEqual(self.solution.widthOfBinaryTree(root), 1)
    
    def test_sparse_tree(self):
        """Test with a sparse tree with gaps
              1
             / \
            3   2
               /
              9
        """
        root = TreeNode(1)
        root.left = TreeNode(3)
        root.right = TreeNode(2)
        root.right.left = TreeNode(9)
        self.assertEqual(self.solution.widthOfBinaryTree(root), 2)

if __name__ == '__main__':
    unittest.main()

