import click

from pnodes.pnodes import PBSNodes

@click.command()
def list():
    """ Display usage/capacity by node. """
    pbsnodes = PBSNodes()
    pbsnodes.parse_status(total=False, capacity=False)

