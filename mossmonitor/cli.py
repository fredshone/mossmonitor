"""Console script for mossmonitor."""

import click


@click.version_option(package_name="mossmonitor")
@click.command()
def cli(args=None):
    """Console script for mossmonitor."""
    click.echo(
        "Replace this message by putting your code into mossmonitor.cli.cli"
    )
    click.echo("See click documentation at https://click.palletsprojects.com/")
    return 0
