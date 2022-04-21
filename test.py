from core.renderer import Renderer
from core.scene import Scene
from core.camera import Camera
from core.mesh import Mesh
from geometry.geometry import *
from material.material import *
from core.window import Window
import pyglet

def main():

    renderer, scene, camera = Renderer(), Scene(), Camera()

    geometry = TorusGeometry()
    material = SurfaceMaterial()
    mesh = Mesh(geometry, material)

    scene.add(mesh)
    mesh.translate(0, 0, -5)

    win = Window(renderer, scene, camera)



if __name__ == '__main__':
    main()



