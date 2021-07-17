from asciimatics.widgets import Frame, ListBox, Layout, Divider, Text, Button, TextBox, Widget, Label
from asciimatics.scene import Scene
from asciimatics.screen import Screen
from asciimatics.exceptions import ResizeScreenError, NextScene, StopApplication
import sys
from .APIWidget import APIWidget
import requests
import json


class covidView(APIWidget):
    def __init__(self, screen, height, width):
        super(covidView, self).__init__(screen, height, width)
        self.needs_refresh = False
        self.settings_open = False
        self.data = {"country":"united-kingdom"}
        self.Tile = self.createTile(screen, height, width)
        self.screen = screen
        self.id = 1


    def createTile(self, screen, height, width):
        tile = Frame(screen, height, width, title="CovidAPI",can_scroll=False)
        # create the layout
        layout = Layout([100], fill_frame=True)
        tile.add_layout(layout)
        if not "Country" in tile.data:
            tile.data =self.fetch_data()
        #self.json_data = tile.data["covid"]

        # add all the labels
        layout.add_widget(Text('Country:   ' , name="Country", readonly=True))
        layout.add_widget(Text('Confirmed: ' , name="Confirmed", readonly=True))
        layout.add_widget(Text('Deaths:    ' , name='Deaths', readonly=True))
        layout.add_widget(Text('Recovered: ' , name='Recovered', readonly=True))
        layout.add_widget(Text('Active:    ' , name='Active', readonly=True))
        layout.add_widget(Text('Date:      ' , name='Date', readonly=True))


        # creating the bottom bar of widgets
        buttonBar = Layout([1, 1,1])
        tile.add_layout(buttonBar)
        button =Button('Config', self._config, None)
        buttonBar.add_widget(button, 1)
        tile.fix()
        return tile


    def _config(self):
        courtyList = [("United Kingdom","united-kingdom"),("Denmark","denmark"),("Germany","germany")]
        self._widget_list_view = ListBox(
            Widget.FILL_FRAME,
            courtyList,
            name="country",
            add_scroll_bar=True,
            on_select=self._alter_nation)#_addAPIWidget)

        self.menuFrame = Frame(self.screen,10,20)
        layout = Layout([1], fill_frame=True)
        self.menuFrame.add_layout(layout)
        layout.add_widget(self._widget_list_view)
        layout.add_widget(Divider())
        #send menuframe to dashboard
        self.screen._scenes[0].open_menu(self.menuFrame)

    def _alter_nation(self):
        self.screen._scenes[0]._cancel()
        self.menuFrame.save()
        self.data["country"] = self.menuFrame.data["country"]
        self.Tile.data = self.fetch_data()
        self.Tile.save()
        self.Tile.reset()


    def fetch_data(self):
        # getting the json data from the covid api and return the latest data point
        url = f'https://api.covid19api.com/live/country/{self.data["country"]}/status/confirmed'
        payload = {}
        headers = {}
        response = requests.request('GET', url, headers=headers, data=payload)
        data = response.json()[-1]

        retVal = {}
        for k,v in data.items():
            retVal[k] = str(v)
        return retVal 
