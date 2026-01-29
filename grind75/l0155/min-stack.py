class MinStack:

    def __init__(self):
        self.data = []
        self.min_stack = []
        

    def push(self, val: int) -> None:
        self.data.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)
        

    def pop(self) -> None:
        value = self.data.pop()
        if value == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self) -> int:
        if not self.data:
            return
        return self.data[-1]
        
    def getMin(self) -> int:
        if not self.min_stack:
            return
        return self.min_stack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()