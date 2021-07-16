import requests
import json

class testAPI(object):
    def __init__(self,_title):
        self.url = "https://www.boredapi.com/api/activity" 
        self.title = _title#"BoredAPI"

    def apiCall(self):
        response = requests.request("GET",self.url)
        #print(response.json())
        #print(response.json()["activity"])
        return response.json()["activity"]
 