from typing import Optional

from common.tree import TreeNode

def invertTree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    if not root:
        return
    
    left = invertTree(root.left)
    right = invertTree(root.right)
    root.left = right
    root.right = left

    return root

