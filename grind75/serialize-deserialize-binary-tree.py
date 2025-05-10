# 297. Serialize and Deserialize Binary Tree    
# Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.
# Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.
# Clarification: The input/output format is a binary tree serialized using level order traversal, where null signifies a path terminator where no node exists below.
# It is not necessarily a full binary tree, as illustrated below:
# Example 1:
# Input: root = [1,2,3,null,null,4,5]
# Output: [1,2,3,null,null,4,5]
# Example 2:
# Input: root = []
# Output: []
# Example 3:
# Input: root = [1]
# Output: [1]
# Example 4:
# Input: root = [1,2]
# Output: [1,2]
# Constraints:
# The number of nodes in the tree is in the range [0, 104].
# -1000 <= Node.val <= 1000
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def serialize(root):
    """Encodes a tree to a single string.
    
    :type root: TreeNode
    :rtype: str
    """
    if not root:
        return ""
    queue = [root]
    res = []
    while queue:
        node = queue.pop(0)
        if node:
            res.append(str(node.val))
            queue.append(node.left)
            queue.append(node.right)
        else:
            res.append("null")
    return ",".join(res)

def deserialize(data):
    """Decodes your encoded data to tree.
    
    :type data: str
    :rtype: TreeNode
    """
    if not data:
        return None
    nodes = data.split(",")
    root = TreeNode(int(nodes[0]))
    queue = [root]
    i = 1
    while queue:
        node = queue.pop(0)
        if nodes[i] != "null":
            node.left = TreeNode(int(nodes[i]))
            queue.append(node.left)
        i += 1
        if nodes[i] != "null":
            node.right = TreeNode(int(nodes[i]))
            queue.append(node.right)
        i += 1
    return root

def print_tree(root):
    if not root:
        return
    print(root.val)
    print_tree(root.left)
    print_tree(root.right)
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.left = TreeNode(4)
root.right.right = TreeNode(5)
# print_tree(root)
print(serialize(root))
# print_tree(deserialize(serialize(root)))
# print(serialize(deserialize(serialize(root))))