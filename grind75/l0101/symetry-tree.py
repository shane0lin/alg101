from typing import Optional
from common.tree import TreeNode

def isSymmetric(root: Optional[TreeNode]) -> bool:

    def helper(p, q):
        if not p and not q:
            return True
        if p and q and q.val == p.val:
            return helper(p.left, q.right) and helper(p.right, q.left)
        return False
    
    if root:
       return helper(root.left, root.right)
    return True
    
