from asciimatics.scene import Scene
from asciimatics.screen import Screen
from asciimatics.exceptions import ResizeScreenError, NextScene, StopApplication
import sys
from covid import *
from calculator import *
from weather import *


def demo(screen, scene):
    # define the size of each frame
    height = 15
    width = 50

    # make all the scenes
    scenes = [
        Scene([
            covidView(screen, height, width, 0, 0), 
            covidView(screen, height, width, 0, 1), 
            covidView(screen, height, width, 1, 0),
            covidView(screen, height, width, 1, 1)
            ], -1, name='Main'),
    ]

    # running all the scenes
    screen.play(scenes, stop_on_resize=True, start_scene=scenes[0], allow_int=True)


last_scene = None
while True:
    try:
        Screen.wrapper(demo, catch_interrupt=True, arguments=[last_scene])
        sys.exit(0)
    except ResizeScreenError as e:
        last_scene = e.scene