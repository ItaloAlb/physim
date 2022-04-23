from geometry.geometry import *
from material.material import *
from core.mesh import *
import numpy


# Particle is a conceptual physical object used to simplify and to model natural phenomenon, like celestial.
# A particle is used to describe very small objects. Very small is determined based upon your model.
# Also, a particle have physical properties such as mass, position, velocity and so on and so forth.
# This class will store all information about a single particle themselves.

### OBSOLETE ###
class Particle:
    def __init__(self, mass: float, position: numpy.ndarray, velocity: numpy.ndarray):
        # initialize all particles physics properties
        self.mass, self.position, self.velocity = mass, position, velocity

        # setup graphics for particle
        self._geometry = PointGeometry()
        self._material = PointMaterial()
        self.mesh = Mesh(self._geometry, self._material)