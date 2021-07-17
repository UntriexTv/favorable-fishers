from asciimatics.widgets import Frame

class APIWidget():
    """
    Interface that widgets must implement
    """
    def __init__(self, screen, height,width):
        pass

    # defines the tile layout
    def createTile(self,screen, height, width) -> Frame:
        pass

    # TODO: not yet implemented in dashboard
    def createDetailView(self) -> Frame:
        pass

    def fetch_data(self):
        pass

    def setAPIparameters(self): 
        pass
