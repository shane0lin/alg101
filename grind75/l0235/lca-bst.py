from common.tree import TreeNode


def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    if not root:
        return root
    
    ancestor = root
    while ancestor:
        if p.val < ancestor.val and q.val < ancestor:
            ancestor = ancestor.left
        elif p.val > ancestor.val and q.val > ancestor:
            ancestor = ancestor.right
        else:
            return ancestor
        

