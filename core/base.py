import pyglet
from OpenGL.GL import *
from opengl.openglutils import OpenGLUtils
from opengl.attribute import Attribute

config = pyglet.gl.Config(double_buffer=True)

win = pyglet.window.Window(config=config)

vsCode = """
in vec3 position;
in vec3 vertexColor;
out vec3 color;
void main(){
    gl_Position = vec4(position, 1.0);
    color = vertexColor;
}"""
fsCode = """
in vec3 color;
out vec4 fragColor;
void main(){
    fragColor = vec4(color.r, color.g, color.b, 1.0f);
}"""
VAO = glGenVertexArrays(1)
programRef = OpenGLUtils.initializeProgram(vsCode, fsCode)
positionData = \
    [[-0.5, -0.5,  0. ],
    [ 0.5, -0.5,  0. ],
    [-0.5,  0.5,  0. ],
    [ 0.5, -0.5,  0. ],
    [-0.5,  0.5,  0. ],
    [ 0.5,  0.5,  0. ]]
positionAttribute = Attribute("vec3", positionData)
positionAttribute.uploadData(GL_DYNAMIC_DRAW)
positionAttribute.setLink(programRef, "position")
colorData = \
    [[1., 0., 0.],
    [0., 1., 0.],
    [0., 0., 1.],
    [0., 1., 0.],
    [0., 0., 1.],
    [1., 1., 1.]]
colorAttribute = Attribute("vec3", colorData)
colorAttribute.uploadData(GL_STATIC_DRAW)
successLink = colorAttribute.setLink(programRef, "vertexColor")
glUseProgram(programRef)
glDrawArrays(GL_TRIANGLES, 0, 6)
pyglet.app.run()
