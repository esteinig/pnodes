from textwrap import dedent
from dateutil import parser

class Node:
    """ Minimal implementation of PBS Node """

    def __init__(self, name):

        self.name = name

        self.ntype = None
        self.state = None
        self.jobs = list()
        self.arch = None
        self.host = None
        self.available_mem = None
        self.available_ncpus = None
        self.assigned_mem = None
        self.assigned_ncpus = None

        self.last_state_change_time = None
        self.last_used_time = None

        self.print_percent = False

    def print_capacity(self):

        print(f"{self.name}\t{self.available_ncpus} cpu\t{self.available_mem} gb")

    def __str__(self):

        if self.print_percent:
            cpu = f"{round((self.assigned_ncpus/self.available_ncpus)*100, 0)}" + "%"
            mem = f"{round((self.assigned_mem/self.available_mem)*100, 0)}" + "%"
        else:
            cpu = f"{self.assigned_ncpus}/{self.available_ncpus}"
            mem = f"{self.assigned_mem}/{self.available_mem}"

        return f"{self.name}\t" + f"{cpu:<5} cpu\t" + f"{mem:<8} mem\t" + f"{len(self.jobs):<2} jobs\t "



def parse_node_status(status):

    node = None
    nodes = list()
    for line in status.splitlines():
        if line.startswith(' '):
            param, value = line.strip().split('=')
            param = param.strip()
            if param == 'ntype':
                node.ntype = value
            elif param == 'state':
                node.state = value
            elif param == 'jobs':
                jobs = list()
                for j in [x.split('/')[0] for x in value.split()]:
                    if j not in jobs:
                        jobs.append(j)
                node.jobs = jobs
            elif param == 'resources_available.arch':
                node.arch = value
            elif param == 'resources_available.host':
                node.host = value
            elif param == 'resources_available.mem':
                node.available_mem = int(int(''.join(x for x in value if x.isdigit()))/1e06)  # GB
            elif param == 'resources_available.ncpus':
                node.available_ncpus = int(value)
            elif param == 'resources_assigned.mem':
                node.assigned_mem = int(int(''.join(x for x in value if x.isdigit()))/1e06) # GB
            elif param == 'resources_assigned.ncpus':
                node.assigned_ncpus = int(value)
            elif param == 'last_state_change_time':
                node.last_state_change_time = parser.parse(value)
            elif param == 'last_used_time':
                node.last_used_time = parser.parse(value)
            else:
                pass

        else:
            name = line.strip()
            if name:
                nodes.append(node)
                node = Node(name=name)

    # Last Node:
    nodes.append(node)

    return nodes[1:]
