# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 16:34:04 2021

@author: guanglan
"""
import math


# an example of multiple inheritance
class Sphere():
    __pi = 3.14

    def __init__(self, radius=1):
        self.r = radius

    def __str__(self):
        return f'ball with radius {self.r}'

    def volume(self):
        return 4 * self.__pi * self.r**3 / 3


class Cube:
    def __init__(self, side=1):
        self.__side = side

    def __str__(self):
        return f'cube with side {self.__side}'

    def volume(self):
        return self.__side**3


class CubeInSphere(Cube, Sphere):
    def __init__(self, side=1):
        radius = side * math.sqrt(3.0)
        Cube.__init__(self, side)
        Sphere.__init__(self, radius)


class SphereInCube(Sphere, Cube):
    def __init__(self, side=1):
        Cube.__init__(self, side)
        Sphere.__init__(self, side)


class A0(object):
    pass


class A1(object):
    pass


class B0(A0):
    pass


class B1(A1):
    pass


class C(B0, B1):
    pass


if __name__ == "__main__":
    blue_cube = Cube(1)
    red_ball = Sphere(1)
    print('blue cube is ', blue_cube)
    print('red ball is ', red_ball)
    print('blue_cube volume : ', blue_cube.volume())
    print('red ball volume : ', red_ball.volume())

    x = CubeInSphere(1)
    print(x.__class__)  # instance-of
    print(CubeInSphere.__bases__)  # is-a
    print(CubeInSphere.mro())  # method resolution order
    y = SphereInCube(1)
    print(y.__class__)  # instance-of
    print(SphereInCube.__bases__)  # is-a
    print(SphereInCube.mro())  # method resolution order
    print('x is ', x, ' volume :', x.volume())  # used Cube.volumn()
    print('y is ', y, ' volume :', y.volume())  # used Sphere.volumn()

    print(C.mro())  # depth-first, left-right
