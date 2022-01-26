from email.policy import default
import click
import parser
import pathlib
import prod_logging as logging

log = logging.getLogger("rich")

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
    
    includes, excludes = parser.parse(project_path, exclude)
    # print(includes)
    
    # Show excluding files
    for ex in excludes:
        log.info(f"Excluding [bold green blink]{ex}[/]", extra={"markup": True})
    

@cli.command()
def version():
    """Print the version number."""
    click.echo(get_prod_current_version())

if __name__ == '__main__':
    cli()