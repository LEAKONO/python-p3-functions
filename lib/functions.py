#!/usr/bin/env python3

def greet_programmer():
    print("Hello, programmer!")

    return "Hello, programmer!"
greet_programmer()


def greet(name):
    print(f"Hello, {name}!")

    return f"Hello, {name}!"
greet("Alice")




def greet_with_default(name="programmer"):
    print(f"Hello, {name}!")

    return f"Hello, {name}!"
greet_with_default("Alice")
greet_with_default()


def add(num1, num2):
    print(num1 + num2)
    return num1 + num2
add(3,4)

def halve(number):
    print(number / 2)
    return number / 2
halve(10)
