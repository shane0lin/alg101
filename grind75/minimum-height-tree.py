# 310 . Minimum Height Trees
# 无向图，找最小高度树，即最长路径的中间节点
# 从叶子节点开始删除，直到剩下0或1个节点
def findMinHeightTrees(n, edges):
    if n == 1: 
        return [0] 
    graph = {}
    indgree = [0] * n
    for u, v in edges:
        graph[u] = [v] if u not in graph else graph[u] + [v]
        graph[v] = [u] if v not in graph else graph[v] + [u]
        indgree[u] += 1
        indgree[v] += 1

    leaves = [i for i in range(n) if indgree[i] == 1]
    # print(leaves)
    # print(indgree)
    # for k, v in graph.items():
    #     print(k, v)
    remaining = n
    while remaining > 2:
        remaining -= len(leaves)
        new_leaves = []
        for leaf in leaves:
            for node in graph[leaf]:
                indgree[node] -= 1
                if indgree[node] == 1:
                    new_leaves.append(node)
        leaves = new_leaves
    return leaves
print(findMinHeightTrees(4, [[1,0],[1,2],[1,3]]))
print(findMinHeightTrees(6, [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]))