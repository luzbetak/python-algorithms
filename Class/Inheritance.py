class Parent:
    def __init__(self, param1):
        print("Parent Class: " + param1)


class Child(Parent):
    def __init__(self, param1, param2):
        super().__init__(param1)
        print("Child Class : " + param2)


lemon = Child("green", "yellow")
