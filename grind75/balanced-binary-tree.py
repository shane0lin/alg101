# Given a binary tree, determine if it is height-balanced.

def isBalanced(root):
    # return a, b; a is the height of the tree, b is the balance of the tree
    def height(root):
        if not root:
            return 0, 1
        a, b = height(root.left)
        c, d = height(root.right)
        return 1+max(a, c), b and d and abs(a-c) <= 1
    return height(root)[1]
    if not root:
        return True
    return abs(height(root.left) - height(root.right)) <= 1 and isBalanced(root.left) and isBalanced(root.right)