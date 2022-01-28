import parser
import prod_logging as logging
import archive

log = logging.getLogger("rich")



def create( project_path, exclude, output ):
    """Create a production package."""
    files, excludes = parser.parse(project_path, exclude)

    # Show excluding files
    for ex in excludes:
        log.info(f"Excluding [bold green blink]{ex}[/]", extra={"markup": True})

    log.info(f"Project packed into [bold green blink]{output}[/]", extra={"markup": True})

    archive.pack(project_path, files, excludes, output)