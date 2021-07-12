import requests
import json
from asciimatics.widgets import Frame, ListBox, Layout, Divider, Text, \
    Button, TextBox, Widget, Label

class BoredAPI(Frame):
    def __init__(self,_title):
        self.url = "https://www.boredapi.com/api/activity" 
        self.title = _title#"BoredAPI"
        self.apiData = self.apiCall()
        self.createLayout()
        self.createFrame()

    def createLayout(self):
        self.layout = [
        
        
        
        ]

    def apiCall(self):
        response = requests.request("GET",self.url)
        #print(response.json())
        #print(response.json()["activity"])
        return response.json()#["activity"]
