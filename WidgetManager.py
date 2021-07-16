


from APIWidgets.BoredAPI import BoredAPI
from APIWidgets.CovidAPI import covidView
from testwid import testView


class WidgetManager:
    def __init__(self):
        self.widgets = []
        self.widgetList = [("Bored",0),("Covid",1),("Weather",2)]

    def getDetailView(self):
        pass

    def getTile(self,id):
        #return self.widgets[id].Tile
        # return self.widgets[id]
       # raise ValueError("het is" + str(self.widgets[0].Tile))
        return self.widgets[id].Tile

    def update_screen(self, screen):
        for widget in self.widgets:
            widget.Tile._canvas._screen = screen

    def getDashboard(self):
        return [widget.Tile for widget in self.widgets ]

    def addAPIWidget(self, widgetID, screen):

        if widgetID == 0:
            fr = BoredAPI(screen,"BoredAPI")
        else:
            fr = covidView(screen)
        #fr = testView(screen,15,50)
        self.widgets.append(fr)
        
        # fr = testView(screen,15,50,len(self.widgets))
        # self.widgets.append(fr)
        return len(self.widgets)-1


    def delAPIWidget(self, index):
        del self.widgets[index]

    def updateAPI(self):
        pass

    def getWidgetMenu(self):
        return self.widgetList
