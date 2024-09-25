# importing module
import collections

# initialising a deque() of arbitrary length
linked_list = collections.deque()

# filling deque() with elements
linked_list.append('1')
linked_list.append('2')
linked_list.append('3')

print(linked_list)

# adding element at an arbitrary position
linked_list.insert(1, '4')
print(linked_list)

# deleting the last element
linked_list.pop()
print(linked_list)

# removing a specific element
linked_list.remove('4')
print(linked_list)