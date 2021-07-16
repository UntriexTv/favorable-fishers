from rich.console import Console
from rich.table import Table
import random

class GenereteTable():
    def __init__(self):
        pass

    def setup(self):
        kk = Console.input("hello: ")
        Console.print(kk)

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