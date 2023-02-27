#!/usr/bin/env python

def my_decorator(func):
    def wrapper():
        print("Before the (say_hello) function is called.")
        func()
        print("After the (say_hello) unction is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello from decorator")


print("Python Decorator Test")
say_hello()



