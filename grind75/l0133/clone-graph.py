from typing import Optional
from collections import deque
from common.graph import Node

"""
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
    if not node:
        return node
    visited = {}
    visited[node] = Node(node.val)

    que = deque()
    que.append(node)
    
    while que:
        nd = que.popleft()
        for neighbor in nd.neighbors:
            if neighbor not in visited:
                visited[neighbor] = Node(neighbor.val)
                que.append(neighbor)
            
            visited[nd].neighbors.append(visited[neighbor])
        
    return visited[node]
