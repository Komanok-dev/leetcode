from collections import deque


class MyQueue:

    def __init__(self):
        self.stack = deque()

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        return self.stack.popleft() if not self.empty() else None

    def peek(self) -> int:
        return self.stack[0] if not self.empty() else None

    def empty(self) -> bool:
        return len(self.stack) == 0
