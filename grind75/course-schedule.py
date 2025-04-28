# 207 Course Schedule
import collections
def canFinish(numCourses, prerequisites):
    """
    :type numCourses: int
    :type prerequisites: List[List[int]]
    :rtype: bool
    """
    graph = [[] for _ in range(numCourses)]
    indegree = [0 for _ in range(numCourses)]

    for edge in prerequisites:
        child, parent = edge[0], edge[1]
        graph[parent].append(child)
        indegree[child] += 1
    
    sources = collections.deque([i for i in range(numCourses) if indegree[i] == 0])
    count = 0
    while sources:
        vertex = sources.popleft()
        count += 1
        for child in graph[vertex]:
            indegree[child] -= 1
            if indegree[child] == 0:
                sources.append(child)
    return count == numCourses

print(canFinish(2, [[1,0]]))
print(canFinish(2, [[1,0],[0,1]]))