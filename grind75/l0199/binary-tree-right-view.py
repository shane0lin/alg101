from collections import deque
from typing import List, Optional

from common.tree import TreeNode


def rightSideView(root: Optional[TreeNode]) -> List[int]:
    rst = []
    if not root:
        return rst
    que = deque([root])

    while que:
        rst.append(que[-1].val)
        for _ in range(len(que)):
            node = que.popleft()
            if node.left:
                que.append(node.left)
            if node.right:
                que.append(node.right)
    return rst
