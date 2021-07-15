


from APIWidgets.BoredAPI import BoredAPI
from testwid import testView


class WidgetManager:
    def __init__(self):
        self.widgets = []
        self.widgetList = [("Bored",0),("Weather",1),("Covid",2)]

    def getDetailView(self):
        pass

    def getTile(self,id):
        #return self.widgets[id].Tile
        # return self.widgets[id]
        raise ValueError("het is" + str(self.widgets))
        return self.widgets[0].Tile

    def getDashboard(self):
        return [widget.Tile for widget in self.widgets ]

    def addAPIWidget(self, widgetID, screen):
        fr = BoredAPI(screen,"BoredAPI")
        #fr = testView(screen,15,50)
        self.widgets.append(fr)
        
        # fr = testView(screen,15,50,len(self.widgets))
        # self.widgets.append(fr)
        return len(self.widgets)


    def delAPIWidget(self, index):
        del self.widgets[index]

    def updateAPI(self):
        pass

    def getWidgetMenu(self):
        return self.widgetList
