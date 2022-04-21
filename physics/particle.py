from geometry.geometry import *
from material.material import *
from core.mesh import *
import numpy


class Particle:
    def __init__(self, mass: float, position: numpy.ndarray, velocity: numpy.ndarray, acceleration: numpy.ndarray):
        # initialize all particles physics properties
        self.mass, self.position, self.velocity, self.acceleration = mass, position, velocity, acceleration

        # setup graphics for particle
        self._geometry = PointGeometry()
        self._material = PointMaterial()
        self.mesh = Mesh(self._geometry, self._material)