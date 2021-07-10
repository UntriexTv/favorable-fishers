from rich.markdown import Markdown

from textual import events
from textual.app import App
from textual.view import DockView
from textual.widgets import Header, Footer, Placeholder, ScrollView, Static
from widgets import *


class LayoutApp(App):

    async def on_load(self, event):
        await self.bind("q", "quit")
        await self.bind("b", "bell")

    async action_bell(self):
    self.console.bell()


    async def get_layout(self) -> Layout:


    # Build your layout here

    async def on_startup(self, event: events.Startup) -> None:
        self.layout_widget = Static(self.get_layout())
        await self.dock(layout_widget)
        await self.set_interval(0.1, callback=self.get_layout)


    async def update_layout(self) -> None:
        self.layout_widget.update(self.get_layout())


LayoutApp.run()
