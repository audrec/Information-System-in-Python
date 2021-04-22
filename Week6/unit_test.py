# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 16:57:08 2021

@author: guanglan
"""
import unittest
import multi_inheritance as multi


class TestVolume(unittest.TestCase):

    def test_cube_in_sphere(self):
        self.assertEqual(multi.CubeInSphere(1).volume(), 1,
                         "CubeInSphere volumn should be 1")

    def test_sphere_in_cube(self):
        self.assertEqual(round(multi.SphereInCube(2).volume(), 2), 4.19,
                         "SphereInCube volumn should be 4.19")


# simply use assert
def test_CubeInSphere():
    assert multi.CubeInSphere(1).volume() == 1, \
           "CubeInSphere volumn should be 1"


def test_SphereInCube():
    assert round(multi.SphereInCube(2).volume(), 2) == 4.19,\
           "SphereInCube volumn should be 4.19"


if __name__ == '__main__':
    unittest.main()
    print("Passed unit tests")

    # Simply use assert
    test_CubeInSphere()
    test_SphereInCube()
    print("Passed unit tests")
