from typing import Optional
from collections import deque
from common.tree import TreeNode


def widthOfBinaryTree(root: Optional[TreeNode]) -> int:
    if not root:
        return 0

    rst = 1

    que = deque([(root, 1)])
    while que:
        
        rst = max(rst, que[-1][1] - que[0][1] + 1)
        for _ in range(len(que)):
            node, index = que.popleft()
            if node.left:
                que.append((node.left, index * 2))
            if node.right:
                que.append((node.right, index * 2 + 1))
    return rst