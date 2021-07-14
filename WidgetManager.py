


from APIWidgets.BoredAPI import BoredAPI


class WidgetManager:
    def __init__(self):
        self.widgets = []
        self.widgetList = [("Weather",0),("Covid",1)]

    def getDetailView(self):
        pass

    def getTile(self):
        pass

    def getDashboard(self):
        return [widget.getTile() for widget in self.widgets ]

    def addAPIWidget(self, widgetID, screen):

        self.widgets.append(BoredAPI(screen))

    def delAPIWidget(self, index):
        del self.widgets[index]

    def updateAPI(self):
        pass

    def getWidgetMenu(self):
        return self.widgetList
