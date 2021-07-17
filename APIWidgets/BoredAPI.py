from asciimatics.effects import Background
import requests
import json
from .APIWidget import APIWidget
from asciimatics.widgets import Frame, ListBox, Layout, Divider, Text, \
    Button, TextBox, Widget, Label

class BoredAPI(APIWidget):
    def __init__(self, screen, height,width):
        self.url = "https://www.boredapi.com/api/activity" 
        self.id = 0
        self.Tile = self.createTile(screen, height, width)
        self.fetch_data()
       # self.detailView = self.createDetailView()
        super(BoredAPI,self).__init__(screen, height,width)

    # defines the tile layout
    def createTile(self,screen, height,width):
        tile = Frame(screen, height,width, title="BoredAPI", can_scroll=False, reduce_cpu=True)
        if not "idea" in tile.data:
            tile.data = {"idea":""}
        layout = Layout([1])
        tile.add_layout(layout)
        layout.add_widget(Label("", align="^"))
        layout.add_widget(Label("", align="^"))
        layout.add_widget(Label("Bored?", align="^"))
        layout.add_widget(Label("Here's an idea:", align="^"))
        layout.add_widget(Label("", align="^"))
        layout.add_widget(Text("",name="idea", readonly=True))
        buttonBar = Layout([1, 1,1])
        tile.add_layout(buttonBar)
        layout.add_widget(Label("", align="^"))
        layout.add_widget(Label("", align="^"))
        buttonBar.add_widget(Button('A New One!', self.fetch_data, None), 1)
        tile.fix()
        return tile


 

    # TODO: not yet implemented in dashboard
    def create_detail_view(self):
        pass

    # get api data
    def fetch_data(self):
        response = requests.request("GET",self.url)
        self.Tile.data = {"idea": response.json()["activity"]}
        self.Tile.save()
        self.Tile.reset()

        
