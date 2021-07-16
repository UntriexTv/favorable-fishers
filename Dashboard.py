
from testwid import testView
from APIWidgets.BoredAPI import BoredAPI
from asciimatics.effects import Background
from asciimatics.exceptions import StopApplication
from asciimatics.scene import Scene

from asciimatics.widgets import Frame, ListBox, Layout, Divider, Text, \
    Button, TextBox, Widget, Label


TILE_WIDTH = 50
TILE_HEIGHT = 15
TOOLBAR_OFFSET = 3

class Dashboard(Scene):
    def __init__(self, screen, widgetman):
        self.screen = screen
        self.widgetmanager = widgetman
        menu = self.generateInterface()
        super(Dashboard,self).__init__(menu, name="dashboard")

        # after resize / reload: place widget on current screen
        if len(self.widgetmanager.widgets) > 0:
            self.widgetmanager.update_screen(screen)
            self.displayDashboard()


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


    @staticmethod
    def _quit():
        raise StopApplication("User pressed quit")

    # get and place all tiles on dashboard
    def displayDashboard(self):
        allTiles = self.widgetmanager.getDashboard()
        for index, widget in enumerate(allTiles):
            self.placeTile( widget, index)


    # adds tile to scene, with x/y offset, so it gets drawn
    def placeTile(self, tile, tileIndex):
        tilesPerRow = self.screen.width // TILE_WIDTH
        remaining_space = self.screen.width % TILE_WIDTH
        padding = (remaining_space // (tilesPerRow+1))
        x_pos = tileIndex % tilesPerRow
        y_pos = tileIndex // tilesPerRow
        tile._canvas._dx = x_pos * TILE_WIDTH + (padding * (x_pos+1))# + middeling //2
        tile._canvas._dy = ( y_pos * TILE_HEIGHT ) + TOOLBAR_OFFSET + (y_pos+1)
        self.add_effect(tile)


    # close widget menu
    def _cancel(self):
        self.remove_effect(self.effects[-1])


    # removes widget menu, adds new widget to manager
    def _on_select(self):
        self._cancel()
        self.menuFrame.save()
        widgetID = self.menuFrame.data["WidgetList"]
        newtileIndex = self.widgetmanager.addAPIWidget(widgetID, self.screen)
        tile = self.widgetmanager.getTile(newtileIndex)
        self.placeTile(tile, newtileIndex)


    # create menu
    def generateInterface(self):
        interface = Frame(self.screen, TOOLBAR_OFFSET,self.screen.width,x=0,y=0)
        layout = Layout([1,1])
        interface.add_layout(layout)
        layout.add_widget(Button("Add Widget",self._add_widget,None),0)
        layout.add_widget(Button("Quit",self._quit,None),1)
        interface.fix()

        return [Background(self.screen),interface]
