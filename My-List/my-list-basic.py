# Python List
import pprint
pp = pprint.PrettyPrinter(indent=2)

my_list = ["3", "2", "1", "6", "5", "4"]

my_list.sort()
pp.pprint(my_list)

my_list.append("7");
my_list.remove("1");
del my_list[0:2]

my_list.reverse()
my_list.insert(2, "8")
my_list.pop(3)
pp.pprint(my_list)

print("\n------ Iterate through the list ------")
my_list = ["10", "11", "12", "13", "14", "15"]
for element in my_list:
    pp.pprint(element)
