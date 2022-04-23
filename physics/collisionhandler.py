from typing import Tuple

import numpy
# from physics.particlesystem import ParticleSystem


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

        # create a list with all collision index where pNextPos is out of bound
        colCheck = numpy.where(pNextPos > boundBox / 2, True, False)
        pVel = numpy.where(colCheck, -pVel, pVel)
        colCheck = numpy.where(pNextPos < - boundBox / 2, True, False)
        pVel = numpy.where(colCheck, -pVel, pVel)

        pNextPos = numpy.where(pNextPos > boundBox / 2, 2 * boundBox / 2 - pNextPos, pNextPos)
        pNextPos = numpy.where(pNextPos < - boundBox / 2, 2 * (- boundBox / 2) - pNextPos, pNextPos)


        # check and response: particle-to-particle collision

        return pNextPos, pVel
