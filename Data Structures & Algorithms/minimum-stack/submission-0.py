class MinStack:

    def __init__(self):
        self.min_val = float('inf')
        self.storage = []
        

    def push(self, val: int) -> None:
        self.storage.append(val)
        self.min_val = min(self.min_val, val)

    def pop(self) -> None:
        if self.storage:
            val = self.storage.pop()
            if val == self.min_val:
                self.min_val = float('inf')
                for num in self.storage:
                    self.min_val = min(self.min_val, num)

    def top(self) -> int:
        if self.storage:
            return self.storage[-1]
        return float('inf')

    def getMin(self) -> int:
        return self.min_val
        
