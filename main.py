from core.renderer import Renderer
from core.scene import Scene
from core.camera import Camera
from core.mesh import Mesh
from geometry.geometry import *
from material.material import *
import pyglet

import numpy as np


def main():
    config = pyglet.gl.Config(double_buffer=True)

    win = pyglet.window.Window(config=config)

    renderer = Renderer()
    scene = Scene()
    camera = Camera()

    geometry = RectangleGeometry()
    material = SurfaceMaterial()

    mesh = Mesh(geometry, material)

    mesh.translate(0.0, 0.0, -5.0)

    mesh.rotate(0.0, 0.0, 0.0)

    scene.add(mesh)

    def update(dt:float):
        mesh.rotate(1, 1, 1, False)
        # mesh.rotateZ(1, False)
        # mesh.scale(1.001, 1.001, 1.0)


    clock = pyglet.clock.schedule_interval(update, 1/120)

    @win.event
    def on_draw():
        win.clear()
        renderer.render(scene, camera)


    pyglet.app.run()


if __name__ == '__main__':
    main()

