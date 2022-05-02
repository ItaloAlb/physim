import time
from typing import Tuple

import numpy


# Collision Handler is a graphical concept to solve collision problems.
from numpy import ndarray


class CollisionHandler:
    def __init__(self):
        pass

    def __call__(self, **kwargs):
        pPos = kwargs.get("pPos")
        pNextPos = kwargs.get("pNextPos")
        pVel = kwargs.get("pVel")
        boundBox = kwargs.get("boundBox", 1)

        # check and response: particle-to-bounding collision

        _x = pNextPos[0:len(pNextPos):3]
        _y = pNextPos[1:len(pNextPos):3]
        _z = pNextPos[2:len(pNextPos):3]

        # print("pos: ", pNextPos[:6], "x: ", _x[:2], "y: ", _y[:2], "_z: ", _z[:2])

        _temp1, _temp2 = numpy.greater(pNextPos, boundBox / 2), numpy.less(pNextPos, - boundBox / 2)
        _temp3 = numpy.not_equal(_temp1, _temp2)

        # _temp1, _temp2 = pNextPos > boundBox / 2, pNextPos < - boundBox / 2
        # _temp3 = _temp1 != _temp2

        # print("python: ", tpythonictime > 0.0, "; numpy: ", tnumpytime > 0.0)

        pVel = numpy.where(_temp3, -pVel, pVel)
        pNextPos = numpy.where(_temp3, (-1) ** _temp2 * boundBox - pNextPos, pNextPos)

        # check and response: particle-to-particle collision

        return pNextPos, pVel
