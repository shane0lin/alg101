from typing import List, Optional

from common.tree import TreeNode

def pathSum(root: Optional[TreeNode], targetSum: int) -> List[List[int]]:  # noqa: F821
    rst = []

    def dfs(root, curSum, targetSum, cur_nodes, results):
  
        if not root:
            return
        curSum += root.val
        cur_nodes.append(root.val)
        
        if not root.left and not root.right and curSum == targetSum:        
            results.append(list(cur_nodes))
    
        
    
        dfs(root.left, curSum, targetSum, cur_nodes, results)
        dfs(root.right, curSum, targetSum, cur_nodes, results)
        
        cur_nodes.pop()
    
    dfs(root, 0, targetSum, [], rst)
    return rst


a = TreeNode(5)
b = TreeNode(4)
c = TreeNode(8)
a.left = b
a.right = c
d = TreeNode(11)
e = TreeNode(7)
f = TreeNode(2)
d.left = e
d.right = f
b.left = d
g = TreeNode(13)
h = TreeNode(4)
c.left = g
c.right = h
o = TreeNode(5)
p = TreeNode(1)
h.left = o
h.right = p

print(pathSum(a, 22))



        

        
        

        
        