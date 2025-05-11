# 84 - Largest Rectangle in Histogram
# https://leetcode.com/problems/largest-rectangle-in-histogram/
def largestRectangleArea(heights):
    stack = []
    max_area = 0
    for i, h in enumerate(heights):
        start = i
        while stack and stack[-1][1] > h:
            index, height = stack.pop()
            max_area = max(max_area, height * (i - index))
            start = index # start is the index of the first element in the stack that is smaller than h
        stack.append((start, h))
        print(start, h)
    for i, h in stack:
        max_area = max(max_area, h * (len(heights) - i))
    return max_area

print(largestRectangleArea([2,1,5,6,2,3]))