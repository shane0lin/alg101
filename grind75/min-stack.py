# 155 min stack
# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
# push(x) -- Push element x onto stack.
# pop() -- Removes the element on top of the stack.
# top() -- Get the top element.
# getMin() -- Retrieve the minimum element in the stack.
class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min = []
    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack.append(x)
        if not self.min or x <= self.min[-1]:
            self.min.append(x)
    def pop(self):
        """
        :rtype: void
        """
        if self.stack:
            if self.stack[-1] == self.min[-1]:
                self.min.pop()
            self.stack.pop()
    def top(self):
        """
        :rtype: int
        """
        if self.stack:
            return self.stack[-1]
    def getMin(self):
        """
        :rtype: int
        """
        if self.min:
            return self.min[-1]