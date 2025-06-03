# Graph Valid Tree
# Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), write a function to check whether these edges make up a valid tree.
# For example:
# Given n = 5 and edges = [[0, 1], [0, 2], [0, 3], [1, 4]], return true.
# Given n = 5 and edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]], return false.
# Note: you can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.

class ValidTree(object):
    def __init__(self):
        self.father = {}
        self.count = 0

    def union(self, a, b):
        a = self.find(a)
        b = self.find(b)
        if a == b:
            return
        self.father[a] = b
        # self.count -= 1

    def find(self, a):
        path = []
        while self.father[a] != a:
            path.append(a)
            a = self.father[a]
        
        for child in path:
            self.father[child] = a

        return a

    def validTree(self, n, edges):
        for i in range(n):
            self.father[i] = i

        self.count = n
        for edge in edges:
            a, b = edge[0], edge[1]
            if self.find(a) == self.find(b):
                return False
            self.union(a, b)
            self.count -= 1

        # if there is only one connected component, then it is a valid tree
        print(self.count)
        if self.count != 1:
            return False

        return True

vt = ValidTree()

print(vt.validTree(5, [[0, 1], [0, 2], [0, 3], [1, 4]])) # True
print(vt.validTree(5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]])) # False