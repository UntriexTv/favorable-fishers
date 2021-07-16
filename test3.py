import threading
import time

from asciimatics.widgets import Frame, ListBox, Layout, Divider, Text, \
    Button, TextBox, Widget, Label
from asciimatics.scene import Scene
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
    def __init__(self, screen, height, width, comm, x1=0, y1=0):
        super(testView, self).__init__(screen,
                                       height,
                                       width,
                                       hover_focus=True,
                                       can_scroll=False,
                                       title="Calculator",
                                       reduce_cpu=False,
                                       x=width * x1,
                                       y=height * y1
                                       )
        # self.draw()
        self.cmd = comm
        #     self.calculator(5)

        #  def draw(self):
        #  self.palette = {"attribute":(1,2,3)}
        # Create the form for displaying the list of contacts.
        self.cmd.save_data("commands", "")
        self.layout_result = Layout([2])
        self.add_layout(self.layout_result)
        self.layout_result.add_widget(Text("Command: ", name="commands", validator=self.validateCommand))
        self.layout_result.add_widget(Text("Result: ", name="result", readonly=True))

        layout = Layout([5, 5, 5, 5], fill_frame=True)
        self.add_layout(layout)
        layout.add_widget(Button(" ( ", self.calculator, "("), 0)
        layout.add_widget(Button(" ) ", self.calculator, ")"), 1)
        layout.add_widget(Button("DEL", self.calculator, "b"), 2)
        layout.add_widget(Button(" C ", self.calculator, "c"), 3)
        layout.add_widget(Button(" 7 ", self.calculator, "7"), 0)
        layout.add_widget(Button(" 8 ", self.calculator, "8"), 1)
        layout.add_widget(Button(" 9 ", self.calculator, "9"), 2)
        layout.add_widget(Button(" / ", self.calculator, "/"), 3)
        layout.add_widget(Button(" 4 ", self.calculator, "4"), 0)
        layout.add_widget(Button(" 5 ", self.calculator, "5"), 1)
        layout.add_widget(Button(" 6 ", self.calculator, "6"), 2)
        layout.add_widget(Button(" * ", self.calculator, "*"), 3)
        layout.add_widget(Button(" 1 ", self.calculator, "1"), 0)
        layout.add_widget(Button(" 2 ", self.calculator, "2"), 1)
        layout.add_widget(Button(" 3 ", self.calculator, "3"), 2)
        layout.add_widget(Button(" - ", self.calculator, "-"), 3)
        layout.add_widget(Button(" 0 ", self.calculator, "0"), 1)
        layout.add_widget(Button(" . ", self.calculator, "."), 2)
        layout.add_widget(Button(" + ", self.calculator, "+"), 3)
        layout2 = Layout([1, 1, 1, 1, 1])
        self.add_layout(layout2)
        layout2.add_widget(Button("Quit", self._quit, None), 3)
        self.fix()

    def validateCommand(self, data):
        test = ''.join("" if c.isdigit() or c in ["/", "*", "-", "+", ".", "(", ")"] else c for c in data)
        if not test:
            self.cmd.data["commands"] = data
        else:
            return False
        if data:
            self.reset()
        return True

    def _update(self, frame_no):
        super(testView, self)._update(frame_no)

    def reset(self):
        self.data = {"commands": self.cmd.get_data("commands")}
        try:
            exec(f"""self.data["result"] = str({self.data["commands"]})""")
        except:
            self.data["result"] = ""

    def calculator(self, new=None):
        if new == "b":
            self.data["commands"] = self.data["commands"][:-1]
        elif new =="c":
            self.data["commands"] = ""
        else:
            self.data["commands"] += new
        try:
            self.cmd.save_data("commands", self.data["commands"])
        except KeyError:
            self.cmd.save_data("commands", new)
        self.reset()

    @staticmethod
    def _quit():
        raise StopApplication("User pressed quit")


cmd = Data()
t1 = threading.Thread(target=cmd.update_loop, daemon=True)
t1.start()


def demo(screen, scene):
    height = screen.height  # // 2
    width = screen.width  # // 2
    cmd.__init__()
    scenes = [Scene([testView(screen, height, width, cmd)], -1, name="Main"), ]

    screen.play(scenes, stop_on_resize=True, start_scene=scenes[0], allow_int=True)


last_scene = None
while True:
    try:
        Screen.wrapper(demo, catch_interrupt=True, arguments=[last_scene])
        sys.exit(0)
    except ResizeScreenError as e:
        last_scene = e.scene