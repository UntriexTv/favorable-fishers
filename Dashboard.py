
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


    # create widget menu
    def _add_widget(self):

        self._widget_list_view = ListBox(
            Widget.FILL_FRAME,
            self.widgetmanager.getWidgetMenu(),
            name="WidgetList",
            add_scroll_bar=True,
            on_select=self._on_select)#_addAPIWidget)

        self.menuFrame = Frame(self.screen,10,20)
        layout = Layout([1], fill_frame=True)
        self.menuFrame.add_layout(layout)
        layout.add_widget(self._widget_list_view)
        layout.add_widget(Divider())
        self.open_menu(self.menuFrame)

    #open menu
    def open_menu(self, menu:Frame):
        closeMenuBtn = Layout([1])
        menu.add_layout(closeMenuBtn)
        closeMenuBtn.add_widget(Button("Cancel", self._cancel,None))
        menu.fix()

        self.add_effect(menu)


    @staticmethod
    def _quit():
        raise StopApplication("User pressed quit")

    def _save_setup(self):
        try:
            widget_ids = self.widgetmanager.get_widget_ids()
            with open('widget_dashboard.csv', 'w' ) as writer:
                writer.writelines([str(id)+'\n' for id in widget_ids])
        except:
            pass

    def _load_setup(self):
        try:
            widget_ids = []
            with open('widget_dashboard.csv', 'r' ) as reader:
                widget_ids = reader.read().splitlines()
            for type in widget_ids:
                newtileIndex = self.widgetmanager.addAPIWidget(int(type), self.screen, TILE_HEIGHT, TILE_WIDTH)
                tile = self.widgetmanager.getTile(newtileIndex)
                self.placeTile(tile, newtileIndex)
        except:
        # if it does not exist, do nothing
            pass


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
        tile._canvas._dx = x_pos * TILE_WIDTH + (padding * (x_pos+1))
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
        newtileIndex = self.widgetmanager.addAPIWidget(widgetID, self.screen, TILE_HEIGHT, TILE_WIDTH)
        if newtileIndex is not None:
            tile = self.widgetmanager.getTile(newtileIndex)
            self.placeTile(tile, newtileIndex)


    # create menu
    def generateInterface(self):
        interface = Frame(self.screen, TOOLBAR_OFFSET,self.screen.width,x=0,y=0)
        layout = Layout([1,1,1,1])
        interface.add_layout(layout)
        layout.add_widget(Button("Add Widget",self._add_widget,None),0)
        layout.add_widget(Button("Save Layout",self._save_setup,None),1)
        layout.add_widget(Button("Load Layout",self._load_setup,None),2)
        layout.add_widget(Button("Quit",self._quit,None),3)
        interface.fix()

        return [Background(self.screen),interface]
