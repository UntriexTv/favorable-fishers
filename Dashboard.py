
from asciimatics.effects import Background
from asciimatics.exceptions import StopApplication
from asciimatics.scene import Scene

from asciimatics.widgets import Frame, ListBox, Layout, Divider, Text, \
    Button, TextBox, Widget, Label

class Dashboard(Scene):
    def __init__(self, screen, widgetman):
        self.screen = screen
        self.widgetmanager = widgetman
      #  dash = self.generateDashboard()

        super(Dashboard,self).__init__(self.generateInterface(), name="dashboard")

    # def addTile(self,tileFrame):
    #     self.tiles.append(tileFrame)


    # open widget menu
    def _add_widget(self):

        self._widget_list_view = ListBox(
            Widget.FILL_FRAME,
            self.widgetmanager.getWidgetMenu(),
            name="WidgetList",
            add_scroll_bar=True,
          #  on_change=self._on_pick,
            on_select=self._on_select)#_addAPIWidget)
        
        menuFrame = Frame(self.screen,20,20)


        
        layout = Layout([1], fill_frame=True)
        menuFrame.add_layout(layout)
        layout.add_widget(self._widget_list_view)
        layout.add_widget(Divider())

        closeMenuBtn = Layout([1])
        menuFrame.add_layout(closeMenuBtn)
        closeMenuBtn.add_widget(Button("Cancel", self._cancel,None))

        
  

        menuFrame.fix()

        self.add_effect(menuFrame)
        pass

    @staticmethod
    def _quit():
        raise StopApplication("User pressed quit")


    def displayDashboard(self):
        #get all tiles
        widgetTiles = self.widgetmanager.getActiveTiles()

    def _cancel(self):
        self.remove_effect()

    # close widget menu
    def remove_effect(self):
        #super().remove_effect(super().effects[-1])
        self.remove_effect(self.effects[-1])

    def _on_select(self):
        widgetID = self.data["WidgetList"]
        self.widgetmanager.addAPIWidget(widgetID, self.screen)

    def generateInterface(self):
        # basic interface
        interface = Frame(self.screen, 3,50,x=0,y=0)
        layout = Layout([1,1])
        interface.add_layout(layout)
        layout.add_widget(Button("Add Widget",self._add_widget,None),0)
        layout.add_widget(Button("Quit",self._quit,None),1)
        interface.fix()

        return [Background(self.screen),interface] 



    #TMP
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