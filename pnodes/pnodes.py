import delegator

from pnodes.utils import parse_node_status

class PBSNodes:

    def __init__(self, command='pbsnodes -a'):

        self.command = command

    def get_status(self):

        return delegator.run(self.command).out

    def parse_status(self, capacity=False, total=True, percent=False):

        status = self.get_status()

        nodes = parse_node_status(status)

        if total:
            self.print_total_status(nodes)
        else:
            for node in nodes:
                if capacity:
                    node.print_capacity()
                else:
                    if percent:
                        node.print_percent = percent
                    print(node)

    @staticmethod
    def print_total_status(nodes):

        mem = sum([node.available_mem for node in nodes])
        mem_assigned = sum([node.assigned_mem for node in nodes])
        ncpu = sum([node.available_ncpus for node in nodes])
        ncpu_assigned = sum([node.assigned_ncpus for node in nodes])

        total_cpu_percent = round((ncpu_assigned/ncpu)*100, 0)
        total_mem_percent =  round((mem_assigned/mem)*100, 0)

        print(f"cpu\t{ncpu_assigned}/{ncpu}\t{total_cpu_percent}%\n"
              f"mem\t{mem_assigned}/{mem}\t{total_mem_percent}%")