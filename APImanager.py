import requests
import json

# class APImanager():
    # class that handles calling api's and returns json

class Data:
    def __init__(self):
        self.data = {}  # saved data
        self.update = []  # list of {"api": x, "data": y}

    def save_data(self, data_place, data):
        self.data[data_place] = data

    def new_update(self, data_: str, api: str):
        self.data[data_] = "test"
        self.update.append({"api": api, "data": data_})

    def update_loop(self):  # is running in the background and downloading data from provided api
        while True:
            for req in self.update:
                self.data[req["data"]] = requests.request("GET", req["api"])
            time.sleep(0.5)

    def get_data(self, data_: str):
        try:
            return self.data[data_]
        except KeyError:
            return ""