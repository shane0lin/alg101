

from typing import Optional

from common.tree import TreeNode


def maxDepth(root: Optional[TreeNode]) -> int:
    if not root:
        return 0
    
    l_dep = maxDepth(root.left)
    r_dep = maxDepth(root.right)

    return max(l_dep, r_dep) + 1
    
