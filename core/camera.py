from core.object3d import Object3D
from utils.matrix import Matrix
from numpy.linalg import inv


class Camera(Object3D):
    def __init__(self, angleOfView=60, aspectRatio=1, near=0.1, far=1000):
        super().__init__()
        self.projectionMatrix = Matrix.perspective(angleOfView=angleOfView,
                                                   aspectRatio=aspectRatio,
                                                   near=near,
                                                   far=far)
        self.viewMatrix = Matrix.identity()

    # @property
    # def viewMatrix(self):
    #     return self._viewMatrix
    #
    # @viewMatrix.setter
    # def viewMatrix(self, matrix):
    #     self._viewMatrix = matrix


    def updateViewMatrix(self):
        self.viewMatrix = inv(self.getWorldMatrix())
