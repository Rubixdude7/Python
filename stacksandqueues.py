#stacks and queues
from collections import deque
stack = ["a","b","c"]
queue = deque(["a","b","c"])
print("['a','b','c']")
print("popping stack:", stack.pop())
print("popping queue:", queue.popleft())
