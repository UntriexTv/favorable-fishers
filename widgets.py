from rich.table import Table
import random


class TestingWidget:
    def setup(self):
        pass

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


class AboutWidget:
    def __init__(self):
        self.dev = [
            {"name": "Untriex", "git": "place_holder"},
            {"name": "caasitroplla", "git": "place_holder"},
            {"name": "nivranshu", "git": "place_holder"},
            {"name": "CB", "git": "place_holder"},
            {"name": "desmy", "git": "place_holder"},
            {"name": "kedi hacker", "git": "place_holder"}
        ]

    def run(self):
        """Make a new table."""

        table = Table.grid(expand=True)
        table.add_row(":computer: [bold red]Made By:[/bold red] :computer:")
        table.add_row("")
        for developer in self.dev:
            table.add_row(
                ":point_right:  " + developer["name"], f"""[blue]{developer["git"]}"""
            )
        table.add_row("")
        table.add_row("[red]For SummerCodeJam[/red] [bold green]2021[/bold green]")
        return table


widgets = [TestingWidget]
