from asciimatics.widgets import Frame, ListBox, Layout, Divider, Text, Button, TextBox, Widget, Label
from asciimatics.scene import Scene
from asciimatics.screen import Screen
from asciimatics.exceptions import ResizeScreenError, NextScene, StopApplication
import sys
import requests
import requests
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
        layout.add_widget(Label('Recovered: ' + str(self.json_data['Recovered'])))
        layout.add_widget(Label('Active:    ' + str(self.json_data['Active'])))
        layout.add_widget(Label('Date:      ' + str(self.json_data['Date'])))

        buttonBar = Layout([1, 1, 1, 1, 1])
        self.add_layout(buttonBar)
        buttonBar.add_widget(Button('Config', self._config, None), 1)
        buttonBar.add_widget(Button('Quit', self._quit, None), 3)
        self.fix()

    @staticmethod
    def _quit():
        raise StopApplication('User pressed quit')

    @staticmethod
    def _config():
        # this function is to configure the widget i.e. change the country 
        pass

    def fetch_data(self):
        url = 'https://api.covid19api.com/live/country/united-kingdom/status/confirmed'

        payload = {}
        headers = {}

        response = requests.request('GET', url, headers=headers, data=payload)

        data = response.json()

        return data[len(data)-1]

def demo(screen, scene):

    height = 15
    width = 50
    scenes = [
        Scene([
            covidView(screen, height, width, 0, 0), 
            covidView(screen, height, width, 0, 1), 
            covidView(screen, height, width, 1, 0),
            covidView(screen, height, width, 1, 1)
            ], -1, name='Main'),
    ]

    screen.play(scenes, stop_on_resize=True, start_scene=scenes[0], allow_int=True)



last_scene = None
while True:
    try:
        Screen.wrapper(demo, catch_interrupt=True, arguments=[last_scene])
        sys.exit(0)
    except ResizeScreenError as e:
        last_scene = e.scene





