from typing import List, Optional
from collections import deque

from common.tree import TreeNode


def levelOrder(root: Optional[TreeNode]) -> List[List[int]]:
    rst =[]
    if not root:
        return rst
    
    que = deque([root])

    while que:
        cur_level = []
        for _ in range(len(que)):
            node = que.popleft()
            cur_level.append(node.val)
            if node.left:
                que.append(node.left)
            if node.right:
                que.append(node.right)
        rst.append(cur_level)
    return rst
            