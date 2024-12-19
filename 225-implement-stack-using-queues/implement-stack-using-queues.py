class MyStack:

    def __init__(self):
        self.Stack = deque()

    def push(self, x: int) -> None:
        self.Stack.append(x)

    def pop(self) -> int:
        if len(self.Stack)==0:
            return -1
        else:
            return self.Stack.pop()
        
    def top(self) -> int:
        if len(self.Stack)==0:
            return -1
        return self.Stack[-1]

    def empty(self) -> bool:
        if len(self.Stack)==0:
            return True
        return False


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()