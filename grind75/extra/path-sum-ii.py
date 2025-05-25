#113 Path Sum II

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
def pathSum(self, root, sum):
    res = []
    self.dfs(root, sum, [], res)
    return res
def dfs(self, root, sum, path, res):
    if not root:
        return
    path.append(root.val)
    if not root.left and not root.right and sum == root.val:
        res.append(path[:])
    self.dfs(root.left, sum-root.val, path, res)
    self.dfs(root.right, sum-root.val, path, res)
    path.pop()
