from utils.matrix import Matrix
import numpy as np


class Object3D(object):
    def __init__(self):
        self.transform = Matrix.identity()
        self.parent = None
        self.children = []

    # @property
    # def transform(self):
    #     return self._transform
    #
    # @transform.setter
    # def transform(self, matrix):
    #     if not(isinstance(matrix, np.ndarray)) and matrix.shape == (4, 4):
    #         raise Exception("Message not implemented yet.")
    #     self._transform = matrix

    def add(self, child):
        self.children.append(child)
        child.parent = self

    def remove(self, child):
        self.children.remove(child)
        child.parent = None

    def getWorldMatrix(self):
        if self.parent is None:
            return self.transform
        else:
            return self.parent.getWorldMatrix() @ self.transform

    def getDescendant(self):
        descendant = []

        nodesToProcess = [self]

        while len(nodesToProcess) > 0:
            node = nodesToProcess.pop(0)
            descendant.append(node)
            nodesToProcess = node.children + nodesToProcess

        return descendant

    def applyMatrix(self, matrix, localCoord=True):
        if localCoord:
            self.transform = self.transform @ matrix
        else:
            self.transform = matrix @ self.transform

    def translate(self, x, y, z, localCoord=True):
        matrix = Matrix.translate(x, y, z)
        self.applyMatrix(matrix, localCoord)

    def scale(self, x, y, z, localCoord=True):
        matrix = Matrix.scale(x, y, z)
        self.applyMatrix(matrix, localCoord)

    def rotate(self, x, y, z, localCoord=True):
        matrix = Matrix.rotateX(x) @ Matrix.rotateY(y) @ Matrix.rotateZ(z)
        self.applyMatrix(matrix, localCoord)

    def getLocalPosition(self):
        return np.array([self.transform.item(0, 3),
                         self.transform.item(1, 3),
                         self.transform.item(2, 3)])

    def getWorldPosition(self):
        worldTransform = self.getWorldMatrix()
        return np.array([worldTransform.item(0, 3),
                         worldTransform.item(1, 3),
                         worldTransform.item(2, 3)])

    def setLocalPosition(self, position):
        self.transform.itemset((0, 3), position[0])
        self.transform.itemset((1, 3), position[1])
        self.transform.itemset((2, 3), position[2])
