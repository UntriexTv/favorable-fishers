from asciimatics.widgets import Frame, ListBox, Layout, Divider, Text, \
    Button, TextBox, Widget
from asciimatics.scene import Scene
from asciimatics.screen import Screen
from asciimatics.exceptions import ResizeScreenError, NextScene, StopApplication
import sys

class testView(Frame):
    def __init__(self, screen,x1,x2):
        super(testView, self).__init__(screen,
                                          15,
                                          50,
                                          hover_focus=True,
                                          can_scroll=False,
                                          title="Contact Details",
                                          reduce_cpu=True,
                                          x=50*x1,
                                          y=15*x2, 
                                          )

      #  self.palette = {"attribute":(1,2,3)}
        # Create the form for displaying the list of contacts.
        layout = Layout([100], fill_frame=True)
        self.add_layout(layout)
        layout.add_widget(Text("Name:", "name"))
        layout.add_widget(Text("Address:", "address"))
        layout.add_widget(Text("Phone number:", "phone"))
        layout.add_widget(Text("Email address:", "email"))
        layout2 = Layout([1, 1, 1, 1])
        self.add_layout(layout2)
        self.fix()








def demo(screen, scene):
    scenes = [
        Scene([testView(screen,0,0),testView(screen,1,1),testView(screen,2,0),testView(screen,3,1)
        ,testView(screen,0,2),testView(screen,2,2)],   -1, name="Main"),
        
    ]

    screen.play(scenes, stop_on_resize=True, start_scene=scenes[0], allow_int=True)



last_scene = None
while True:
    try:
        Screen.wrapper(demo, catch_interrupt=True, arguments=[last_scene])
        sys.exit(0)
    except ResizeScreenError as e:
        last_scene = e.scene






