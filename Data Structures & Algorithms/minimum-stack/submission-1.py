class MinStack:

    def __init__(self):
        self.storage = []
        self.min_stack = []
        

    def push(self, val: int) -> None:
        self.storage.append(val)
        if self.min_stack:
            self.min_stack.append(min(val, self.min_stack[-1]))
        else:
            self.min_stack.append(val)

    def pop(self) -> None:
        self.min_stack.pop()
        self.storage.pop()

    def top(self) -> int:
        if self.storage:
            return self.storage[-1]
        return float('inf')

    def getMin(self) -> int:
        return self.min_stack[-1]
        
