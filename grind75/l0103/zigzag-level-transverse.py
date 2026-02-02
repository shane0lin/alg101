from collections import deque
from typing import List, Optional
from common.tree import TreeNode


def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
    rst = []
    if not root:
        return rst
    
    que = deque([root])
    direction = 1

    while que:
        cur_level = []
        for _ in range(len(que)):
            node = que.popleft()
            cur_level.append(node.val)
            if node.left:
                que.append(node.left)
            if node.right:
                que.append(node.right)
        if direction:
            rst.append(cur_level)
        else:
            rst.append(cur_level[::-1])
        direction = not direction
    return rst
    
        
