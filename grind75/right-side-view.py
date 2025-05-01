# 199. Binary Tree Right Side View
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def rightSideView(self, root: TreeNode) -> List[int]:
    if not root:
        return []
    res = []
    queue = [root]
    while queue:
        res.append(queue[-1].val)
        for i in range(len(queue)):
            node = queue.pop(0)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    return res