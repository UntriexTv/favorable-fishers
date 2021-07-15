from asciimatics.effects import Background
import requests
import json
from .APIWidget import APIWidget
from asciimatics.widgets import Frame, ListBox, Layout, Divider, Text, \
    Button, TextBox, Widget, Label

class BoredAPI(APIWidget):
    def __init__(self, screen,_title):
        self.url = "https://www.boredapi.com/api/activity" 
        self.title = _title#"BoredAPI"
        self.apiData = self.apiCall()
        self.screen = screen
        self.Tile = self.createTile()
       # self.createDetailView()
        super(BoredAPI,self).__init__(self.url)

    def createTile(self):
        tile = Frame(self.screen,15,50)#super().height,super().width)
        tile.add_effect(Background(self.screen,4))
        layout = Layout([1])
        tile.add_layout(layout)
        layout.add_widget(Label(self.apiData))
        return tile

    def apiCall(self):
        response = requests.request("GET",self.url)
        #print(response.json())
        #print(response.json()["activity"])
        return response.json()["activity"]

    def move(self,x,y):
        super().move(x,y)
        
