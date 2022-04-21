from geometry.geometry import *
from material.material import *
from core.mesh import *

class ParticleSystem:
    def __init__(self):
        self.particles = []

        # setup graphics for bounding box
        self._geometry = BoundingBoxGeometry()
        self._material = LineMaterial()
        self._mesh = Mesh(self._geometry, self._material)

    def add_particle(self, particle) -> None:
        self.particles.append(particle)

    def remove_particle(self, particle) -> None:
        self.particles.remove(particle)