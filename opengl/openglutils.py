from OpenGL.GL import *
from opengl.openglconstants import *
import numpy as np


class OpenGLUtils(object):
    @staticmethod
    def initializeShader(shaderCode, shaderType):
        shaderCode = '#version 330 \n' + shaderCode
        shaderRef = glCreateShader(shaderType)

        glShaderSource(shaderRef, shaderCode)
        glCompileShader(shaderRef)

        if not glGetShaderiv(shaderRef, GL_COMPILE_STATUS):
            errorMessage = glGetShaderInfoLog(shaderRef)
            glDeleteShader(shaderRef)
            errorMessage = '\n' + errorMessage.decode()
            raise Exception(errorMessage)

        return shaderRef

    @staticmethod
    def initializeProgram(vertexShaderCode, fragmentShaderCode):
        vertexShaderRef = OpenGLUtils.initializeShader(vertexShaderCode, GL_VERTEX_SHADER)
        fragmentShaderRef = OpenGLUtils.initializeShader(fragmentShaderCode, GL_FRAGMENT_SHADER)

        programRef = glCreateProgram()

        glAttachShader(programRef, vertexShaderRef)
        glAttachShader(programRef, fragmentShaderRef)

        glLinkProgram(programRef)

        if not glGetProgramiv(programRef, GL_LINK_STATUS):
            errorMessage = glGetProgramInfoLog(programRef)
            glDeleteProgram(programRef)
            errorMessage = '\n' + errorMessage.decode()
            raise Exception(errorMessage)

        glDeleteShader(vertexShaderRef)
        glDeleteShader(fragmentShaderRef)

        return programRef

    @staticmethod
    def uploadData(buffer, data, method):
        glBindBuffer(GL_ARRAY_BUFFER, buffer)
        glBufferData(GL_ARRAY_BUFFER, data.nbytes(), data.astype(np.float32), method)

    @staticmethod
    def linkVertexAttribute(programRef, buffer, attribName, attribType, stride=0, offset=None):
        attribRef = glGetAttribLocation(programRef, attribName)

        if attribRef == -1:
            return -1

        glBindBuffer(GL_ARRAY_BUFFER, buffer)

        if attribType == "int":
            glVertexAttribPointer(attribRef, 1, GL_INT, False, stride, offset)
        elif attribType == "float":
            glVertexAttribPointer(attribRef, 1, GL_FLOAT, False, stride, offset)
        elif attribType == "vec2":
            glVertexAttribPointer(attribRef, 2, GL_FLOAT, False, stride, offset)
        elif attribType == "vec3":
            glVertexAttribPointer(attribRef, 3, GL_FLOAT, False, stride, offset)
        elif attribType == "vec4":
            glVertexAttribPointer(attribRef, 4, GL_FLOAT, False, stride, offset)
        else:
            raise Exception("Attribute " + attribName + " has wrong type: " + attribType)

        glEnableVertexAttribArray(attribRef)

        return 0
