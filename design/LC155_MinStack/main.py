class MinStack:

    def __init__(self):
        self.stack = []
        self.min = []

    def push(self, x):
        self.stack.append(x)
        prevMin = self.getMin()

        if prevMin == None:
            self.min.append(x)
        else:
            self.min.append(min(prevMin, x))
    def pop(self):
        self.stack.pop()
        self.min.pop()

    def top(self):
        if len(self.stack) > 0:
            return self.stack[-1]

    def getMin(self):
        if len(self.min) > 0:
            return self.min[-1]
