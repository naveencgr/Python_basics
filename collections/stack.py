from collections import deque

stack = deque()
stack.append(1)
stack.append(2)
stack.append(3)
stack.append(4)
stack.append(5)

print(f"stack size {len(stack)}")
element = stack.pop()
print(f"pop element {element}")

stack.appendleft(12)
print(stack)


for s in stack:
    print(s)

