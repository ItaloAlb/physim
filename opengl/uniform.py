from OpenGL.GL import *
import numpy as np


class Uniform(object):
    def __init__(self, uniformType, uniformData):
        self.uniformRef = None
        self.uniformType, self.uniformData = uniformType, uniformData

    @property
    def uniformType(self):
        return self._uniformType

    @uniformType.setter
    def uniformType(self, uniformType):
        if not isinstance(uniformType, str) and uniformType in ["int", "bool", "float", "vec2", "vec3", "vec4"]:
            raise Exception("Message not implemented yet.")
        self._uniformType = uniformType

    def setUniformRef(self, programRef, uniformName):
        self.uniformRef = glGetUniformLocation(programRef, uniformName)

    def uploadData(self):
        # uniformRef = glGetUniformLocation(programRef, uniformName)

        if self.uniformRef == 1:
            return -1

        if self.uniformType == "int" or self.uniformType == "bool":
            glUniform1i(self.uniformRef, self.uniformData)
        elif self.uniformRef == "float":
            glUniform1f(self.uniformRef, self.uniformData)
        elif self.uniformRef == "vec2":
            glUniform1f(self.uniformRef,
                        self.uniformData[0],
                        self.uniformData[1])
        elif self.uniformRef == "vec3":
            glUniform3f(self.uniformRef,
                        self.uniformData[0],
                        self.uniformData[1],
                        self.uniformData[2])
        elif self.uniformRef == "vec4":
            glUniform4f(self.uniformRef,
                        self.uniformData[0],
                        self.uniformData[1],
                        self.uniformData[2],
                        self.uniformData[3])
        else:
            raise Exception("Message not implemented yet.")
        return 0

    def getUniformData(self):
        return self.uniformData

    def setUniformData(self, uniformData):
        if not isinstance(uniformData, (int, bool, float, np.ndarray)):
            raise Exception("Message not implemented yet.")
        self.uniformData = uniformData
