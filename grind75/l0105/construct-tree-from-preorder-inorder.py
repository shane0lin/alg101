from typing import List, Optional

from common.tree import TreeNode


def buildTree(preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
    if not preorder or not inorder:
        return
    
    root = TreeNode(preorder[0])

    pos = inorder.index(preorder[0])
    root.left = buildTree(preorder[1:1+pos], inorder[:pos])
    root.right = buildTree(preorder[1+pos:], inorder[1+pos:])
    return root

