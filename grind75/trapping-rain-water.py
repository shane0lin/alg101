# 42 - Trapping Rain Water

def trap(height):
    if not height:
        return 0
    l, r = 0, len(height) - 1
    leftMax, rightMax = height[l], height[r]
    res = 0
    while l < r:
        if leftMax < rightMax:
            l += 1
            leftMax = max(leftMax, height[l])
            res += leftMax - height[l]
        else:
            r -= 1
            rightMax = max(rightMax, height[r])
            res += rightMax - height[r]
    return res

def trap2(height):
    if not height:
        return 0
    stack = []
    res = 0
    for i in range(len(height)):
        while stack and height[i] > height[stack[-1]]:
            top = stack.pop()
            if not stack: # top is the lowest bar, boundary, no water
                break
            dist = i - stack[-1] - 1
            h = min(height[i], height[stack[-1]]) - height[top] # minimum height of the left and right boundary, minus current height
            res += dist * h
        stack.append(i)
    return res

# print(trap([0,1,0,2,1,0,1,3,2,1,2,1]))
# print(trap([4,2,0,3,2,5]))

# print(trap2([0,1,0,2,1,0,1,3,2,1,2,1]))
# print(trap2([4,2,0,3,2,5]))

import unittest


class TestTrappingRainWater(unittest.TestCase):
    
    def test_example_1(self):
        """Test with the first example: [0,1,0,2,1,0,1,3,2,1,2,1]"""
        height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
        self.assertEqual(trap2(height), 6)
    
    def test_example_2(self):
        """Test with the second example: [4,2,0,3,2,5]"""
        height = [4, 2, 0, 3, 2, 5]
        self.assertEqual(trap2(height), 9)
    
    def test_empty_array(self):
        """Test with an empty array."""
        height = []
        self.assertEqual(trap2(height), 0)
    
    def test_single_element(self):
        """Test with a single element."""
        height = [5]
        self.assertEqual(trap2(height), 0)
    
    def test_two_elements(self):
        """Test with two elements."""
        height = [5, 3]
        self.assertEqual(trap2(height), 0)
    
    def test_no_trap(self):
        """Test with heights that don't trap any water."""
        height = [1, 2, 3, 4, 5]
        self.assertEqual(trap2(height), 0)
        
        height = [5, 4, 3, 2, 1]
        self.assertEqual(trap2(height), 0)
    
    def test_flat_middle(self):
        """Test with a flat middle section."""
        height = [3, 0, 0, 0, 3]
        self.assertEqual(trap2(height), 9)
    
    def test_pyramid(self):
        """Test with a pyramid shape (no water trapped)."""
        height = [1, 2, 3, 4, 5, 4, 3, 2, 1]
        self.assertEqual(trap2(height), 0)
    
    def test_inverse_pyramid(self):
        """Test with an inverse pyramid shape."""
        height = [5, 4, 3, 2, 1, 2, 3, 4, 5]
        self.assertEqual(trap2(height), 16)
    
    def test_irregular_heights(self):
        """Test with irregular heights."""
        height = [5, 2, 1, 2, 1, 5]
        self.assertEqual(trap2(height), 14)
        
        height = [6, 4, 2, 0, 3, 2, 0, 3, 1, 4, 5, 3, 2, 7, 5, 3, 0, 1, 2, 1, 3, 4, 6, 8, 1, 3]
        self.assertEqual(trap2(height), 83)
    
    def test_all_zeros(self):
        """Test with all zeros."""
        height = [0, 0, 0, 0, 0]
        self.assertEqual(trap2(height), 0)
    
    def test_alternating_heights(self):
        """Test with alternating heights."""
        height = [1, 0, 1, 0, 1]
        self.assertEqual(trap2(height), 2)
        
        height = [5, 1, 5, 1, 5]
        self.assertEqual(trap2(height), 8)
    
    def test_large_numbers(self):
        """Test with large numbers."""
        height = [10000, 0, 10000]
        self.assertEqual(trap2(height), 10000)
    
    def test_edge_case_descending(self):
        """Test with strictly descending heights."""
        height = [9, 8, 7, 6, 5, 4, 3, 2, 1]
        self.assertEqual(trap2(height), 0)
    
    def test_edge_case_ascending(self):
        """Test with strictly ascending heights."""
        height = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertEqual(trap2(height), 0)
    
    def test_complex_case(self):
        """Test with a more complex case."""
        height = [5, 3, 7, 2, 6, 4, 5, 9, 1, 2]
        self.assertEqual(trap2(height), 14)
    
    def test_increase_height(self):
        """Test with a more complex case."""
        height = [5, 2, 3, 7]
        self.assertEqual(trap2(height), 5)

if __name__ == "__main__":
    unittest.main()