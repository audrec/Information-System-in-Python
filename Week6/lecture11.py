# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 22:42:59 2021

@author: guanglan
"""
import copy


class MyFirstClass():
    pass


class Student():
    """Simple Student class."""
    school = "Brookline High"  # calss attribute

    def __init__(self, first='', last='', id=0):  # constructor
        print("in __init__")
        self.first_name = first  # public attribute
        self.last_name = last
        self.__id = id  # private attribute

    def __str__(self):  # string representation, e.g. for printing
        print("in __str__")
        return f"{self.first_name} {self.last_name}, ID:{self.__id}"

    def __copy__(self):
        return Student(self.first_name, self.last_name, self.__id)

    def update(self, first='', last='', id=0):  # mutator
        if first:
            self.first_name = first
        if last:
            self.last_name = last
        if id:
            self.__id = id


dir(Student)
type(Student)
print(issubclass(Student, object))
print(Student.__doc__)

# An instuance of Student class
student1 = Student(first="John", last="Doe", id=100)
dir(student1)
type(student1)
print(student1)
print(repr(student1))
print(isinstance(student1, Student))
print(isinstance(student1, object))
student1.gender = "M"
student1.quiz1_score = 99.5
student1.last_name = "Smith"
print(Student.gender, Student.quiz1_score)

# access class attributes, both way works
print(Student.school)
print(student1.school)

# retagging & shallow copy
student2 = student1  # retagging, refer to the same object
print(id(student1), id(student2))
student3 = copy.copy(student1)  # shallow copy
print(id(student1), id(student3))
print(student3)

# update an instance
student3.update(first="Alice", last="Smith", id=101)
print(student3)

# public vs. private attributes
print(f"student 1: {student1.first_name} {student1.last_name}")
print(f"student 1 ID: {student1.__id}")  # Does not work
print(f"student 1 ID: {student1._Student__id}")


x_str = 'Boston University'
x_list = ['Boston', 'University']
len(x_str)
x_str.__len__()
x_list[0]
x_list.__getitem__(0)


class StoreOrder:
    def __init__(self, customer, cart):
        self.cart = list(cart)
        self.customer = customer

    def __str__(self):
        return f"{self.customer}'s shopping cart contains {self.cart}"

    def __repr__(self):
        return f'StoreOrder({self.customer}, {self.cart})'

    def __len__(self):  # overloading len()
        '''Get the nubmer of items in the cart'''
        return len(self.cart)

    def __add__(self, other_item):  # overloading +
        '''Allow adding new items to the cart'''
        new_cart = self.cart.copy()
        new_cart.append(other_item)
        return StoreOrder(self.customer, new_cart)

    def __iadd__(self, other_item):
        self.cart.append(other_item)
        return self  # the value of instance changed to what was returned here

    def __getitem__(self, index):
        return self.cart[index]

order1 = StoreOrder('John Smith', ['banana', 'apple'])
print(order1, id(order1))
str(order1)
repr(order1)
len(order1)
order2 = order1 + "kiwi"
print(order2, id(order2))
order1 += "orange"
print(order1, id(order1))
order1[0]


# exercise: define a Circle class
# It take a parameter radius to construct an instance of the class.
# The default radius is 1.
# print(instance of Circle) should print out appropriate message
# Include a method area() that calculates area of a circle
# '+': new circle with r = max(r1, r2)
# ‘-': new circle with r = min(r1, r2)
# '==': True if both radii are the same
# '>': True if r1 > r2


class Circle():
    """Circle class"""

    __pi = 3.14

    def __init__(self, radius=1):
        ''' Create attribute r. Default radius is 1'''
        self.__r = radius

    def __str__(self):
        return f"A circle with radius {self.__r:.2f}."

    def __copy__(self):
        return Circle(self.__r)

    def set_radius(self, r):  # mutator
        self.__r = r  # (setter)

    def get_radius(self):  # accessor
        return self.__r

    def area(self):
        return Circle.__pi*self.__r**2

    def __add__(self, other):
        if self.__r >= other.__r:
            return Circle(self.__r)
        else:
            return Circle(other.__r)

    def __sub__(self, other):
        if self.__r <= other.__r:
            return Circle(self.__r)
        else:
            return Circle(other.__r)

    def __eq__(self, other):
        return (self.__r == other.__r)

    def __gt__(self, other):
        return (self.__r > other.__r)


c1 = Circle(2)
c2 = Circle(5)
c3 = c1 + c2
print(c1 == c2)
print(c1 > c2)
