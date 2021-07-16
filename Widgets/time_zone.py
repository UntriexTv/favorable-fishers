from asciimatics.widgets import Frame, ListBox, Layout, Divider, Text, Button, TextBox, Widget, Label
from asciimatics.scene import Scene
from asciimatics.screen import Screen
from asciimatics.exceptions import ResizeScreenError, NextScene, StopApplication
import sys
import requests
import json


class timeView(Frame):
    def __init__(self, screen, height, width, x, y, can_scroll):
        super().__init__(screen, height, width, x=x, y=y, can_scroll=can_scroll)
        self.needs_refresh = True
        
        # create the layout
        layout = Layout([100], fill_frame=True)
        self.add_layout(layout)
        self.json_data = self.fetch_data()

        # add all the labels




        # creating the bottom bar of buttons
        buttonBar = Layout([1, 1])
        self.add_layout(buttonBar)
        buttonBar.add_widget(Button('Quit', self._quit, None), 3)
        self.fix()

    @staticmethod
    def _quit():
        raise StopApplication('User pressed quit') 