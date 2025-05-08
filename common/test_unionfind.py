import unittest
from unionfind import UnionFind

# AI writen unitests

class TestUnionFind(unittest.TestCase):
    def test_initialization(self):
        """Test that UnionFind initializes correctly with n elements."""
        n = 10
        uf = UnionFind(n)
        self.assertEqual(len(uf.parents), n)
        for i in range(n):
            self.assertEqual(uf.parents[i], i)
            self.assertEqual(uf.find(i), i)
    
    def test_simple_union(self):
        """Test simple union operations."""
        uf = UnionFind(5)
        uf.union(0, 1)
        self.assertEqual(uf.find(0), uf.find(1))
        self.assertNotEqual(uf.find(0), uf.find(2))
        
        uf.union(2, 3)
        self.assertEqual(uf.find(2), uf.find(3))
        self.assertNotEqual(uf.find(0), uf.find(2))
        
        uf.union(0, 2)
        self.assertEqual(uf.find(0), uf.find(2))
        self.assertEqual(uf.find(1), uf.find(3))
    
    def test_transitive_union(self):
        """Test that union operations are transitive."""
        uf = UnionFind(5)
        uf.union(0, 1)
        uf.union(1, 2)
        self.assertEqual(uf.find(0), uf.find(2))
        
        uf.union(3, 4)
        uf.union(2, 3)
        # Now all elements should be in the same set
        for i in range(4):
            self.assertEqual(uf.find(i), uf.find(i+1))
    
    def test_path_compression(self):
        """Test that path compression works."""
        uf = UnionFind(5)
        # Create a chain: 0 -> 1 -> 2 -> 3 -> 4
        uf.parents = [1, 2, 3, 4, 4]
        
        # Find should compress the path
        self.assertEqual(uf.find(0), 4)
        
        # After path compression, 0 should point directly to 4
        self.assertEqual(uf.parents[0], 4)
    
    def test_large_union(self):
        """Test with a larger number of elements."""
        n = 1000
        uf = UnionFind(n)
        
        # Create two large sets
        for i in range(0, n//2, 2):
            uf.union(i, i+1)
        
        for i in range(0, n//2, 2):
            self.assertEqual(uf.find(i), uf.find(i+1))
            if i+2 < n//2:
                self.assertNotEqual(uf.find(i), uf.find(i+2))
        
        # Merge all sets into one
        for i in range(n-1):
            uf.union(i, i+1)
        
        # All elements should be in the same set now
        root = uf.find(0)
        for i in range(1, n):
            self.assertEqual(uf.find(i), root)
    
    def test_find_idempotence(self):
        """Test that multiple calls to find() return the same result."""
        uf = UnionFind(10)
        uf.union(0, 1)
        uf.union(1, 2)
        uf.union(3, 4)
        uf.union(4, 5)
        uf.union(2, 5)
        
        for i in range(10):
            first_find = uf.find(i)
            second_find = uf.find(i)
            self.assertEqual(first_find, second_find)
    
    def test_disjoint_sets(self):
        """Test maintaining disjoint sets."""
        uf = UnionFind(10)
        
        # Create two disjoint sets: [0,1,2,3,4] and [5,6,7,8,9]
        for i in range(4):
            uf.union(i, i+1)
        
        for i in range(5, 9):
            uf.union(i, i+1)
        
        # Verify the sets are disjoint
        for i in range(5):
            for j in range(5, 10):
                self.assertNotEqual(uf.find(i), uf.find(j))
        
        # Merge the sets
        uf.union(4, 5)
        
        # Now all elements should be in the same set
        for i in range(9):
            self.assertEqual(uf.find(i), uf.find(i+1))
    
    def test_union_with_self(self):
        """Test union of an element with itself."""
        uf = UnionFind(5)
        original_parent = uf.find(3)
        uf.union(3, 3)
        self.assertEqual(uf.find(3), original_parent)

if __name__ == "__main__":
    unittest.main()