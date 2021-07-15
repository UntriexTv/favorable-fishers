


from APIWidgets.BoredAPI import BoredAPI


class WidgetManager:
    def __init__(self):
        self.widgets = []
        self.widgetList = [("Bored",0),("Weather",1),("Covid",2)]

    def getDetailView(self):
        pass

    def getTile(self,id):
        return self.widgets[id].Tile

    def getDashboard(self):
        return [widget.Tile for widget in self.widgets ]

    def addAPIWidget(self, widgetID, screen):
        
        self.widgets.append(BoredAPI(screen,"BoredAPI"))
        return len(self.widgets)


    def delAPIWidget(self, index):
        del self.widgets[index]

    def updateAPI(self):
        pass

    def getWidgetMenu(self):
        return self.widgetList
