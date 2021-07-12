from asciimatics.widgets import Frame, ListBox, Layout, Divider, Text, \
    Button, TextBox, Widget, Label


class Placeholder(Frame):
    def __init__(self, screen, model):
        super(Placeholder, self).__init__(screen,
                                          screen.height * 2 // 3,
                                          screen.width * 2 // 3,
                                          hover_focus=True,
                                          can_scroll=False,
                                          title="Placeholder",
                                          reduce_cpu=True)    
