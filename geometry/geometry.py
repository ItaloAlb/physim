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
    def __init__(self, width=1.0, height=1.0):
        super().__init__()
        p0, p1, p2, p3 = [-width/2, height/2, 0.0], \
                         [width/2, height/2, 0.0], \
                         [-width/2, -height/2, 0.0], \
                         [width/2, -height/2, 0.0]
        c0, c1, c2, c3 = [1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0], [1.0, 1.0, 1.0]
        positionData = [p0, p1, p2, p1, p2, p3]
        colorData = [c0, c1, c2, c1, c2, c3]

        self.addAttrib("vec3", "vertexPosition", positionData)
        self.addAttrib("vec3", "vertexColor", colorData)

        self.vertexCount = 6


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

        c0, c1, c2, c3, c4, c5, c6, c7 = [1.0, 1.0, 1.0], [1.0, 1.0, 1.0], [1.0, 1.0, 1.0], [1.0, 1.0, 1.0], [1.0, 1.0, 1.0], [1.0, 1.0, 1.0], [1.0, 1.0, 1.0], [1.0, 1.0, 1.0]

        colorData = [c0, c1, c2, c1, c2, c3, c4, c5, c6, c5, c6, c7, c0, c2, c4, c2, c4, c6, c1, c3, c5, c3, c5, c7, c0, c1, c4, c1, c4, c5, c2, c3, c6, c3, c6, c7]


        self.addAttrib("vec4", "vertexPosition", positionData)
        self.addAttrib("vec4", "vertexColor", colorData)

        self.vertexCount = len(positionData)