from asciimatics.widgets import Frame, ListBox, Layout, Divider, Text, \
    Button, TextBox, Widget, Label
from asciimatics.scene import Scene
import requests
from asciimatics.screen import Screen
from asciimatics.exceptions import ResizeScreenError, NextScene, StopApplication
import sys


class Commands():
    def __init__(self):
        self.commands = {"commands": "", "result": ""}

    def addCommand(self, cmd):
        if cmd == "b":
            self.commands["commands"] = self.commands["commands"][:-1]
        elif cmd =="c":
            self.commands["commands"] = ""
        else:
            self.commands["commands"] += cmd

    def getCommands(self):
        try:
            exec(f"""self.commands["result"] = str({self.commands["commands"]})""")
        except:
            self.commands["result"] = ""
        return self.commands


class calculatorView(Frame):
    def __init__(self, screen, height, width, comm, x1=0, y1=0):
        super(calculatorView, self).__init__(screen,
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
        layout_result = Layout([2])
        self.add_layout(layout_result)
        layout_result.add_widget(Text("Command: ", name="commands", validator=self.validateCommand))
        layout_result.add_widget(Text("Result: ", name="result", readonly=True))

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
            self.cmd.commands["commands"] = data
        if data:
            self.reset()
        return True

    def _update(self, frame_no):
        super(calculatorView, self)._update(frame_no)

    def reset(self):
        self.data = self.cmd.getCommands()

    def calculator(self, new=None):
        self.cmd.addCommand(new)
        self.reset()

    @staticmethod
    def _quit():
        raise StopApplication("User pressed quit")