from asciimatics.widgets import Frame
import  APImanager 
import json

class APIWidget():
    # self.tile = Frame()
    # self.detailView = Frame()
    # self.data = json

    def __init__(self, api):
        self.height = 15
        self.width = 50
        self.data = APImanager.callAPI("test")


    def getTile(self) -> Frame:
        return self.Tile

    def getDetailView(self) -> Frame:
        pass

    def refreshData(self):
        self.data = APImanager.callAPI("test")
        #update view
        pass

    def setAPIparameters(self):
        pass

    def move(self,x,y):
        self.Tile._canvas._dx = x
        self.Tile._canvas._dy = y