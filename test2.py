from textual.app import App
from textual import events
from textual.view import View
from textual.widgets import Static, Header, Footer, ScrollView
from textual.layouts.grid import GridLayout
from widgets import *



class GridTest(App):
    async def on_load(self, event: events.Load) -> None:
        await self.bind("q,ctrl+c", "quit", "Quit")
        await self.bind("b", "change", "Testing")
        self.table = TestingWidget()
        self.widgets = [0, 0, 0, 0]
        self.available_widgets = []
        self.available_widgets.append(TestingWidget())
        self.available_widgets.append(AboutWidget())
        self.available_widgets.append(TestingPanel())

    async def update_layout(self):
        await self.l1.update(self.available_widgets[self.widgets[0]].run(self.l1))
        await self.l2.update(self.available_widgets[self.widgets[1]].run(self.l2))
        await self.l3.update(self.available_widgets[self.widgets[2]].run(self.l3))
        await self.l4.update(self.available_widgets[self.widgets[3]].run(self.l4))

    async def action_change(self):
        if self.focused:
            if self.widgets[int(self.focused.name)] >= len(self.available_widgets) - 1:
                self.widgets[int(self.focused.name)] = 0
            else:
                self.widgets[int(self.focused.name)] += 1
            await self.focused.update(self.available_widgets[self.widgets[int(self.focused.name)]].run(self.focused))

    async def on_startup(self, event: events.Startup) -> None:

        layout = GridLayout()
        view = await self.push_view(View(layout=layout))
        view.set_interval(0.1, callback=self.update_layout)
        self.l1 = ScrollView("", name="0")
        self.l2 = Static("", name="1")
        self.l3 = Static("", name="2")
        self.l4 = Static("", name="3")
        layout.add_column(fraction=1, name="left", min_size=20)
        layout.add_column(size=30, name="center")
        layout.add_column(fraction=1, name="right")

        layout.add_row(fraction=1, name="top")
        layout.add_row(fraction=2, name="middle")
        layout.add_row(fraction=1, name="bottom")
        layout.add_areas(
            area1="left,top-start|middle-end",
            area2="center,middle",
            area3="left-start|right-end,bottom",
            area4="right,top-start|middle-end",
        )

        layout.place(
            area1=self.l1,
            area2=self.l2,
            area3=self.l3,
            area4=self.l4,
        )


GridTest.run(title="Grid Test")