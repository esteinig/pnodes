import click

from .list import list
from .cap import cap
from .total import total

VERSION = '0.1'


@click.group()
@click.version_option(version=VERSION)
def terminal_client():
    pass


terminal_client.add_command(list)
terminal_client.add_command(total)
terminal_client.add_command(cap)