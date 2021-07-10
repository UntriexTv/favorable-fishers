from rich.console import Console
from rich.layout import Layout
from rich.live import Live
from time import sleep
from rich.table import Table
import random
from widgets import *
import json

console = Console()

def make_layout() -> Layout:
    layout = Layout(name="root")
    layout.split(
        Layout(name="header", size=3),
        Layout(ratio=1, name="main"),
        Layout(size=3, name="footer"),
    )

    return layout


table = TestingWidget(console)
table.setup()
layout = make_layout()
layout["body"].update(table.run())

with Live(layout, screen=True):
    while True:
        sleep(1)
        layout["body"].update(table.run())
