from OpenGL.GL import *
import numpy as np

#   Attribute class will manage opengl attributes such as position and color
#   It will handle two main tasks: (i) upload data to a buffer; (ii) set a link between program and attribute
class Attribute(object):
    def __init__(self, attribType, attribData):
        self.attribType, self.attribData = attribType, attribData
        self.VBO = glGenBuffers(1)

    @property
    def attribType(self):
        return self._attribType

    @attribType.setter
    def attribType(self, attribType):
        if not isinstance(attribType, str) and attribType in ["int", "float", "vec2", "vec3", "vec4"]:
            raise Exception("Message not implemented yet.")
        self._attribType = attribType

    def setData(self, attribData):
        self.attribData = attribData

    # method: (i) static, (ii) dynamic
    def uploadData(self, method):
        glBindBuffer(GL_ARRAY_BUFFER, self.VBO)
        data = np.array(self.attribData).astype(np.float32)
        glBufferData(GL_ARRAY_BUFFER, data.nbytes, data, method)
        glBindBuffer(GL_ARRAY_BUFFER, 0)

    def setLink(self, programRef, attribName, stride=0, offset=None):
        attribRef = glGetAttribLocation(programRef, attribName)

        if attribRef == -1:
            return -1

        glBindBuffer(GL_ARRAY_BUFFER, self.VBO)

        if self.attribType == "int":
            glVertexAttribPointer(attribRef, 1, GL_INT, False, stride, offset)
        elif self.attribType == "float":
            glVertexAttribPointer(attribRef, 1, GL_FLOAT, False, stride, offset)
        elif self.attribType == "vec2":
            glVertexAttribPointer(attribRef, 2, GL_FLOAT, False, stride, offset)
        elif self.attribType == "vec3":
            glVertexAttribPointer(attribRef, 3, GL_FLOAT, False, stride, offset)
        elif self.attribType == "vec4":
            glVertexAttribPointer(attribRef, 4, GL_FLOAT, False, stride, offset)
        else:
            raise Exception("Attribute " + attribName + " has wrong type: " + self.attribType)

        glEnableVertexAttribArray(attribRef)

        return 0
