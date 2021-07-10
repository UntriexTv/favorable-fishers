# This contians the layout for all the widget with the customsiation

from rich.layout import Layout
from rich.console import Console
from rich.live import Live
from rich.table import Table

from time import sleep
import random

def generate_table() -> Table:
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


def make_grid():
	layout = Layout(name='Dashboard')
	layout.split_row(
		Layout(name='left', ratio=1),
		Layout(name='middle', ratio=1),
		Layout(name='right', ratio=1)
		)

	layout['left'].split_column(
		Layout(name='top left', ratio=1),
		Layout(name='middle left', ratio=1),
		Layout(name='bottom left', ratio=1)
		)

	layout['middle'].split_column(
		Layout(name='top middle', ratio=1),
		Layout(name='middle middle', ratio=1),
		Layout(name='bottom middle', ratio=1)
		)

	layout['right'].split_column(
		Layout(name='top right', ratio=1),
		Layout(name='middle right', ratio=1),
		Layout(name='bottom right', ratio=1)
		)

	return layout


def update_grid():
	#layout['top left'].update()
	#layout['middle left'].update()
	#layout['bottom left'].update()

	#layout['top middle'].update()
	#layout['middle middle'].update()
	#layout['bottom middle'].update()

	#layout['top right'].update()
	layout['middle right'].update(generate_table())
	#layout['bottom right'].update()

layout = make_grid()
update_grid()

with Live(layout, screen=True):
	while True:
		sleep(1)
		update_grid()
		