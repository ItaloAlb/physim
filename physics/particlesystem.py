from geometry.geometry import *
from material.material import *
from core.mesh import *
from physics.collisionhandler import *


# Particle System is a physical object that evolves in time.
# It will store information about all particles.
# Also, it will call a collision handler to solve collision problems.
class ParticleSystem:
    def __init__(self):

        # array list with all information about particles
        # particles[i][j]: i = [0, 1, 2] or [mass, position, velocity] ; j = [0, ..., n] each particle
        self.particles = []

        self.collisionHandler = CollisionHandler()

        # setup graphics for bounding box
        self._boundBoxGeo = BoundingBoxGeometry()
        self._boundBoxMat = LineMaterial()
        self._boundBoxMesh = Mesh(self._boundBoxGeo, self._boundBoxMat)

        # setup graphics for particles
        self._particleGeo = PointGeometry()
        self._particleMat = PointMaterial()
        self._particleMesh = Mesh(self._particleGeo, self._particleMat)



    def add_particle(self, particle) -> None:
        self.particles.append(particle)

    def remove_particle(self, particle) -> None:
        self.particles.remove(particle)

    def update(self, dt: float):
        # updating all particles position by calling collision handler
        self.particles[1] = self.collisionHandler(self.particles[1], self.particles[1] + self.particles[2] * dt)