import numpy as np
from math import cos, sin, tan, pi


class Matrix(object):
    @staticmethod
    def identity():
        return np.array([[1, 0, 0, 0],
                        [0, 1, 0, 0],
                        [0, 0, 1, 0],
                        [0, 0, 0, 1]]).astype(float)

    @staticmethod
    def translate(x, y, z):
        return np.array([[1, 0, 0, x],
                        [0, 1, 0, y],
                        [0, 0, 1, z],
                        [0, 0, 0, 1]]).astype(float)

    @staticmethod
    def rotate(x=0, y=0, z=0):
        cx, cy, cz = cos(x), cos(y), cos(z)
        sx, sy, sz = sin(x), sin(y), sin(z)
        return np.array([[cy*cz,     sz,     sy,     0],
                        [sz,        cx*cz, -sx,     0],
                        [-sy,       sx,     cx*cy,  0],
                        [0,         0,      0,      1]]).astype(float)

    @staticmethod
    def scale(x, y, z):
        return np.array([[x, 0, 0, 0],
                        [0, y, 0, 0],
                        [0, 0, z, 0],
                        [0, 0, 0, 1]]).astype(float)

    @staticmethod
    def orthographic():
        pass

    @staticmethod
    def perspective(angleOfView=60, aspectRatio=1, near=0.1, far=1000):
        a = angleOfView * pi / 180.0
        d = 1.0 / tan(a/2)
        r = aspectRatio
        b = (far + near) / (near - far)
        c = 2 * far * near / (near - far)
        return np.array([[d/r, 0, 0, 0],
                        [0, d, 0, 0],
                        [0, 0, b, c],
                        [0, 0, -1, 0]]).astype(float)
