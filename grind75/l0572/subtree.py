from typing import Optional
from common.tree import TreeNode


def isSubtree(root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
    def isSameTree(p, q):
        if not p and not q:
            return True
        if not p or not q:
            return False
        
        if p.val == q.bval:
            return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
        return False
    if not root and not subRoot:
        return True
    
    if not root or not subRoot:
        return False
    
    if root.val == subRoot.val:
        if isSameTree(root, subRoot):
            return True
    
    if isSubtree(root.left) or isSubtree(root.right):
        return True
    return False