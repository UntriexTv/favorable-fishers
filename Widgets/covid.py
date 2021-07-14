from asciimatics.widgets import Frame, ListBox, Layout, Divider, Text, Button, TextBox, Widget, Label
from asciimatics.scene import Scene
from asciimatics.screen import Screen
from asciimatics.exceptions import ResizeScreenError, NextScene, StopApplication
import sys
from requests import request
import json

class covidView(Frame):
    def __init__(self, screen, height, width, x, y, can_scroll=False):
        super(covidView, self).__init__(screen, height, width, x=x, y=y, can_scroll=can_scroll)
        self.needs_refresh = False

        # create the layout
        layout = Layout([100], fill_frame=True)
        self.add_layout(layout)
        self.json_data = self.fetch_data()

        layout.add_widget(Label('Country:   ' + str(self.json_data['Country'])))
        layout.add_widget(Label('Confirmed: ' + str(self.json_data['Confirmed'])))
        layout.add_widget(Label('Deaths:    ' + str(self.json['Deaths'])))
        

