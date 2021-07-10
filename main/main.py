from rich.console import Console
from rich.layout import Layout
from rich.live import Live
from time import sleep
from rich.table import Table
import random

console = Console()


class GenereteTable():
    def __init__(self):
        pass

    def setup(self):
        kk = console.input("hello: ")
        console.print(kk)

    def run(self):
        """Make a new table."""
        table = Table()
        table.add_column("ID")
        table.add_column("Value")
        table.add_column("Status")

        for row in range(random.randint(2, 6)):
            value = random.random() * 100
            table.add_row(
                f"{row}", f"{value:3.2f}", "[red]ERROR" if value < 50 else "[green]SUCCESS"
            )
        return table


def make_layout() -> Layout:
    layout = Layout(name="root")
    layout.split(
        Layout(name="header", size=3),
        Layout(ratio=1, name="main"),
        Layout(size=10, name="footer"),
    )
    layout["main"].split_row(
        Layout(name="side"),
        Layout(name="body", ratio=2))
    layout["side"].split(Layout(), Layout())
    return layout


table = GenereteTable()
table.setup()
layout = make_layout()
layout["body"].update(table.run())

with Live(layout, screen=True):
    while True:
        sleep(0.1)
        layout["body"].update(table.run())