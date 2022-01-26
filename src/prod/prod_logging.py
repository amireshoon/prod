import logging
from rich.logging import RichHandler
from rich.console import Console

log = logging.getLogger("rich")
console = Console()
tasks = [
    "Prod file loaded",
    "Files excluded",
    "Project packed",
]

FORMAT = "%(message)s"
logging.basicConfig(
    level="NOTSET", format=FORMAT, datefmt="[%X]", handlers=[RichHandler()]
)

console = Console()
    
def getLogger(name):
    return logging.getLogger(name)

def update(message):
    tasks.pop(0)
    console.log(message)