from asciimatics.screen import Screen
from asciimatics.scene import Scene
from APImanager import APImanager
from Dashboard import Dashboard
from APIWidgets.Placeholder import Placeholder

from asciimatics.exceptions import ResizeScreenError, NextScene, StopApplication
import sys




def app(screen, scene):
    scenes = [
        #Scene([Dashboard(screen, apiManager)], -1, name="Dashboard"),
       # Scene([Placeholder(screen, apiManager)], -1, name="APIWidget")
	   Dashboard(screen)
    ]
    print(scenes)
    screen.play(scenes, stop_on_resize=True, start_scene=scenes[0], allow_int=True) 



apiManager = APImanager()
last_scene = None
while True:
    try:
        Screen.wrapper(app, catch_interrupt=True, arguments=[last_scene])
        sys.exit(0)
    except ResizeScreenError as e:
        last_scene = e.scene