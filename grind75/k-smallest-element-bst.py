# 230. Kth Smallest Element in a BST
# https://leetcode.com/problems/kth-smallest-element-in-a-bst/
# Definition for a binary tree node.

import unittest
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



def kthSmallest(root: Optional[TreeNode], k: int) -> int:
    # def inorder(root):
    #     return inorder(root.left) + [root.val] + inorder(root.right) if root else []
    # return inorder(root)[k - 1]

    # sol 2
    stack = []
    while True:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        k -= 1
        if not k:
            return root.val
        root = root.right




# print(kthSmallest([3,1,4,None,2], 1))


class TestKthSmallestElementBST(unittest.TestCase):
    
    def build_tree(self, nodes: List[Optional[int]]) -> Optional[TreeNode]:
        """Helper function to build a tree from a list representation."""
        if not nodes:
            return None
        
        root = TreeNode(nodes[0])
        queue = [root]
        i = 1
        
        while queue and i < len(nodes):
            node = queue.pop(0)
            
            # Left child
            if i < len(nodes) and nodes[i] is not None:
                node.left = TreeNode(nodes[i])
                queue.append(node.left)
            i += 1
            
            # Right child
            if i < len(nodes) and nodes[i] is not None:
                node.right = TreeNode(nodes[i])
                queue.append(node.right)
            i += 1
        
        return root
    
    def test_example_1(self):
        """Test with the first example: [3,1,4,None,2], k=1."""
        root = self.build_tree([3, 1, 4, None, 2])
        self.assertEqual(kthSmallest(root, 1), 1)
    
    def test_example_2(self):
        """Test with the second example: [5,3,6,2,4,None,None,1], k=3."""
        root = self.build_tree([5, 3, 6, 2, 4, None, None, 1])
        self.assertEqual(kthSmallest(root, 3), 3)
    
    def test_single_node(self):
        """Test with a single node tree."""
        root = TreeNode(1)
        self.assertEqual(kthSmallest(root, 1), 1)
    
    def test_left_skewed_tree(self):
        """Test with a left-skewed tree."""
        # Tree: 5 -> 4 -> 3 -> 2 -> 1
        root = TreeNode(5)
        root.left = TreeNode(4)
        root.left.left = TreeNode(3)
        root.left.left.left = TreeNode(2)
        root.left.left.left.left = TreeNode(1)
        
        self.assertEqual(kthSmallest(root, 1), 1)
        self.assertEqual(kthSmallest(root, 3), 3)
        self.assertEqual(kthSmallest(root, 5), 5)
    
    def test_right_skewed_tree(self):
        """Test with a right-skewed tree."""
        # Tree: 1 -> 2 -> 3 -> 4 -> 5
        root = TreeNode(1)
        root.right = TreeNode(2)
        root.right.right = TreeNode(3)
        root.right.right.right = TreeNode(4)
        root.right.right.right.right = TreeNode(5)
        
        self.assertEqual(kthSmallest(root, 1), 1)
        self.assertEqual(kthSmallest(root, 3), 3)
        self.assertEqual(kthSmallest(root, 5), 5)
    
    def test_balanced_tree(self):
        """Test with a balanced binary search tree."""
        # Tree:
        #       4
        #     /   \
        #    2     6
        #   / \   / \
        #  1   3 5   7
        root = self.build_tree([4, 2, 6, 1, 3, 5, 7])
        
        self.assertEqual(kthSmallest(root, 1), 1)
        self.assertEqual(kthSmallest(root, 4), 4)
        self.assertEqual(kthSmallest(root, 7), 7)
    
    def test_k_equals_total_nodes(self):
        """Test when k equals the total number of nodes."""
        root = self.build_tree([3, 1, 4, None, 2])
        self.assertEqual(kthSmallest(root, 4), 4)
    
    def test_duplicate_values(self):
        """Test with duplicate values in the tree (though a proper BST shouldn't have duplicates)."""
        # For this test, we'll manually create a tree that has duplicates
        # Tree:
        #       3
        #     /   \
        #    2     5
        #   /     / 
        #  1     4   
        #       /
        #      3*  (* duplicate value)
        root = TreeNode(3)
        root.left = TreeNode(2)
        root.left.left = TreeNode(1)
        root.right = TreeNode(5)
        root.right.left = TreeNode(4)
        root.right.left.left = TreeNode(3)  # Duplicate value
        
        # The inorder traversal would be [1, 2, 3, 3, 4, 5]
        self.assertEqual(kthSmallest(root, 3), 3)
        self.assertEqual(kthSmallest(root, 4), 3)  # Second occurrence of 3
        self.assertEqual(kthSmallest(root, 5), 4)

if __name__ == "__main__":
    unittest.main()