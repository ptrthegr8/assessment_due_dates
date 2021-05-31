from datetime import datetime, timedelta

import click
from dateutil import parser


def calc_new_due_date(date: datetime, days: int) -> datetime:
    delta = timedelta(days=days)
    new_due_date = date + delta
    return new_due_date


@click.command()
@click.option(
    "--due_date",
    default=datetime.now,
    prompt="Enter due date",
    help="due date for assessment.",
)
def get_due_dates(due_date: str) -> None:
    dd = parser.parse(due_date)
    dd_due_date = calc_new_due_date(dd, 5)
    two_week_due_date = calc_new_due_date(dd_due_date, 14)
    output_format = "%A, %B %d, %Y"

    click.echo(
        f"""
        Due Date: {dd.strftime(output_format)} 
        Drop Dead Due Date: {dd_due_date.strftime(output_format)} 
        Two Week Due Date: {two_week_due_date.strftime(output_format)}
        """
    )


if __name__ == "__main__":
    get_due_dates()
