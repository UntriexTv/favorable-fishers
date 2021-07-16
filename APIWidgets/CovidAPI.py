from asciimatics.widgets import Frame, ListBox, Layout, Divider, Text, Button, TextBox, Widget, Label
from asciimatics.scene import Scene
from asciimatics.screen import Screen
from asciimatics.exceptions import ResizeScreenError, NextScene, StopApplication
import sys
from .APIWidget import APIWidget
import requests
import json


class covidView(APIWidget):
    def __init__(self, screen, height=15, width=50, x=0, y=0, can_scroll=False):
        super(covidView, self).__init__("")
        self.needs_refresh = False
        self.settings_open = False
        self.Tile = self.createTile(screen, height, width)



    def createTile(self, screen, height, width):
        fr = Frame(screen, height, width, can_scroll=False)
        # create the layout
        layout = Layout([100], fill_frame=True)
        fr.add_layout(layout)
        self.json_data = self.fetch_data()

        # add all the labels
        layout.add_widget(Label('Country:   ' + str(self.json_data['Country'])))
        layout.add_widget(Label('Confirmed: ' + str(self.json_data['Confirmed'])))
        layout.add_widget(Label('Deaths:    ' + str(self.json_data['Deaths'])))
        layout.add_widget(Label('Recovered: ' + str(self.json_data['Recovered'])))
        layout.add_widget(Label('Active:    ' + str(self.json_data['Active'])))
        layout.add_widget(Label('Date:      ' + str(self.json_data['Date'])))

        if self.settings_open == True:
            layout.add_widget(Text('Country:', 'country'))

        # creating the bottom bar of widgets
        buttonBar = Layout([1, 1,1,1])
        fr.add_layout(buttonBar)
        buttonBar.add_widget(Button('Config', self._config, None), 1)
        buttonBar.add_widget(Button('Quit', self._quit, None), 3)
        fr.fix()
        return fr

    @staticmethod
    def _quit():
        raise StopApplication('User pressed quit')

    def _config(self):
        if self.settings_open == True:
            self.settings_open = False
        else:
            self.settings_open = True


    def fetch_data(self):
        # getting the json data from the covid api and return the latest data point
        url = 'https://api.covid19api.com/live/country/united-kingdom/status/confirmed'
        payload = {}
        headers = {}
        response = requests.request('GET', url, headers=headers, data=payload)
        data = response.json()

        return data[len(data)-1]