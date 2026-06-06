class MinStack:

    def __init__(self):
        self.stack = []
        self.minElement = []


    def push(self, val: int) -> None:
        if len(self.minElement) == 0:
            self.minElement.append(val)
        else:
            self.minElement.append(min(self.minElement[-1], val))
        self.stack.append(val)


    def pop(self) -> None:
        self.stack.pop()
        self.minElement.pop()


    def top(self) -> int:
        return self.stack[-1]


    def getMin(self) -> int:
        return self.minElement[-1]