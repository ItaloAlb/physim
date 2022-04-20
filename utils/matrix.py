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
    def translate(x=0, y=0, z=0):
        return np.array([[1, 0, 0, 0],
                        [0, 1, 0, 0],
                        [0, 0, 1, 0],
                        [x, y, z, 1]]).astype(float)

    # Obsolete function
    # @staticmethod
    # def rotate(x=0, y=0, z=0):
    #
    #     cx, cy, cz = cos(x * np.pi / 180), cos(y * np.pi / 180), cos(z * np.pi / 180)
    #     sx, sy, sz = sin(x * np.pi / 180), sin(y * np.pi / 180), sin(z * np.pi / 180)
    #     return np.array([[cy*cz,     sz,     -sy,     0],
    #                     [sz,        cx*cz, sx,     0],
    #                     [sy,       -sx,     cx*cy,  0],
    #                     [0,         0,      0,      1]]).astype(float)

    @staticmethod
    def rotateX(x=0):
        c, s = cos(x * np.pi / 180), sin(x * np.pi / 180)
        return np.array([[1, 0, 0, 0],
                        [0, c, s, 0],
                        [0, -s, c, 0],
                        [0, 0, 0, 1]]).astype(float)

    @staticmethod
    def rotateY(y=0):
        c, s = cos(y * np.pi / 180), sin(y * np.pi / 180)
        return np.array([[c, 0, -s, 0],
                        [0, 1, 0, 0],
                        [s, 0, c, 0],
                        [0, 0, 0, 1]]).astype(float)

    @staticmethod
    def rotateZ(z=0):
        c, s = cos(z * np.pi / 180), sin(z * np.pi / 180)
        return np.array([[c, s, 0, 0],
                        [-s, c, 0, 0],
                        [0, 0, 1, 0],
                        [0, 0, 0, 1]]).astype(float)

    @staticmethod
    def scale(x=1.0, y=1.0, z=1.0):
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
                        [0, 0, b, -1],
                        [0, 0, c, 0]]).astype(float)
