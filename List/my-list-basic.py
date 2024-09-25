# Python List
import pprint
pp = pprint.PrettyPrinter(indent=2)

my_list = ["3", "2", "7", "6", "5", "4"]
my_list.append("8")
my_list.append("9")

my_list.sort()
pp.pprint(my_list)

my_list.remove("7")
my_list.sort()

del my_list[0:2]

my_list.reverse()
my_list.insert(2, "1")
my_list.pop(3)
print(my_list)

print("\n------ Iterate through the list ------")
my_list = ["10", "11", "12", "13", "14", "15"]

for element in my_list:
    print(element)
