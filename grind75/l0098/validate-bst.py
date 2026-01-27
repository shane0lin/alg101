from typing import Optional

from common.tree import TreeNode
from sys import maxsize


def isValidBST(root: Optional[TreeNode]) -> bool:
    
    def valid(root, minv, maxv):
        if not root:
            return True
        if minv >= root.val or root.val >= maxv:
            return False

        return valid(root.left, minv, root.val) and valid(root.right, root.val, maxv)

    
    return valid(root, -maxsize, maxsize)
