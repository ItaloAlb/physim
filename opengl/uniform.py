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
        if not isinstance(uniformType, str) and uniformType in ["int", "bool", "float", "vec2", "vec3", "vec4", "mat4"]:
            raise Exception("Message not implemented yet.")
        self._uniformType = uniformType

    def setUniformRef(self, programRef, uniformName):
        self.uniformRef = glGetUniformLocation(programRef, uniformName)

    def uploadData(self):

        if self.uniformRef == -1:
            return -1

        if self.uniformType == "int" or self.uniformType == "bool":
            glUniform1i(self.uniformRef, self.uniformData)
        elif self.uniformType == "float":
            glUniform1f(self.uniformRef, self.uniformData)
        elif self.uniformType == "vec2":
            glUniform2f(self.uniformRef,
                        self.uniformData[0],
                        self.uniformData[1])
        elif self.uniformType == "vec3":
            glUniform3f(self.uniformRef,
                        self.uniformData[0],
                        self.uniformData[1],
                        self.uniformData[2])
        elif self.uniformType == "vec4":
            glUniform4f(self.uniformRef,
                        self.uniformData[0],
                        self.uniformData[1],
                        self.uniformData[2],
                        self.uniformData[3])
        elif self.uniformType == "mat4":
            glUniformMatrix4fv(self.uniformRef, 1, False, self.uniformData)
        return 0
