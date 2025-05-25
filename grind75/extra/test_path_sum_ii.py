import unittest
from path_sum_ii import TreeNode

class Solution:
    def pathSum(self, root, target_sum):
        res = []
        self.dfs(root, target_sum, [], res)
        return res
    
    def dfs(self, root, target_sum, path, res):
        if not root:
            return
        path.append(root.val)
        if not root.left and not root.right and target_sum == root.val:
            res.append(path[:])
        self.dfs(root.left, target_sum-root.val, path, res)
        self.dfs(root.right, target_sum-root.val, path, res)
        path.pop()

class TestPathSumII(unittest.TestCase):
    def test_example_1(self):
        # Create tree: [5,4,8,11,null,13,4,7,2,null,null,5,1]
        #        5
        #       / \
        #      4   8
        #     /   / \
        #    11  13  4
        #   /  \    / \
        #  7    2  5   1
        root = TreeNode(5)
        root.left = TreeNode(4)
        root.right = TreeNode(8)
        root.left.left = TreeNode(11)
        root.left.left.left = TreeNode(7)
        root.left.left.right = TreeNode(2)
        root.right.left = TreeNode(13)
        root.right.right = TreeNode(4)
        root.right.right.left = TreeNode(5)
        root.right.right.right = TreeNode(1)
        
        solution = Solution()
        result = solution.pathSum(root, 22)
        expected = [[5, 4, 11, 2], [5, 8, 4, 5]]
        self.assertEqual(result, expected)
    
    def test_example_2(self):
        # Create tree: [1,2,3]
        #     1
        #    / \
        #   2   3
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        
        solution = Solution()
        result = solution.pathSum(root, 3)
        expected = [[1, 2]]
        self.assertEqual(result, expected)
    
    def test_example_3(self):
        # Create tree: [1,2]
        #     1
        #    /
        #   2
        root = TreeNode(1)
        root.left = TreeNode(2)
        
        solution = Solution()
        result = solution.pathSum(root, 3)
        expected = [[1, 2]]
        self.assertEqual(result, expected)
    
    def test_empty_tree(self):
        solution = Solution()
        result = solution.pathSum(None, 0)
        expected = []
        self.assertEqual(result, expected)
    
    def test_single_node_matching(self):
        root = TreeNode(1)
        solution = Solution()
        result = solution.pathSum(root, 1)
        expected = [[1]]
        self.assertEqual(result, expected)
    
    def test_single_node_not_matching(self):
        root = TreeNode(1)
        solution = Solution()
        result = solution.pathSum(root, 2)
        expected = []
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()