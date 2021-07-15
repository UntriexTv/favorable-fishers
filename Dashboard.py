
from testwid import testView
from APIWidgets.BoredAPI import BoredAPI
from asciimatics.effects import Background
from asciimatics.exceptions import StopApplication
from asciimatics.scene import Scene

from asciimatics.widgets import Frame, ListBox, Layout, Divider, Text, \
    Button, TextBox, Widget, Label


TILE_WIDTH = 50
TILE_HEIGHT = 15

class Dashboard(Scene):
    def __init__(self, screen, widgetman):
        self.screen = screen
        self.widgetmanager = widgetman
      #  dash = self.generateDashboard()
        self.newtile = []
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
        
        self.menuFrame = Frame(self.screen,20,20)
        layout = Layout([1], fill_frame=True)
        self.menuFrame.add_layout(layout)
        layout.add_widget(self._widget_list_view)
        layout.add_widget(Divider())

        closeMenuBtn = Layout([1])
        self.menuFrame.add_layout(closeMenuBtn)
        closeMenuBtn.add_widget(Button("Cancel", self._cancel,None))
        self.menuFrame.fix()

        self.add_effect(self.menuFrame)

        self.displayDashboard()
        pass

    @staticmethod
    def _quit():
        raise StopApplication("User pressed quit")


    def displayDashboard(self):
        #get all tiles
        self.widgetTiles = self.widgetmanager.getDashboard()

        tilesPerRow = self.screen.width // TILE_WIDTH
        for index, widget in enumerate(self.widgetTiles):
            widget.move(  (index%tilesPerRow ) * TILE_WIDTH,    (index // tilesPerRow) *TILE_HEIGHT   )
            self.add_effect(widget)

    def placeTile(self, tile, x_offset, y_offset):
        #tile._canvas.move(x_offset,y_offset)
        tile._canvas._dx = x_offset
        tile._canvas._dy = y_offset
        self.add_effect(tile)
        

    # close widget menu
    def _cancel(self):
        self.remove_effect(self.effects[-1])

#for widget in self.widgetTiles:

    def _on_select(self):
        # pass
        self.remove_effect(self.effects[-1])
        self.menuFrame.save()
        widgetID = self.menuFrame.data["WidgetList"]


        # q =  testView(self.screen,15,50)
        # self.newtile.append(q )

        # newtileIndex = len(self.effects)-1
        
        # tilesPerRow = self.screen.width // TILE_WIDTH
        # x_off = newtileIndex%tilesPerRow
        # y_off = newtileIndex//tilesPerRow
        
        # self.placeTile(q,x_off*50, y_off*15)#, x_off*50, y_off*15)

        # first a test instance
        newtileIndex = self.widgetmanager.addAPIWidget(widgetID, self.screen)
       
        
        tilesPerRow = self.screen.width // TILE_WIDTH
        # x_off = newtileIndex%tilesPerRow
        # y_off = newtileIndex//tilesPerRow

        t = self.widgetmanager.getTile(self.screen)
        
        self.placeTile(t, 1*50, 0*15)

        # self.placeTile(self.widgetmanager.getTile(newtileIndex-1), x_off*50, y_off*15)


    def generateInterface(self):
        # basic interface
        interface = Frame(self.screen, 35,50,x=0,y=0)
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