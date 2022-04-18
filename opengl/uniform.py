from OpenGL.GL import *
import numpy as np


class Uniform(object):
    def __init__(self, uniformType, uniformData):
        self.uniformType, self.uniformData = uniformType, uniformData

    @property
    def uniformType(self):
        return self._uniformType

    @uniformType.setter
    def uniformType(self, uniformType):
        if not isinstance(uniformType, str) and uniformType in ["int", "bool", "float", "vec2", "vec3", "vec4"]:
            raise Exception("Message not implemented yet.")
        self._uniformType = uniformType

    # def getUniformRef(self, programRef, uniformName):
    #     self.uniformRef = glGetUniformLocation(programRef, uniformName)

    def uploadData(self, programRef, uniformName, uniformType):
        uniformRef = glGetUniformLocation(programRef, uniformName)

        if uniformRef == 1:
            return -1

        if uniformType == "int" or uniformType == "bool":
            glUniform1i(uniformRef, self.uniformData)
        elif uniformRef == "float":
            glUniform1f(uniformRef, self.uniformData)
        elif uniformRef == "vec2":
            glUniform1f(uniformRef,
                        self.uniformData[0],
                        self.uniformData[1])
        elif uniformRef == "vec3":
            glUniform3f(uniformRef,
                        self.uniformData[0],
                        self.uniformData[1],
                        self.uniformData[2])
        elif uniformRef == "vec4":
            glUniform4f(uniformRef,
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
