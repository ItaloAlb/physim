from opengl.attribute import Attribute

#   Geometry class will specify the general shape and other vertex-related properties
#   Also this class will mainly serve to store Attribute (from opengl.attribute) objects
#   Which describe vertex properties such as position and color
class Geometry(object):
    def __init__(self):
        self.attrib = {}

        self.vertexCount = None

    def addAttrib(self, attribType, attribName, attribData):
        self.attrib[attribName] = Attribute(attribType, attribData)

    # Not implemented yet
    def countVertex(self):
        attrib = list(self.attrib.values())[0]
        self.vertexCount = len(attrib.attribData)


class RectangleGeometry(Geometry):
    def __init__(self, width=1, height=1):
        super().__init__()
        p0, p1, p2, p3 = [-width/2, -height/2, 0], \
                         [width/2, -height/2, 0], \
                         [-width/2, height/2, 0], \
                         [width/2, height/2, 0]
        c0, c1, c2, c3 = [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]
        positionData = [p0, p1, p2, p0, p2, p3]
        colorData = [c0, c1, c2, c0, c2, c3]

        self.addAttrib("vec3", "vertexPosition", positionData)
        self.addAttrib("vec4", "vertexColor", colorData)

        self.vertexCount = 6


class BoxGeometry(Geometry):
    def __init__(self):
        super().__init__()
