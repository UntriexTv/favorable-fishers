from asciimatics.renderers import Box
from asciimatics.effects import Background, Clock, Cog, Print
from asciimatics.widgets import Frame, ListBox, Layout, Divider, Text, \
    Button, TextBox, Widget
from asciimatics.scene import Scene
from asciimatics.screen import Canvas, Screen
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
        self.canvas_base = (screen,height,width)
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

    def move(self,x,y):
        #pass
        self._canvas._dx = x
        self._canvas._dy = y




def demo(screen, scene):

    
    # #=================
    # # for dashboard with multiple tile-frames
    # # set frame size
    height = 15
    width = 50
    fr1 = testView(screen,height,width)
    fr2 = testView(screen,height,width)
    fr2.move(20,20)
    x=  Scene([fr1
        #,testView(screen,0,2),testView(screen,2,2)
             ] ,   -1, name="Main")
        
    x.add_effect(fr2)

    fr3 = testView(screen,height,width)
    fr4 = testView(screen,height,width)
    fr5 = testView(screen,height,width)



    widgetTiles = [fr1,fr3,fr4,fr5]



    tilesPerRow = screen.width // 50
    for index, widget in enumerate(widgetTiles):
        widget.move(  (index%tilesPerRow ) * 50,    (index // tilesPerRow) *15   )
        x.add_effect(widget)

    #================
    # for detailView
    # height = screen.height // 2
    # width = screen.width // 2
    #  scenes = [
    #     Scene([testView(screen,height,width)
    #          ] ,   -1, name="Main"),
        
    # ]

    #screen.play(scenes, stop_on_resize=True, start_scene=scenes[0], allow_int=True)

   # fr = Frame(screen,20,20,x=0,y=0 )


    #screen.play([Scene([Background(screen, 1), Print(screen,Box(10,10),3)])])
    screen.play([x])


last_scene = None
while True:
    try:
        Screen.wrapper(demo, catch_interrupt=True, arguments=[last_scene])
        sys.exit(0)
    except ResizeScreenError as e:
        last_scene = e.scene






