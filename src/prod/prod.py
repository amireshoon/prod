import click

@click.command()
def version():
    """Print the version number."""
    click.echo('0.0.1')
