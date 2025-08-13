# 101. Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).
def isSymmetric(root: Optional[TreeNode]) -> bool:
    if not root:
        return True
    def isMirror(left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
        if not left and not right:
            return True
        if not left or not right:
            return False
        return (left.val == right.val) and isMirror(left.left, right.right) and isMirror(left.right, right.left)
    return isMirror(root.left, root.right)