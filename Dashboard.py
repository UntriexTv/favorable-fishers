
from asciimatics.scene import Scene

from asciimatics.widgets import Frame, ListBox, Layout, Divider, Text, \
    Button, TextBox, Widget, Label

class Dashboard(Scene):
    def __init__(self, screen):
        self.screen = screen
        dash = self.generateDashboard()
        
        super(Dashboard,self).__init__(dash, name="dashboard")

    def generateDashboard(self):
        #mainFrame = Frame(self.screen,width=1920, height=1080)
        mainFrame = Frame(self.screen,width=800//2, height=600//2, x=0, y=0)
        layout = Layout([1])
        mainFrame.add_layout(layout)
        layout.add_widget(Label("one"))
        mainFrame.fix()
        
        mainFrame2 = Frame(self.screen,width=800//2, height=600//2, x=50, y=0)
        layout = Layout([1])
        mainFrame2.add_layout(layout)
        layout.add_widget(Label("two"))
        mainFrame2.fix()


        return [mainFrame, mainFrame2]