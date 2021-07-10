from rich.table import Table
import random

class TestingWidget():
    def __init__(self, console):
        self.console = console

    def setup(self):
        kk = self.console.input("hello: ")
        self.console.print(kk)

    def run(self):
        """Make a new table."""
        table = Table(expand=True)
        table.add_column("ID")
        table.add_column("Value")
        table.add_column("Status")

        for row in range(random.randint(2, 6)):
            value = random.random() * 100
            table.add_row(
                f"{row}", f"{value:3.2f}", "[red]ERROR" if value < 50 else "[green]SUCCESS"
            )
        return table


widgets = [TestingWidget]
