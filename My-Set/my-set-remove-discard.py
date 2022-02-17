# Python program to demonstrate Deletion of elements in a Set

# Creating a Set
set1 = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
set1.add(10)
set1.add(10)
print(set1)

print("\nRemoving elements from Set using Remove() method")
set1.remove(5)
set1.remove(6)
print(set1)

print("\nRemoving elements from Set using Discard() method")
set1.discard(8)
set1.discard(9)
print(set1)

print("\n" + "-" * 50)
for i in range(100, 105):
    set1.add(i)
print(set1)

for i in range(100, 102):
    set1.remove(i)

print(set1)
