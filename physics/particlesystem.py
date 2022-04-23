import numpy

from geometry.geometry import *
from material.material import *
from core.mesh import *
from physics.collisionhandler import *


# Particle System is a physical object that evolves in time.
# It will store information about all particles.
# Also, it will call a collision handler to solve collision problems.
class ParticleSystem:
    def __init__(self):

        # numpy array with all information about particles
        # each value is assigned to one particle
        self.pMass = numpy.asarray([1])
        # every three values is assigned to one particle.
        # ex: pPos[0], pPos[1], pPos[2] -> first particle position
        # ex: pPos[3], pPos[4], pPos[5] -> second particle position
        self.pPos = numpy.asarray([0, 0, -5])
        # same as particle position array.
        # every three value is assigned to one particle.
        self.pVel = numpy.asarray([0, 0, 0])

        # instance of Collision Handler class
        self.collisionHandler = CollisionHandler()

        # setup graphics for bounding box
        self._boundBoxGeo = BoundingBoxGeometry()
        self._boundBoxMat = LineMaterial()
        self.boundBoxMesh = Mesh(self._boundBoxGeo, self._boundBoxMat)

        # setup graphics for particles
        self._particleGeo = ParticleSystemGeometry(self.pPos)
        self._particleMat = PointMaterial()
        self.particleMesh = Mesh(self._particleGeo, self._particleMat)

    def add_particle(self, mass, position, velocity) -> None:
        numpy.append(self.pMass, mass)
        numpy.append(self.pPos, position)
        numpy.append(self.pVel, velocity)

    def remove_particle(self, i: int) -> None:
        numpy.delete(self.pMass, i)
        numpy.delete(self.pPos, i)
        numpy.delete(self.pVel, i)

    def update(self, dt: float = 1 / 60):
        # updating all particles position by calling collision handler
        # self.pPos = self.pPos + self.pVel * dt
        self.pPos, self.pVel = self.collisionHandler(pPos = self.pPos, pNextPos = self.pPos + self.pVel * dt, pVel = self.pVel)

        attrib = self._particleGeo.attrib["vertexPosition"]
        attrib.attribData = self.pPos
        attrib.uploadData()

    def __call__(self):
        self.update()