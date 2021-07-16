import time

from asciimatics.widgets import Frame, ListBox, Layout, Divider, Text, \
    Button, TextBox, Widget, Label
from asciimatics.scene import Scene
import threading
import requests
from asciimatics.screen import Screen
from asciimatics.exceptions import ResizeScreenError, NextScene, StopApplication
import sys


class Data:
    def __init__(self):
        self.data = {}  # saved data
        self.update = []  # list of {"api": x, "data": y}

    def save_data(self, data_place, data):
        self.data[data_place] = data

    def new_update(self, data_: str, api: str):
        if data_ in self.data:
            for x in self.update:
                if x["data"] == data_:
                    x["api"] = api
                    break
        else:
            self.data[data_] = "loading..."
            self.update.append({"api": api, "data": data_})

    def update_loop(self):  # is running on background and downloading data from provided api
        while True:
            for req in self.update:
                self.data[req["data"]] = req["api"]()
                time.sleep(0.5)

    def get_data(self, data_: str):
        try:
            return self.data[data_]
        except KeyError:
            return ""


class testView(Frame):
    def __init__(self, screen, height, width, data_api, x1=0, y1=0):
        super(testView, self).__init__(screen,
                                       height,
                                       width,
                                       hover_focus=True,
                                       can_scroll=False,
                                       title="Contact Details",
                                       reduce_cpu=True,
                                       x=width * x1,
                                       y=height * y1
                                       )

        #  self.palette = {"attribute":(1,2,3)}
        # Create the form for displaying the list of contacts.
        self.layout = Layout([100], fill_frame=True)
        self.data_api = data_api
        data_api.new_update("first", lambda: requests.request("GET", "https://www.boredapi.com/api/activity"))
        data_api.new_update("second", lambda: requests.request("GET", "https://www.boredapi.com/api/activity"))
        self.data["api"] = "loading"
        self.data["apiapi"] = "loading"
        self.add_layout(self.layout)
        self.layout.add_widget(Text("Email address:", "apiapi", readonly=True))
        self.layout.add_widget(Text("Api test", "api", readonly=True))
        layout2 = Layout([1, 1, 1, 1, 1])
        self.add_layout(layout2)
        layout2.add_widget(Button("Quit", self._quit, None), 0)
        layout2.add_widget(Button("Quit", self._quit, None), 1)
        layout2.add_widget(Button("Quit", self._quit, None), 2)
        layout2.add_widget(Button("Quit", self._quit, None), 3)
        layout2.add_widget(Button("Quit", self._quit, None), 4)
        self.fix()

    def _update(self, frame_no):
        super(testView, self)._update(frame_no)

    @staticmethod
    def _quit():
        raise StopApplication("User pressed quit")

    def updating(self):
        # self.data_api.update_s()
        try:
            # self.data["api"] = self.data_api.get_data("first").json()["activity"]
            self.data["api"] = str(self.data_api.data)
            self.data["apiapi"] = self.data_api.get_data("second").json()["activity"]
        except:
            # self.data["api"] = "loading"
            self.data["api"] = str(self.data_api.data)
            self.data["apiapi"] = "loading"
        self.layout.reset()

    @property
    def frame_update_count(self):
        self.updating()
        # Refresh once every 2 seconds by default.
        return 40


cmd = Data()
t1 = threading.Thread(target=cmd.update_loop, daemon=True)
t1.start()


def demo(screen, scene):
    # =================
    # for dashboard with multiple tile-frames
    # set frame size
    # height = 15
    # width = 50
    # scenes = [

    #    Scene([testView(screen,height,width,0,0),testView(screen,height,width,1,1),testView(screen,height,width,2,0),testView(screen,height,width,3,1)
    # ,testView(screen,0,2),testView(screen,2,2)
    #         ] ,   -1, name="Main"),

    # ]

    # ================
    # for detailView
    cmd.__init__()
    height = screen.height // 2
    width = screen.width // 2
    scenes = [Scene([testView(screen, height, width, cmd)], -1, name="Main"), ]

    screen.play(scenes, stop_on_resize=True, start_scene=scenes[0], allow_int=True)


last_scene = None
while True:
    try:
        Screen.wrapper(demo, catch_interrupt=True, arguments=[last_scene])
        sys.exit(0)
    except ResizeScreenError as e:
        last_scene = e.scene
