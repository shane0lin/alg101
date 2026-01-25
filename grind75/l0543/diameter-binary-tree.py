from typing import Optional
from common.tree import TreeNode


def diameterOfBinaryTree(root: Optional[TreeNode]) -> int:
    diameter = 0
    def height(root):
        nonlocal diameter
        if not root:
            return 0
        l_height = height(root.left)
        r_height = height(root.right)
        diameter = max(diameter, l_height + r_height) 

        return max(l_height, r_height) + 1
    height(root)
    
    return diameter