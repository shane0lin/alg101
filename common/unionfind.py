class UnionFind:
    def __init__(self, n):
        self.parents = [i for i in range(n)]
        
    def find(self, x):
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]
    
    def union(self, x, y):
        self.parents[self.find(x)] = self.find(y)


# uf = UnionFind(5)
# uf.union(3, 4)
# for i in range(5):
#     print(uf.find(i))