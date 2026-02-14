from common.tree import TreeNode


def goodNodes(root: TreeNode) -> int:
    good_nodes = 0
    
    def dfs(root, max_val):
        nonlocal good_nodes

        if not root:
            return

        if root.val >= max_val:
            good_nodes += 1
            max_val = root.val

        dfs(root.left, max_val)
        dfs(root.right, max_val)

    dfs(root, root.val)
    return good_nodes
        
