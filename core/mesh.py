from core.object3d import Object3D
from OpenGL.GL import *


class Mesh(Object3D):
    def __init__(self, geometry, material):
        super().__init__()

        self.geometry = geometry
        self.material = material

        self.visible = True
