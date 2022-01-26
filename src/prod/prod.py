from email.policy import default
import click
import parser
import pathlib
import prod_logging as logging
import package
from rich.console import Console
from time import sleep
log = logging.getLogger("rich")
console = Console()
tasks = [
    "Prod file loaded",
    "Files excluded",
    "Project packed",
]

def get_prod_current_version():
    return '0.0.1'

@click.group()
def cli():
    pass

@cli.command()
@click.option('--output', '-o', default='prod.zip', help='Output file name.')
@click.option('--exclude', '-e', multiple=True, help='Exclude files.')
@click.argument('project_path', default=".")
def make(output, exclude, project_path):
    """Make production package."""


    if project_path == ".":
        project_path = pathlib.Path().resolve()
    

    log.info(f"Loading from [bold blue blink]{project_path}[/]", extra={"markup": True})
    
    # Create a production package
    # package.create(project_path, exclude, output)
    # task = tasks.pop(0)
    
    package.create(project_path, exclude, output)
    logging.update(f"Created [bold green blink]{output}[/]")
    

@cli.command()
def version():
    """Print the version number."""
    click.echo(get_prod_current_version())

if __name__ == '__main__':
    cli()