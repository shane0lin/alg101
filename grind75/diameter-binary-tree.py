# 543. Diameter of Binary Tree
# Given the root of a binary tree, return the length of the diameter of the tree.

# The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

# The length of a path between two nodes is represented by the number of edges between them.



class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def diameterOfBinaryTree(root: TreeNode) -> int:
    diameter = 1
    def depth(node):
        nonlocal diameter
        if not node:
            return 0
        left = depth(node.left)
        right = depth(node.right)
        diameter = max(diameter, left + right + 1)
        return max(left, right) + 1
    depth(root)
    # We subtract 1 from diameter because the diameter is defined as the number of edges
    # between the two farthest nodes, but in our depth calculation we counted nodes.
    # Since the number of edges is always one less than the number of nodes in a path,
    # we need to subtract 1 from our result.
    return diameter - 1