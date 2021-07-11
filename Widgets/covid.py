import requests 
import json
from rich.console import Console
from rich.table import Table

def format_json(obj):
	# Create a formatted string of the Python JSON object
	return obj[0]

def make_covid_table() -> Table:
	url = 'https://api.covid19api.com/live/country/united-kingdom/status/confirmed'

	payload={}
	headers = {}

	response = requests.request("GET", url, headers=headers, data=payload)

	data = format_json(response.json())

	# Table itself
	table = Table(title="Covid Stats")

	# Columns
	table.add_column("key", justify="right", style="cyan", no_wrap=True)
	table.add_column("data", justify="center", style="magenta")

	# Rows
	table.add_row('Country', data['Country'])
	table.add_row('Confirmed', str(data['Confirmed']))
	table.add_row('Deaths', str(data['Deaths']))
	table.add_row('Recovered', str(data['Recovered']))
	table.add_row('Active', str(data['Active']))
	table.add_row('Date', str(data['Date']))

	return table