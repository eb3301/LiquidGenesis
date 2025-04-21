import genesis as gs
import pyglet
from OpenGL.GL import glGetString, GL_VERSION

pyglet.options['debug_gl'] = False
pyglet.options['shadow_window'] = False
pyglet.options['vsync'] = False
pyglet.options['headless'] = False



gs.init(
    seed                = None,
    precision           = '32',
    debug               = False,
    eps                 = 1e-12,
    logging_level       = None,
    backend             = gs.cpu,
    theme               = 'dark',
    logger_verbose_time = 'Debug'
)

scene = gs.Scene(show_viewer=True)
plane = scene.add_entity(gs.morphs.Plane())
franka = scene.add_entity(
    gs.morphs.MJCF(file='xml/franka_emika_panda/panda.xml'),
)

scene.build()
scene.show()

import time
time.sleep(1)  # aspetta che il viewer appaia

print("OpenGL Version:", glGetString(GL_VERSION))



for i in range(1000):
    scene.step()