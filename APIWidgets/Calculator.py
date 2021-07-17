from APIWidgets.APIWidget import APIWidget
from asciimatics.widgets import Frame, ListBox, Layout, Divider, Text, \
    Button, TextBox, Widget, Label
from asciimatics.scene import Scene
import requests
from asciimatics.screen import Screen
from asciimatics.exceptions import ResizeScreenError, NextScene, StopApplication
import sys

"""
helper class to persist data
"""
class Data:
    def __init__(self):
        self.data = {}  # saved data
        self.update = []  # list of {"api": x, "data": y}

    def save_data(self, data_place, data):
        self.data[data_place] = data

    def get_data(self, data_: str):
        try:
            return self.data[data_]
        except KeyError:
            return ""

class calculator(APIWidget):
    def __init__(self, screen, height,width):
        self.cmd = Data()
        self.Tile = self.createTile(screen, height, width)
        self.id = 4
        super(calculator,self).__init__(screen, height,width)

    def createTile(self, screen, height, width):
        tile = Frame(screen,
                                       height,
                                       width,
                                       hover_focus=True,
                                       can_scroll=False,
                                       title="Calculator",
                                       reduce_cpu=True,
                                       )
        

        # Create the form for displaying the list of contacts.
        self.cmd.save_data("commands", "")
        tile.data = {"commands": self.cmd.get_data("commands")}
        self.layout_result = Layout([2])
        tile.add_layout(self.layout_result)
        self.layout_result.add_widget(Text("Command: ", name="commands", validator=self.validateCommand))
        self.layout_result.add_widget(Text("Result: ", name="result", readonly=True))
        
        layout = Layout([5, 5, 5, 5], fill_frame=True)
        tile.add_layout(layout)
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
        tile.fix()
        return tile

    def validateCommand(self, data):
        test = ''.join("" if c.isdigit() or c in ["/", "*", "-", "+", ".", "(", ")"] else c for c in data)
        if not test:
            self.cmd.data["commands"] = data
        else:
            return False
        if data:
            self.checkResult()
        return True

    def checkResult(self):
        self.Tile.data = {"commands": self.cmd.get_data("commands")}
        try:
            exec(f"""self.data["result"] = str({self.Tile.data["commands"]})""")
        except:
            self.Tile.data["result"] = ""

    def calculator(self, new=None):
        if not "commands" in self.Tile.data:
            self.Tile.data = {"commands":""}
        if new == "b":
            self.Tile.data["commands"] = self.Tile.data["commands"][:-1]
        elif new =="c":
            self.Tile.data["commands"] = ""
        else:
            self.Tile.data["commands"] += new
        try:
            self.cmd.save_data("commands", self.Tile.data["commands"])
        except KeyError:
            self.cmd.save_data("commands", new)
        self.Tile.save()
        self.Tile.reset()