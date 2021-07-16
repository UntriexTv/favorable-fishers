from asciimatics.widgets import Frame, ListBox, Layout, Divider, Text, \
    Button, TextBox, Widget, Label
from asciimatics.scene import Scene
import requests
from asciimatics.screen import Screen
from asciimatics.exceptions import ResizeScreenError, NextScene, StopApplication
import sys


class testView(Frame):
    def __init__(self, screen, height, width, x1=0, y1=0):
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
        self.layout_result = Layout([2])
        self.add_layout(self.layout_result)
        try:
            self.layout_result.add_widget(Label(self.data["commands"]))
            self.layout_result.add_widget(Label(self.data["result"]))
        except:
            self.layout_result.add_widget(Label("11"))
            self.layout_result.add_widget(Label(""))
        layout = Layout([4, 4, 4, 4], fill_frame=True)
        self.add_layout(layout)
        layout.add_widget(Button("7", self.calculator, "7"), 0)
        layout.add_widget(Button("8", self.calculator, "8"), 1)
        layout.add_widget(Button("9", self.calculator, "9"), 2)
        layout.add_widget(Button("/", self.calculator, "/"), 3)
        layout.add_widget(Button("4", self.calculator, "4"), 0)
        layout.add_widget(Button("5", self.calculator, "5"), 1)
        layout.add_widget(Button("6", self.calculator, "6"), 2)
        layout.add_widget(Button("*", self.calculator, "*"), 3)
        layout.add_widget(Button("1", self.calculator, "1"), 0)
        layout.add_widget(Button("2", self.calculator, "2"), 1)
        layout.add_widget(Button("3", self.calculator, "3"), 2)
        layout.add_widget(Button("-", self.calculator, "-"), 3)
        layout.add_widget(Button("0", self.calculator, "0"), 1)
        layout.add_widget(Button(".", self.calculator, "."), 2)
        layout.add_widget(Button("+", self.calculator, "+"), 3)
        layout2 = Layout([1, 1, 1, 1, 1])
        self.add_layout(layout2)
        layout2.add_widget(Button("Quit", self._quit, None), 3)
        self.fix()

    def _update(self, frame_no):
        super(testView, self)._update(frame_no)

    def calculator(self, new):
        try:
            self.data["commands"] += str(new)
        except:
            self.data["commands"] = str(new)
        try:
            exec(f"""self.data["result"] = {self.data["commands"]}""")
        except:
            self.data["result"] = "Error"
        self.layout_result.update(2)
        print(self.data)

    @staticmethod
    def _quit():
        raise StopApplication("User pressed quit")


def demo(screen):
    height = screen.height  # // 2
    width = screen.width  # // 2
    scenes = [Scene([testView(screen, height, width)], -1, name="Main"), ]

    screen.play(scenes, stop_on_resize=True, start_scene=scenes[0], allow_int=True)


last_scene = None
while True:
    try:
        Screen.wrapper(demo, catch_interrupt=True)
        sys.exit(0)
    except ResizeScreenError as e:
        last_scene = e.scene
