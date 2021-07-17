


from APIWidgets.JokeAPI import JokeAPI
from APIWidgets.CryptoAPI import CryptoAPI
from APIWidgets.Calculator import calculator
from APIWidgets.BoredAPI import BoredAPI
from APIWidgets.CovidAPI import covidView


class WidgetManager:
    """
    Class that connects the UI to the widgets. It handles 
    creating, updating en deletion of widgets and passes 
    and passes the visual elements to the UI.
    """

    def __init__(self):
        # create a list that will hold added widgets
        self.widgets = []
        # list of available widgets 
        self.widgetList = [("Bored",0),("Covid",1),("Crypto",2),("Jokes",3),("Calculator",4)]

    # TODO: open a view that displays more details / options
    def getDetailView(self):
        pass

    # return the dashboard tile for a specific widget
    def getTile(self,id):
        return self.widgets[id].Tile

    # redraw widgets after screen resize
    def update_screen(self, screen):
        for widget in self.widgets:
            widget.Tile._canvas._screen = screen

    # return all widgets on dashboard
    def getDashboard(self):
        return [widget.Tile for widget in self.widgets ]

    # add new widget
    def addAPIWidget(self, widgetID, screen, height,width):

        if widgetID == 0:
            fr = BoredAPI(screen, height,width)
        elif widgetID ==1:
            fr = covidView(screen, height,width)
        elif widgetID ==2:
            fr = CryptoAPI(screen, height,width)
        elif widgetID ==3:
            fr = JokeAPI(screen, height,width)
        else:
            fr = calculator(screen, height,width)
        #fr = testView(screen,15,50)
        self.widgets.append(fr)
        
        # fr = testView(screen,15,50,len(self.widgets))
        # self.widgets.append(fr)
        return len(self.widgets)-1

    # TODO: removes widget, not called by anything
    def delAPIWidget(self, index):
        del self.widgets[index]

    # TODO: refresh widget content with new API call
    def updateAPI(self):
        pass

    # return list of possible widgets
    def getWidgetMenu(self):
        return self.widgetList
