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


class PointGeometry(Geometry):
    def __init__(self):
        super().__init__()

        positionData = [0, 0, 0]
        colorData = [1, 1, 1]

        self.addAttrib("vec3", "vertexPosition", positionData)
        self.addAttrib("vec3", "vertexColor", colorData)

        self.vertexCount = 1

class BoundingBoxGeometry(Geometry):
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

        positionData = [p0, p1, p0, p2, p0, p4, p1, p3, p1, p5, p2, p3, p2, p6, p3, p7, p4, p5, p4, p6, p5, p7, p6, p7]

        c0 = [1, 1, 1]

        colorData = [c0 * 24]

        self.addAttrib("vec3", "vertexPosition", positionData)
        self.addAttrib("vec3", "vertexColor", colorData)

        self.countVertex()

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


class ParametricGeometry(Geometry):
    def __init__(self, u0, un, uRes, v0, vn, vRes, S):
        super().__init__()

        du = (un - u0) / uRes
        dv = (vn - v0) / vRes

        position = []

        for uIndex in range(uRes + 1):
            vArray = []
            for vIndex in range(vRes + 1):
                u = u0 + uIndex * du
                v = v0 + vIndex * dv
                vArray.append(S(u, v))
            position.append(vArray)

        positionData = []
        colorData = []

        c0, c1, c2 = [1, 0, 0], [0, 1, 0], [0, 0, 1]
        c3, c4, c5 = [0, 1, 1], [1, 0, 1], [1, 1, 0]

        for xIndex in range(uRes):
            for yIndex in range(vRes):
                pA = position[xIndex][yIndex]
                pB = position[xIndex + 1][yIndex]
                pC = position[xIndex + 1][yIndex + 1]
                pD = position[xIndex][yIndex + 1]

                positionData += [pA.copy(), pB.copy(), pC.copy(), pA.copy(), pC.copy(), pD.copy()]
                colorData += [c0, c1, c2, c3, c4, c5]

        self.addAttrib("vec3", "vertexPosition", positionData)
        self.addAttrib("vec3", "vertexColor", colorData)

        self.countVertex()


class PlaneGeometry(ParametricGeometry):
    def __init__(self, width=1, height=1, widthSegments=8, heightSegments=8):
        def S(u, v):
            return [u, v, 0]
        super().__init__(-width/2, width/2, widthSegments, -height/2, height/2, heightSegments, S)


class EllipsoidGeometry(ParametricGeometry):
    def __init__(self, width=1, height=1, depth=1, radiusSegments=32, heightSegments=16):
        def S(u, v):
            return [width / 2 * sin(u) * cos(v), height / 2 * sin(v), depth / 2 * cos(u) * cos(v)]
        super().__init__(0, 2 * pi, radiusSegments, - pi / 2, pi / 2, heightSegments, S)


class SphereGeometry(EllipsoidGeometry):
    def __init__(self, radius=1, radiusSegments=32, heightSegments=16):
        super().__init__(2 * radius, 2 * radius, 2 * radius, radiusSegments, heightSegments)


class TorusGeometry(ParametricGeometry):
    def __init__(self, R=1, r=1/4, radiusSegments=32, heightSegments=16):
        def S(u, v):
            return [(R + r * cos(v)) * cos(u), (R + r * cos(v)) * sin(u), r * sin(v)]
        super().__init__(0, 2 * pi, radiusSegments, 0, 2 * pi, heightSegments, S)


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

