# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 22:53:57 2021

@author: guanglan
"""
import os


def apply_discount(price: float, off_rate: float = 0.1) -> float:
    return price * (1 - off_rate)


apply_discount(10, 0.2)  # passing by position
apply_discount(10)
apply_discount.__annotations__

# Iterators
x_list = ["apple", "banana", "kiwi"]
x_iter = iter(x_list)
print(next(x_iter))
print(next(x_iter))
print(next(x_iter))
print(next(x_iter))  # StopIteration

iter(50)  # TypeError, int is not iterable
next(x_list)  # TypeError, list is not an iterator

os.getcwd()  # check working directory
os.chdir('C:/Users/guanglan/Dropbox/BUwork/Python/CS521/')
d_file = open('three_lines.txt', "r")
d_file = iter(d_file)
next(d_file)
next(d_file)
next(d_file)
next(d_file)
d_file.close()


def infinite_num():
    num = 0
    while True:
        yield num
        num += 1


num_gen = infinite_num()
next(num_gen)
next(num_gen)
next(num_gen)


def fibo_generator():
    '''Fibonacci number generator'''
    first, second = 0, 1
    while True:
        yield first
        first, second = second, first + second


fibo_gen = fibo_generator()
for counter in range(50):
    print(next(fibo_gen), end=", ")


# lambda
x_list = [1, 2, 3]
y_list = [2, 3, 4]
map_result = map(lambda x, y: x + y, x_list, y_list)
map_result
z_list = list(map_result)
z_list
list(map_result)  # the reuslt, once iterated over, is exhausted

filter_result = filter(lambda x: x.isdigit(), 'Boston Marathon 2021')
filter_result
number_str = "".join(list(filter_result))
number_str
list(filter_result)  # exhausted

from functools import reduce
n = 5
reduce_result = reduce(lambda x, y: x*y, range(1, n+1))
reduce_result


# non-recursive
def factorial(n: int) -> int:
    '''calculate factorial, input an integer larger than or equal to 0'''
    f = 1

    if n == 0 | n == 1:
        return f
    else:
        for m in range(1, n+1):
            f *= m
        return f


factorial(5)


# recursive
def factorial_rec(n: int) -> int:
    '''calculate factorial, input an integer larger than or equal to 0'''
    if n <= 1:
        return 1
    else:
        return n * factorial_rec(n-1)


factorial_rec(5)


# Exercise 1: generate the next arithmetic progression number
def arith_prog_gen(a, b):
    first = a
    while True:
        yield first
        first += b


gen = arith_prog_gen(5, 3)
next(gen)


#  Exercise 2: recursive function for Fibonacci numbers
def fibo_rec(n: int):
    '''Fibonacci number, input an integer larger than or equal to 0'''
    if n == 0:
        return 0
    elif n <= 2:
        return 1
    else:
        return fibo_rec(n - 1) + fibo_rec(n - 2)

fibo_rec(5)

