from asciimatics.widgets import Frame
import  APImanager 
import json

class AIPWidget():
    # self.tile = Frame()
    # self.detailView = Frame()
    # self.data = json

    def __init__(self, api):
        
        self.data = APImanager.callAPI("test")


    def getTile(self) -> Frame:
        pass

    def getDetailView(self) -> Frame:
        pass

    def refreshData(self):
        self.data = APImanager.callAPI("test")
        #update view
        pass

    def setAPIparameters(self):
        pass