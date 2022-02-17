from llist import sllist, sllistnode

# creating a singly linked list
lst = sllist(['1', '2', '3'])
print("-" * 80)
print(lst)
print("-" * 80)

# adding and inserting values
lst.append('4')
node = lst.nodeat(2)
lst.insertafter('5', node)

print(lst)
print(lst.first)
print("-" * 80)

# popping a value
lst.pop()
print(lst)
print("-" * 80)

# removing a specific element
node = lst.nodeat(1)
lst.remove(node)
print(lst)
print(lst.first)
print(lst.last)
print(lst.size)
print("-" * 80)
