from logging import exception
from asciimatics.effects import Background
import requests
import json
from .APIWidget import APIWidget
from asciimatics.widgets import Frame, ListBox, Layout, Divider, Text, \
    Button, TextBox, Widget, Label

class JokeAPI(APIWidget):
    def __init__(self, screen, height,width):
        self.url = "https://official-joke-api.appspot.com/random_joke" 

        self.Tile = self.createTile(screen, height, width)
        self.fetch_data()
       # self.detailView = self.createDetailView()
        super(JokeAPI,self).__init__(screen, height,width)

    # defines the tile layout
    def createTile(self,screen, height,width):
        tile = Frame(screen, height,width, title="JokeAPI", can_scroll=False, reduce_cpu=True)
        if not "setup" in tile.data:
            tile.data = {"setup":""}
        layout = Layout([1])
        tile.add_layout(layout)
        layout.add_widget(Label("", align="^"))
        layout.add_widget(Text("",name="setup", readonly=True))
        layout.add_widget(Label("", align="^"))
        layout.add_widget(Text("",name="punchline", readonly=True))
        layout.add_widget(Label("", align="^"))
        buttonBar = Layout([1, 1,1])
        tile.add_layout(buttonBar)
        layout.add_widget(Label("", align="^"))
        layout.add_widget(Label("", align="^"))
        buttonBar.add_widget(Button('Another!', self.fetch_data, None), 1)
        tile.fix()
        return tile
 

    # TODO: not yet implemented in dashboard
    def createDetailView(self):
        pass

    # get api data
    def fetch_data(self):
        response = requests.request("GET",self.url)
        json_data =  response.json()

        self.Tile.data = {
            "setup":json_data["setup"]
            ,"punchline":json_data["punchline"]
        }
        self.Tile.save()
        self.Tile.reset()

        
