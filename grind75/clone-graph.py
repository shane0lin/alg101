# 133 Copy Graph


class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

def cloneGraph(self, node: 'Node') -> 'Node':
    if not node: return None
    visited = {}
    que = [node]
    visited[node] = Node(node.val, [])
    while que:
        n = que.pop(0)
        for neighbor in n.neighbors:
            if neighbor not in visited:
                visited[neighbor] = Node(neighbor.val, [])
                que.append(neighbor)
            visited[n].neighbors.append(visited[neighbor])
    return visited[node]