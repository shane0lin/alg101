
from typing import Optional

from common.tree import TreeNode


def isBalanced(root: Optional[TreeNode]) -> bool:
    
    def tree_height(root) -> tuple[bool, int]:
        if not root:
            return True, 0
        
        if not root.left and not root.right:
            return True, 1
        
        l_balanced, l_height = tree_height(root.left) 
        r_balanced, r_height = tree_height(root.right)

        balanced = l_balanced and r_balanced and abs(l_height - r_height) <= 1
        height = max(l_height, r_height) + 1
        # print(root.val, ": ", balanced, height)
        return balanced, height
    
    balanced, height = tree_height(root)
    return balanced

    
a = TreeNode(3)
b = TreeNode(9)
c = TreeNode(20)
d = TreeNode(15)
e = TreeNode(7)
a.left= b
a.right = c
c.left = d
c.right = e

print (isBalanced(a))
print (isBalanced(b))
print (isBalanced(c))
print (isBalanced(d))
print (isBalanced(e))
