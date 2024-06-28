import collections

queue = collections.deque()

queue.append(3)
queue.appendleft(2)
queue.append(4)
queue.appendleft(1)
queue.append(5)
print(queue)

print(queue.pop())
print(queue.popleft())
print(queue)



