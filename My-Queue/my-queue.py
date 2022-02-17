# The Python My-Queue functions
from collections import deque

# create a new empty deque object that will function as a My-Queue
queue = deque()

# add some items to the My-Queue
queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)

# print the My-Queue contents
print(queue)

# pop an item off the front of the My-Queue
x = queue.popleft()
print(x)
print(queue)
