from opengl.attribute import Attribute
from math import pi, cos, sin

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
    def __init__(self, width=1.0, height=1.0):
        super().__init__()
        p0, p1, p2, p3 = [-width/2, height/2, 0.0], \
                         [width/2, height/2, 0.0], \
                         [-width/2, -height/2, 0.0], \
                         [width/2, -height/2, 0.0]

        # vertex: top left, top right, bottom left, bottom right
        c0, c1, c2, c3 = [1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0], [1.0, 1.0, 1.0]

        positionData = [p0, p1, p2, p1, p2, p3]
        colorData = [c0, c1, c2, c1, c2, c3]

        self.addAttrib("vec3", "vertexPosition", positionData)
        self.addAttrib("vec3", "vertexColor", colorData)

        self.vertexCount = 6


class PolygonGeometry(Geometry):
    def __init__(self, radius, sides: int = 3):
        super().__init__()

        a = 2 * pi / sides

        positionData = []
        colorData = []

        for n in range(sides):
            positionData.append([0, 0, 0])
            positionData.append([radius * cos(n * a), radius * sin(n * a), 0])
            positionData.append([radius * cos((n + 1) * a), radius * sin((n + 1) * a), 0])

            # vertex: center, left, right
            colorData.append([1, 1, 1])
            colorData.append([1, 0, 0])
            colorData.append([0, 0, 1])

        self.addAttrib("vec3", "vertexPosition", positionData)
        self.addAttrib("vec3", "vertexColor", colorData)

        self.countVertex()



class BoxGeometry(Geometry):
    def __init__(self, width=1, height=1, depth=1):
        super().__init__()
        p0, p1, p2, p3, p4, p5, p6, p7 = [-width/2, height/2, -depth/2], \
                                         [width / 2, height / 2, -depth / 2], \
                                         [-width / 2, -height / 2, -depth / 2], \
                                         [width / 2, -height / 2, -depth / 2], \
                                         [-width / 2, height / 2, depth / 2], \
                                         [width / 2, height / 2, depth / 2], \
                                         [-width / 2, -height / 2, depth / 2], \
                                         [width / 2, -height / 2, depth / 2]

        positionData = [p0, p1, p2, p1, p2, p3, p4, p5, p6, p5, p6, p7, p0, p2, p4, p2, p4, p6, p1, p3, p5, p3, p5, p7, p0, p1, p4, p1, p4, p5, p2, p3, p6, p3, p6, p7]

        # face: z+, z-
        c0, c1 = [1, 0.5, 0.5], [0.5, 0, 0]
        # face: x+, x-
        c2, c3 = [0.5, 1, 0.5], [0, 0.5, 0]
        # face: y+, y-
        c4, c5 = [0.5, 0.5, 1], [0, 0, 0.5]

        colorData = [c1] * 6 + [c0] * 6 + [c3] * 6 + [c2] * 6 + [c5] * 6 + [c4] * 6

        self.addAttrib("vec3", "vertexPosition", positionData)
        self.addAttrib("vec3", "vertexColor", colorData)

        self.countVertex()

