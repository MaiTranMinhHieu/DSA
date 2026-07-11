class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int):
        self.stack.append(val)
        current_min = min(val, self.min_stack[-1] if self.min_stack else val)
        self.min_stack.append(current_min)

    def pop(self):
        self.stack.pop()
        self.min_stack.pop()

    def getMin(self) -> int:
        return self.min_stack[-1]

minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
print(minStack.getMin())
minStack.pop()
print(minStack.getMin())