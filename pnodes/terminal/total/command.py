import click

from pnodes.pnodes import PBSNodes

@click.command()
def total():
    """ Display total usage/capacity. """
    pbsnodes = PBSNodes()
    pbsnodes.parse_status(total=True, capacity=False)

