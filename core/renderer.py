from core.mesh import Mesh
from OpenGL.GL import *


class Renderer(object):
    def __init__(self, clearColor: tuple = (0, 0, 0, 1)):
        glEnable(GL_DEPTH_TEST)
        # required for antialiasing
        glEnable(GL_MULTISAMPLE)
        glClearColor(clearColor[0], clearColor[1], clearColor[2], clearColor[3])

    def render(self, scene, camera):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # update camera view matrix
        camera.updateViewMatrix()

        descendantList = scene.getDescendant()
        meshFilter = lambda x: isinstance(x, Mesh)
        meshList = list(filter(meshFilter, descendantList))

        for mesh in meshList:
            if not mesh.visible:
                continue

            # setup mesh program
            glUseProgram(mesh.material.programRef)

            # bind VAO
            glBindVertexArray(mesh.VAO)

            mesh.material.uniforms["modelMatrix"].uniformData = mesh.getWorldMatrix()

            mesh.material.uniforms["viewMatrix"].uniformData = camera.viewMatrix

            mesh.material.uniforms["projectionMatrix"].uniformData = camera.projectionMatrix

            for uniformName, uniformObject in mesh.material.uniforms.items():
                uniformObject.uploadData()

            mesh.material.updateRenderSettings()

            glDrawArrays(mesh.material.settings["drawStyle"], 0, mesh.geometry.vertexCount)