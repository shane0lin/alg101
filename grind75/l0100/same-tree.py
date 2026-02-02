from typing import Optional

from common.tree import TreeNode


def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    if not p and not q:
        return True
    if not p or not q:
        return False
    
    if p.val == q.val:
        return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
    return False
