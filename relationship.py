#---------------------------------------------------------------------------#
from collections import defaultdict
import pprint as pp
#---------------------------------------------------------------------------#
relationship = [
    {
        'id': 1,
        'relationship': "spouse",
        'related': 2,
    },
    {
        'id': 2,
        'relationship': "spouse",
        'related': 1,
    },
    {
        'id': 3,
        'relationship': "child",
        'related': 1,
    },
    {
        'id': 3,
        'relationship': "child",
        'related': 2,
    },
    {
        'id': 4,
        'relationship': "child",
        'related': 1,
    },
]
#---------------------------------------------------------------------------#
pp.pprint(relationship)
print("-" * 80)

#---------------------------------------------------------------------------#
child_dict = defaultdict(list)
for item in relationship:
    if item.get("relationship") == "child":
        child_dict[item["id"]].append(item["related"])

pp.pprint(child_dict)
print("-" * 80)
#---------------------------------------------------------------------------#
parent_dict = {}
for child, parent in child_dict.items():
    print("child_" + str(child) + " -> parent_" + str(parent))

    for i in parent:
        parent_dict[i] = parent_dict.get(i, 0) + 1

print("-" * 80)
pp.pprint(parent_dict)
for key, value in parent_dict.items():
    # print("Parent: {} -> Children {}".format(key, value))
    print(key, ":", ', '.join(value))


#---------------------------------------------------------------------------#
# Scala Implementation
#---------------------------------------------------------------------------#
# case class Relationship(id: Int, relation: String, to: Int)
# val relations = Seq(
# Relationship(1, "spouse", 2),
# Relationship(2, "spouse", 1),
# Relationship(3, "child", 1),
# Relationship(3, "child", 2),
# Relationship(4, "child", 1)
# )
#---------------------------------------------------------------------------#
# val childCounts = relations
# .filter(_.relation == "child")
# .map( e => (e.to, e.id))
# .groupBy(_._1)
# .mapValues(_.size)
#---------------------------------------------------------------------------#
# Scala / Python / PySpark



