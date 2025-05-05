# 105 Construct Binary Tree from Preorder and Inorder Traversal
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right  
    
    def __repr__(self):
        return str(self.val)


def buildTree(preorder: List[int], inorder: List[int]) -> TreeNode:
    if not preorder or not inorder:
        return None
    root = TreeNode(preorder[0])
    mid = inorder.index(preorder[0])
    root.left = buildTree(preorder[1:mid+1], inorder[:mid])
    root.right = buildTree(preorder[mid+1:], inorder[mid+1:])
    return root

print(buildTree([3,9,20,15,7], [9,3,15,20,7]))