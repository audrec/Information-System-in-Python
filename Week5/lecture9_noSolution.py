# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 22:51:21 2021

@author: guanglan
"""


# Passing an immutable object to a function
def my_function(param):
    '''Print value and its ID '''
    print(f'x is {param} and its id is {id(param)}')


arg = 5
print(id(arg))
my_function(arg)


# A function can’t modify an immutable object in the calling environment
def my_function1(param):
    """Pay attention to the the parameter's ID"""
    param = 10  # the assignment change the reference to a different object
    print(f'x is {param} and its id is {id(param)}')


arg = 5
print(id(arg))
my_function1(arg)
print(arg, id(arg))


# passing mutable objects to a function
def my_function2(param_list):
    print(f'Parameter list before modification: {param_list}')
    param_list[0] = 10  # modification in place
    print(f'Parameter list after modification: {param_list}')


arg_list = [1, 2, 3]
my_function2(arg_list)
print(arg_list)  # arg_list got modified too


def sort_list1(x_list):
    '''sort a list in place'''
    return x_list.sort()


arg_list = [4, 2, 3]
sort_list1(arg_list)
print(arg_list)  # arg_list got modified too


def sort_list2(x_list):
    '''create a new list containing the sorted values'''
    return sorted(x_list)  # an new object is created


arg_list = [4, 2, 3]
y_list = sort_list2(arg_list)
print(arg_list, y_list)  # arg_list is unchanged


# Passing a mutable object to a function
def my_function3(element, param_list=[]):
    param_list.append(element)
    return param_list


my_function3(1)
my_function3(2)
my_function3(3)


# a parameter listed without assignment is a required parameter
def apply_discount(price, off_rate=0.1):
    return price * (1 - off_rate)


apply_discount(10, 0.2)  # passing by position
apply_discount(off_rate=0.2, price=10)  # passing by keyword
apply_discount(10)  # use default value for off_rate
apply_discount()  # error, price is a required parameter


# argument tuple packing
def cal_mean(*args):
    if len(args) != 0:
        return sum(args) / len(args)


result = cal_mean()
print(result)
cal_mean(1)
cal_mean(1, 2, 3)


# argument dictionary packing
def my_function4(param1, *args, **kwargs):
    print(param1)
    print(args)
    for k, v in kwargs.items():
        print(f"{k} is {v}")


my_function4('0001', "Ward Elementary School", "Class 2",
             Name='John Smith', DOB='01/01/1989')


# Handle exceptions
# print built-in exceptions, functions, and attributes.
print(dir(locals()['__builtins__']))


def multi_div(a, b):
    '''multiply and divide two numbers '''
    x, y = a*b, a/b
    return x, y


print(multi_div)
print(multi_div.__doc__)
help(multi_div)
multi_div(5, 0)  # ZeroDivisionError
multi_div(5, 'apple')  # TypeError


def multi_div1(a, b):
    '''multiply and divide two numbers and check for exception '''
    x, y = None, None

    try:
        x = a*b
        y = a/b
    except ZeroDivisionError:
        print("cannot divide by zero")
    except Exception as e:
        print(f'Python error: {e}')
    else:
        print("Calculations were done correctly!")
    finally:
        print("always run this part")
        return x, y


multi_div1(5, 1)
multi_div1(5, 0)
multi_div1(5, 'apple')


# Exercise: Write a function to calculate arithmetic progression




# Exercise: Write a function ratio_list() to compute the ratio of
# the 2nd element divided by the 1st element in a list, and return the ratio



