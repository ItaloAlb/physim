from OpenGL.GL import *
from opengl.openglutils import OpenGLUtils
from opengl.uniform import Uniform


#   Material class will specify the general appearance of an object.
#   It will store three types of data related to rendering:
#   (i) shader program references; (ii) Uniform objects, (iii) OpenGL render settings.
class Material(object):
    def __init__(self, vertexShaderCode, fragmentShaderCode):
        # Initialize program using a vertex shader code and a fragment shader code
        self.programRef = OpenGLUtils.initializeProgram(vertexShaderCode, fragmentShaderCode)

        # Initialize uniforms dictionary
        self.uniforms = {"modelMatrix": Uniform("mat4", None),
                         "viewMatrix": Uniform("mat4", None),
                         "projectionMatrix": Uniform("mat4", None)}

        # Initialize settings dictionary
        self.settings = {"drawStyle": GL_TRIANGLES}

    # Add a uniform to an Uniforms dictionary.
    def addUniform(self, uniformDataType, uniformName, uniformData):
        self.uniforms[uniformName] = Uniform(uniformDataType, uniformData)

    # Set all uniforms reference to later use.
    def setUniformsRef(self):
        for uniformName, uniformObject in self.uniforms.items():
            uniformObject.setUniformRef(self.programRef, uniformName)

    # Configure opengl with render settings.
    def updateRenderSettings(self):
        pass

    # not implemented yet.
    def setProperties(self, properties):
        pass


class BasicMaterial(Material):
    def __init__(self):
        vertexShaderCode = """
        uniform mat4 projectionMatrix;
        uniform mat4 viewMatrix;
        uniform mat4 modelMatrix;
        in vec4 vertexPosition;
        in vec4 vertexColor;
        out vec4 color;
        
        void main()
        {
            gl_Position = projectionMatrix * viewMatrix * modelMatrix * vertexPosition;
            color = vertexColor;
        }
        """

        fragmentShaderCode = """
        uniform vec4 baseColor;
        uniform bool useVertexColor;
        in vec4 color;
        out vec4 fragColor;
        
        void main()
        {
            vec4 tempColor = baseColor;
            
            if(useVertexColor)
                tempColor *= color;
            
            fragColor = tempColor;
        }
        """
        
        super().__init__(vertexShaderCode, fragmentShaderCode)

        self.addUniform("vec4", "baseColor", [1.0, 1.0, 1.0, 1.0])
        self.addUniform("bool", "useVertexColor", False)
        self.setUniformsRef()

class PointMaterial(BasicMaterial):
    def __init__(self, properties={}):
        super().__init__()

        self.settings["drawStyle"] = GL_POINTS
        self.settings["pointSize"] = 8
        self.settings["roundedPoint"] = False

        self.setProperties(properties)

    def updateRenderSettings(self):
        glPointSize(self.settings["pointSize"])

        if self.settings["roundedPoint"]:
            glEnable(GL_POINT_SMOOTH)
        else:
            glDisable(GL_POINT_SMOOTH)


class LineMaterial(BasicMaterial):
    def __init__(self, properties={}):
        super().__init__()
        self.settings["drawStyle"] = GL_LINE_STRIP
        self.settings["lineWidth"] = 1
        # line type: "strip" | "loop" | "segments"
        self.settings["lineType"] = "strip"

        self.setProperties(properties)

    def updateRenderSettings(self):
        glLineWidth(self.settings["lineWidth"])

        if self.settings["lineType"] == "strip":
            self.settings["drawStyle"] = GL_LINE_STRIP
        elif self.settings["lineType"] == "loop":
            self.settings["drawStyle"] = GL_LINE_LOOP
        elif self.settings["lineType"] == "segments":
            self.settings["drawStyle"] = GL_LINES
        else:
            raise Exception("Unknown LineMaterial line type")


class SurfaceMaterial(BasicMaterial):
    def __init__(self, properties={}):
        super().__init__()

        self.settings["drawStyle"] = GL_TRIANGLES
        self.settings["doubleSide"] = False
        self.settings["wireframe"] = False
        self.settings["lineWidth"] = 1

        self.setProperties(properties)

    def updateRenderSettings(self):
        if self.settings["doubleSide"]:
            glEnable(GL_CULL_FACE)
        else:
            glDisable(GL_CULL_FACE)

        if self.settings["wireframe"]:
            glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
        else:
            glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)

        glLineWidth(self.settings["lineWidth"])
