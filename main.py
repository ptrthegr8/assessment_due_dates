import datetime

import click
from dateutil import parser


def generate_drop_dead_due_date(dd):
    dd_delta = datetime.timedelta(days=5)
    dd_due_date = dd + dd_delta
    return dd_due_date


def generate_two_weeks_date(dd_due_date):
    dd_delta = datetime.timedelta(days=14)
    two_week_due_date = dd_due_date + dd_delta
    return two_week_due_date


@click.command()
@click.option(
    "--due_date",
    default=datetime.datetime.now,
    prompt="Your due date",
    help="due date for assessment.",
)
def get_due_dates(due_date):
    dd = parser.parse(due_date)
    dd_due_date = generate_drop_dead_due_date(dd)
    two_week_due_date = generate_two_weeks_date(dd_due_date)
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
