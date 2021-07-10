from rich.layout import Layout
from rich.markdown import Markdown

from textual import events
from textual.app import App
from textual.view import DockView, View
from textual.widgets import Header, Footer, Placeholder, ScrollView, Static
from widgets import *


class LayoutApp(App):
    async def on_load(self, event):
        await self.bind("q", "quit")
        await self.bind("b", "bell")

    async def action_bell(self):
        self.console.bell()

    async def get_layout(self):
        table = TestingWidget("")
        return table.run()

    async def on_startup(self, event: events.Startup) -> None:
        view = await self.push_view(DockView())
        self.layout_widget = Static(await self.get_layout())
        await view.dock(self.layout_widget)
        view.set_interval(0.1, callback=self.update_layout)

    async def update_layout(self) -> None:
        self.layout_widget.renderable = await self.get_layout()
        self.layout_widget.require_repaint()


LayoutApp.run()
