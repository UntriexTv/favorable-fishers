from asciimatics.screen import Screen
from asciimatics.scene import Scene
from WidgetManager import WidgetManager
from Dashboard import Dashboard
from APIWidgets.Placeholder import Placeholder

from asciimatics.exceptions import ResizeScreenError, NextScene, StopApplication
import sys


# initialize the application
def app(screen, scene):
    dashboard = Dashboard(screen, widgetmanager)
    screen.play([dashboard], stop_on_resize=True, start_scene=scene, allow_int=True) 


widgetmanager = WidgetManager()
last_scene = None
while True:
    try:
        Screen.wrapper(app, catch_interrupt=True, arguments=[last_scene])
        sys.exit(0)
    except ResizeScreenError as e:
        pass
        last_scene = e.scene
