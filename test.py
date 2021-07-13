from asciimatics.widgets import Frame, ListBox, Layout, Divider, Text, \
    Button, TextBox, Widget
from asciimatics.scene import Scene
from asciimatics.screen import Screen
from asciimatics.exceptions import ResizeScreenError, NextScene, StopApplication
import sys

class testView(Frame):
    def __init__(self, screen,height,width,x1=0,y1=0):
        super(testView, self).__init__(screen,
                                          height,
                                          width,
                                          hover_focus=True,
                                          can_scroll=False,
                                          title="Contact Details",
                                          reduce_cpu=True,
                                          x=width*x1,
                                          y=height*y1
                                          )

      #  self.palette = {"attribute":(1,2,3)}
        # Create the form for displaying the list of contacts.
        layout = Layout([100], fill_frame=True)
        self.add_layout(layout)
        layout.add_widget(Text("Name:", "name"))
        layout.add_widget(Text("Address:", "address"))
        layout.add_widget(Text("Phone number:", "phone"))
        layout.add_widget(Text("Email address:", "email"))
        layout2 = Layout([1, 1, 1, 1, 1])
        self.add_layout(layout2)
        layout2.add_widget(Button("Quit", self._quit, None), 3)
        self.fix()

    @staticmethod
    def _quit():
        raise StopApplication("User pressed quit")




def demo(screen, scene):

    
    #=================
    # for dashboard with multiple tile-frames
    # set frame size
    height = 15
    width = 50
    scenes = [
        
        Scene([testView(screen,height,width,0,0),testView(screen,height,width,1,1),testView(screen,height,width,2,0),testView(screen,height,width,3,1)
        #,testView(screen,0,2),testView(screen,2,2)
             ] ,   -1, name="Main"),
        
    ]

    #================
    # for detailView
    # height = screen.height // 2
    # width = screen.width // 2
    #  scenes = [
    #     Scene([testView(screen,height,width)
    #          ] ,   -1, name="Main"),
        
    # ]

    screen.play(scenes, stop_on_resize=True, start_scene=scenes[0], allow_int=True)



last_scene = None
while True:
    try:
        Screen.wrapper(demo, catch_interrupt=True, arguments=[last_scene])
        sys.exit(0)
    except ResizeScreenError as e:
        last_scene = e.scene






