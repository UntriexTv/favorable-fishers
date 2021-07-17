import sys

from WidgetManager import WidgetManager
from Dashboard import Dashboard

from asciimatics.screen import Screen
from asciimatics.exceptions import ResizeScreenError


"""
The application is initialized using an asciimatics wrapper
"""


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
