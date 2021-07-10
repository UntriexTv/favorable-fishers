import time

from rich.markdown import Markdown
from rich.console import Console
from textual import events
from textual.app import App
from textual.view import Layout, View
from textual.views import DockView
from textual.widgets import Header, Footer, Placeholder, ScrollView, Static

from widgets import *


class MyApp(App):
    async def on_load(self, event: events.Load) -> None:
        await self.bind("q,ctrl+c", "quit")
        await self.bind("v", "view.toggle('sidebar_l')")
        await self.bind("b", "view.toggle('sidebar_r')")
        await self.bind("ctrl+v", "change_l('test')")
        await self.bind("ctrl+b", "view.toggle('sidebar_r')")

    async def change_l(self, test):
        print(test)
        self.sidebar_l.renderable = "name"
        self.sidebar_l.require_repaint()

    async def change_r(self):
        pass

    async def on_startup(self, event: events.Startup) -> None:
        view = await self.push_view(DockView())
        header = Header("")
        footer = Footer()
        self.sidebar_l = ScrollView("test", name="sidebar_l")
        self.sidebar_r = Placeholder(name="sidebar_r")
        self.table = AboutWidget()
        self.body = Static(self.table.run())

        footer.add_key("b", "Toggle sidebar")
        footer.add_key("q", "Quit")

        await view.dock(header, edge="top")
        await view.dock(footer, edge="bottom")
        await view.dock(self.sidebar_l, edge="left", size=30)
        await view.dock(self.sidebar_r, edge="right", size=30)
        await view.dock(self.body, edge="right")
        self.require_layout()

    async def on_timer(self, event: events.Timer) -> None:
        self.body.renderable = self.table.run()
        self.body.require_repaint()


app = MyApp(title="Simple App")
app.run()
