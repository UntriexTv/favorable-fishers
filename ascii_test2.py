from asciimatics.screen import Screen
from asciimatics.scene import Scene
from asciimatics.widgets import Frame, ListBox, Layout, Divider, Text, \
    Button, TextBox, Widget, Label
from asciimatics.exceptions import ResizeScreenError, NextScene, StopApplication
from api_test import testAPI


# simple class to transfer data between frames
class viewManager(object):
    def __init__(self):
        self.widgets = {}
        self.id = None
        pass

    def addWidget(self,wdgt,id):
        self.widgets[id] = wdgt
 
    def getWidget(self):
        return self.widgets[str(self.id)].content
    

class wdgt(object):
    def __init__(self, testAPI):
        # self.content = [
        #     # Label(""),
        #     # Label(testAPI.title),
        #     # Label(testAPI.apiCall()),
        #     # Label("")
        #     "",
        #     testAPI.title,
        #     testAPI.apiCall(),
        #     ""
        # ]
        self.content = {
            "0":"",
            "1":testAPI.title,
            "2":testAPI.apiCall(),
            "3":""
        }
        

class widgetRow(Layout):
    def __init__(self, widgets, mainapp):
        nr_of_tiles = widgets
        self.mainapp = mainapp
        super(widgetRow, self).__init__([1 for x in range(nr_of_tiles)])


    def populate(self, widgets, offset):
        for i, wid in enumerate(widgets):
#            self.add_widget(wid,i)
            for key, label in wid.content.items():
                self.add_widget(Label(label),i)
            self.add_widget(Button("Open", self.mainapp._button_clicked, i+offset),i)

    def populate2(self, content):
        for key, label in content.items():
            self.add_widget(Text("a",name=key))


# defines the screen
class app(Frame):
    def __init__(self, screen, _title,_viewmanager):
        super(app, self).__init__(screen,
                                        screen.height ,
                                        screen.width ,
                                        hover_focus=True,
                                        can_scroll=False,
                                        title=_title,
                                       reduce_cpu=True)
        self.viewmanager = _viewmanager

        # list of all api's on dashboard, currently just a label
        #allWidgets = [Label("Weather"),Label("Crypto"),Label("News"),Label("Covid")]
        allWidgets = list(self.viewmanager.widgets.values())

        # divide widgets is smaller lists that match the columns
        cols = 2
        rows = [allWidgets[i:i+cols] for i in range(0,len(allWidgets),cols)  ]
        
        # create a layout based on the rows, use offset to create unique id's for button callback
        for offset,row in enumerate(rows):
            row_layout = widgetRow(cols,self)
            self.add_layout(row_layout)
            row_layout.populate(row, offset*cols)

        layout = Layout([1])
        self.add_layout(layout)
        layout.add_widget(Divider(height=5))
        layout.add_widget(Button("Quit", self._quit, None))


        self.fix()

    @staticmethod
    def _quit():
        raise StopApplication("User pressed quit")

    def _button_clicked(self, value):
        self.viewmanager.id = value 
        raise NextScene("details")


class DetailView(Frame):
    def __init__(self, screen, _title, _viewmanager):
        super(DetailView, self).__init__(screen,
                                        screen.height * 2 // 4,
                                        screen.width * 2 // 4,
                                        hover_focus=True,
                                        can_scroll=False,
                                        title=_title,
                                       reduce_cpu=True)
        self.viewmanager = _viewmanager

        layout = Layout([1],  fill_frame=True)
        self.add_layout(layout)
        layout.add_widget(Text("Contect:  ",name="2",readonly=True))
        row_layout = widgetRow(1,self)
        self.add_layout(row_layout)
        row_layout.populate2(self.data)



        layout.add_widget(Divider(height=5))
        layout.add_widget(Button("Close", self._on_close, None))
        self.fix()

    def _on_close(self):
        raise NextScene("main")

    #runs when scene is activated
    def reset(self):
        self.data = self.viewmanager.getWidget()
        


# create and start TUI
viewMan = viewManager()
allWidgets = {"0":wdgt(testAPI("Weather")),"1":wdgt(testAPI("Crypto")),"2":wdgt(testAPI("News")),"3":wdgt(testAPI("Covid"))}
viewMan.widgets = allWidgets

def appr(screen ):
    scenes = [
     Scene([app(screen,"Dashboard",viewMan)],name="main"),
     Scene([DetailView(screen,"DetailView",viewMan)],-1,name="details")
    ]

    screen.play(scenes)

Screen.wrapper(appr,catch_interrupt=True)