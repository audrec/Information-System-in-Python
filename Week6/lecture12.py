s# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 22:42:59 2021

@author: guanglan
"""


class Person():
    """Simple Person class."""
    school = "Brookline High"

    def __init__(self, first='', last='', id=0):
        self.first_name = first
        self.last_name = last
        self.id = id

    def __str__(self):
        return f"{self.first_name} {self.last_name}, ID:{self.id}"

    def isStudent(self):
        return False

    def isEmployee(self):
        return False


# child class of class Person
class Student(Person):
    """Simple Student class."""

    def __init__(self, first='', last='', id=0, gpa=4.0):
        self.gpa = gpa
        # Make sure to call the parent class's __init__
        Person.__init__(self, first, last, id)
        # super().__init__(first, last, id)

    def __str__(self):
        # result_str = f"Student: {super().__str__()} gap:{self.gpa}"
        result_str = f"Student: {Person.__str__(self)} gap:{self.gpa}"
        return result_str

    def isStudent(self):  # Polymorphic method
        return True


if __name__ == "__main__":
    # created instuances of Person class
    p1 = Person(first="John", last="Doe", id=100)
    p2 = Person(first="Alice", last="Smith", id=101)

    # access and modify the class attribute
    print(Person.school, p1.school, p2.school)
    Person.school = "Brighton High"  # modify the class attribute
    print(Person.school, p1.school, p2.school)
    p1.school = "Newton High"  # create an instance attribute
    # the instance namespace takes supremacy over the class namespace
    print(Person.school, p1.school, p2.school)

    print(issubclass(Student, Person))
    student1 = Student(first="Emma", last="Boss", id=200, gpa=3.7)
    print(student1)
    print(student1.isStudent(), student1.isEmployee())
    print(student1.__class__)  # instance-of
    print(Student.__bases__)  # is-a
    print(Student.__mro__)  # method resolution order










