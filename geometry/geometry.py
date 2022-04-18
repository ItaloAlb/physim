from opengl.attribute import Attribute


class Geometry(object):
    def __init__(self):
        self.attrib = []

    def addAttrib(self, attribType, attribName, attribData):
        self.attrib[attribName] = Attribute(attribType, attribData)


class RectangleGeometry(Geometry):
    def __init__(self, width, height):
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
