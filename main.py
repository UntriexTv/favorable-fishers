# This contians the layout for all the widget with the customsiation

from rich.layout import Layout
from rich.console import Console
from rich.live import Live

from time import sleep
import sys

sys.path.insert(0, './Widgets')

from table import *
from weather import *
from covid import *

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
	with open('settings.json') as json_file:
		data = json.load(json_file)

	#layout['top left'].update()
	layout['middle left'].update(make_covid_table())
	#layout['bottom left'].update()

	#layout['top middle'].update()
	#layout['middle middle'].update()
	#layout['bottom middle'].update()

	#layout['top right'].update()
	layout['middle right'].update(generate_table()) 
	#layout['bottom right'].update()
	exec('')

layout = make_grid()
update_grid()

with Live(layout, screen=True):
	while True:
		sleep(1)
		update_grid()
		