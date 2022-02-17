class MyClass:
    # Class variable shared by all instances
    kind = 'Canine'

    # instance variable unique to each instance
    def __init__(self, name):
        self.name = name
        self.tricks = []

    def add_trick(self, trick):
        self.tricks.append(trick)


d = MyClass('Fido')
e = MyClass('Buddy')

d.add_trick('roll over')
e.add_trick('play dead')

print(d.kind, d.name, d.tricks)
print(d.kind, e.name, e.tricks)
