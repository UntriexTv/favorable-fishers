from logging import exception
from asciimatics.effects import Background
import requests
import json
from .APIWidget import APIWidget
from asciimatics.widgets import Frame, ListBox, Layout, Divider, Text, \
    Button, TextBox, Widget, Label

class CryptoAPI(APIWidget):
    def __init__(self, screen, height,width):
        self.url = "https://api.coindesk.com/v1/bpi/currentprice.json" 

        self.Tile = self.createTile(screen, height, width)
        self.fetch_data()
       # self.detailView = self.createDetailView()
        super(CryptoAPI,self).__init__(screen, height,width)

    # defines the tile layout
    def createTile(self,screen, height,width):
        tile = Frame(screen, height,width, title="CryptoAPI", can_scroll=False, reduce_cpu=True)
        if not "btc" in tile.data:
            tile.data = {"btc":""}
        layout = Layout([1])
        tile.add_layout(layout)
        layout.add_widget(Label("Bitcoin", align="^"))
        layout.add_widget(Label("", align="^"))
        layout.add_widget(Text("Dollar: ",name="dollar", readonly=True))
        layout.add_widget(Text("Euro: ",name="euro", readonly=True))
        layout.add_widget(Label("", align="^"))
        layout.add_widget(Label("", align="^"))
        layout.add_widget(Text("Timestamp: ",name="time", readonly=True))
        buttonBar = Layout([1, 1,1])
        tile.add_layout(buttonBar)
        layout.add_widget(Label("", align="^"))
        layout.add_widget(Label("", align="^"))
        buttonBar.add_widget(Button('Update!', self.fetch_data, None), 1)
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
            "dollar":json_data["bpi"]["USD"]["rate"]
            ,"euro":json_data["bpi"]["EUR"]["rate"]
            ,"time":json_data["time"]["updated"]
        }
        self.Tile.save()
        self.Tile.reset()

        
