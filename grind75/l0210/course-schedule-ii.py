from typing import List
from collections import deque


def findOrder(numCourses: int, prerequisites: List[List[int]]) -> List[int]:
    graph = {i:[] for i in range(numCourses)}

    indegree = [0] * numCourses

    for child, parent in prerequisites:
        graph[parent].append(child)
        indegree[child] += 1

    src = deque([])
    for i in range(numCourses):
        if indegree[i] == 0:
            src.append(i)
    
    rst = []
    while src:
        course = src.popleft()
        rst.append(course)
        for child in graph[course]:
            indegree[child] -= 1
            if indegree[child] == 0:
                src.append(child)
    
    return [] if len(rst) != numCourses else rst

