import click

from pnodes.pnodes import PBSNodes

@click.command()
def cap():
    """ Display node capacity by node. """
    pbsnodes = PBSNodes()
    pbsnodes.parse_status(total=False, capacity=True)

