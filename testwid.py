from os import write
from asciimatics.renderers import Box
from asciimatics.effects import Background, Clock, Cog, Print
from asciimatics.widgets import Frame, ListBox, Layout, Divider, Text, \
    Button, TextBox, Widget
from asciimatics.scene import Scene
from asciimatics.screen import Canvas, Screen
from asciimatics.exceptions import ResizeScreenError, NextScene, StopApplication
import sys

# class testView(Frame):
#     def __init__(self, screen,height,width,x1=0,y1=0):
#         super(testView, self).__init__(screen,
#                                           height,
#                                           width,
#                                           hover_focus=True,
#                                           can_scroll=False,
#                                           title="Contact Details",
#                                           reduce_cpu=True,
#                                           x=width*x1,
#                                           y=height*y1
#                                           )
#         self.canvas_base = (screen,height,width)
#       #  self.palette = {"attribute":(1,2,3)}
#         # Create the form for displaying the list of contacts.
#         layout = Layout([100], fill_frame=True)
#         self.add_layout(layout)
#         layout.add_widget(Text("Naqme:", "name"))
#         layout.add_widget(Text("Address:", "address"))
#         layout.add_widget(Text("Phone number:", "phone"))
#         layout.add_widget(Text("Email address:", "email"))
#         layout2 = Layout([1, 1, 1, 1, 1])
#         self.add_layout(layout2)
#         layout2.add_widget(Button("Quit", self._quit, None), 3)
#         self.fix()

#     @staticmethod
#     def _quit():
#         raise StopApplication("User pressed quit")

#     def move(self,x,y):
#         #pass
#         self._canvas._dx = x
#         self._canvas._dy = y


# import json

# y = {"a":"1","b":"2","c":"3"}
# jsony = json.dumps(y)
# print(jsony["a"])
# x = {"q":jsony}

# print(x["q"])


w = [0,1,2,3]

with open('widgets.csv', 'w' ) as writer:
    for x in w:
        writer.writelines(str(x))


with open('widgets.csv', 'r' ) as reader:
    x = reader.readlines()
print(x)
