from typing import Optional
from common.tree import TreeNode


def kthSmallest(root: Optional[TreeNode], k: int) -> int:
    stack = []
    curr = root

    while stack or curr:
        while curr:
            stack.append(curr)
            curr = curr.left

        curr = stack.pop()
        k -= 1
        if k == 0:
            return curr.val

        curr = curr.right
