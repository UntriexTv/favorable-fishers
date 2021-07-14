from asciimatics.effects import Background
import requests
import json
from .APIWidget import APIWidget
from asciimatics.widgets import Frame, ListBox, Layout, Divider, Text, \
    Button, TextBox, Widget, Label

class BoredAPI(APIWidget):
    def __init__(self,_title, screen):
        self.url = "https://www.boredapi.com/api/activity" 
        self.title = _title#"BoredAPI"
        self.apiData = self.apiCall()
        self.screen = screen
        self.createTile()
        self.createDetailView()

    def createTile(self):
        tile = Frame(self.screen,super().height,super().width)
        tile.add_effect(Background(self.screen,4))
        layout = Layout([1])
        tile.add_layout(layout)
        layout.add_widget(Label(self.apiData))

    def apiCall(self):
        response = requests.request("GET",self.url)
        #print(response.json())
        #print(response.json()["activity"])
        return response.json()["activity"]
