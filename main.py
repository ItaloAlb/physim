from core.renderer import Renderer
from core.scene import Scene
from core.camera import Camera
from core.mesh import Mesh
from geometry.geometry import *
from material.material import *
from physics.particlesystem import *
import pyglet


def main():
    config = pyglet.gl.Config(double_buffer=True, sample_buffers=1, samples=4)

    win = pyglet.window.Window(config=config)

    renderer = Renderer()
    scene = Scene()
    camera = Camera()

    camera.translate(0, 0, 2)

    particleSystem = ParticleSystem()

    scene.add(particleSystem.boundBoxMesh)
    scene.add(particleSystem.particleMesh)


    def update(dt:float):
        particleSystem()
        # mesh.rotate(0, 0.1, 0.1)


    clock = pyglet.clock.schedule_interval(update, 1/120)

    @win.event
    def on_draw():
        win.clear()
        renderer.render(scene, camera)

    @win.event
    def on_mouse_drag(x, y, dx, dy, buttons, modifiers):
        if buttons & pyglet.window.mouse.RIGHT:
            scene.rotate(- dy/10, dx/10, 0)

    @win.event
    def on_mouse_scroll(x, y, scroll_x, scroll_y):
        camera.translate(0, 0, - scroll_y)

    # @win.event
    # def on_key_press(symbol, modifiers):
    #     if symbol == pyglet.window.key.A:
    #         camera.translate(-0.1, 0, 0)
    #     if symbol == pyglet.window.key.D:
    #         camera.translate(0.1, 0, 0)
    #     if symbol == pyglet.window.key.W:
    #         camera.translate(0, 0.1, 0)
    #     if symbol == pyglet.window.key.S:
    #         camera.translate(0,-0.1, 0)

    pyglet.app.run()


if __name__ == '__main__':
    main()

