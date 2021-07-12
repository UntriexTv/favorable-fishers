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
        await self.bind("b", "view.toggle('sidebar_r')")
        await self.bind("v", "changel", "Testing")
        self.press = 0

    async def action_changel(self):
        await self.body.update("hii")

    async def on_key(self, event: events.Key) -> None:
        try:
            await self.body.update(str(self.press))
            self.press += 1
        except:
            pass


    async def change_r(self):
        pass

    async def on_startup(self, event: events.Startup) -> None:
        view = await self.push_view(DockView())
        header = Header()
        footer = Footer()
        self.sidebar_l = Static("test", name="sidebar_l")
        self.sidebar_l_l = Static("test2", name="sidebar_l_l")
        self.sidebar_r = Placeholder(name="sidebar_r")
        self.table = AboutWidget()
        self.body = Static(self.table.run())

        footer.add_key("b", "Toggle sidebar")
        footer.add_key("q", "Quit")

        await view.dock(header, edge="top")
        await view.dock(footer, edge="bottom")
        await view.dock(self.sidebar_l, edge="left", size=30)
        await view.dock(self.sidebar_l_l, edge="left", size=30)
        await view.dock(self.sidebar_r, edge="bottom")
        await view.dock(self.body, edge="right")
        self.require_layout()

    #async def on_timer(self, event: events.Timer) -> None:
    #    await self.body.update(self.table.run())


app = MyApp(title="Simple App")
app.run()
