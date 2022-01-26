import os

import prod_logging as logging

log = logging.getLogger("rich")

def is_dir(path):
    """Check if the path is a directory."""
    return os.path.isdir(path)

def load_file_from_dir(dir_path, file_name):
    """Load a file from a directory."""
    return load_from_file(os.path.join(dir_path, file_name))

def load_from_file(file_path):
    """Load a file and return its content."""
    if is_dir(file_path):
        return load_file_from_dir(file_path, ".prod")

    if not os.path.isfile(file_path):
        log.error(f"[bold red blink]{file_path}[/] Is not a file", extra={"markup": True})
        exit(1)

    with open(file_path, "r", encoding="utf-8") as fh:
        return fh.read()

def parse( project_path, exclude ):
    """Parse the .prod file and return the list of files to exclude."""
    try:
        content = load_from_file(project_path)
    except FileNotFoundError:
        log.error(f"File not found: [bold red blink]{project_path}[/]", extra={"markup": True})
        exit(1)

    lines = content.splitlines()
    files = []
    excludes = []
    for line in lines:
        # Remove comments
        if line.startswith("#"):
            continue

        # Remove excludes
        if line.startswith("!"):
            if line[1:] in files:
                files.remove(line[1:])
            continue

        files.append(line)
    
    exclude = tuple(excludes) + exclude
    
    for file_name in exclude:
        if file_name in files:
            files.remove(file_name)
    
    return files, exclude