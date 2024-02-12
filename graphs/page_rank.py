"""
Author: https://github.com/bhushan-borole
"""
"""
The input graph for the algorithm is:

  A B C
A 0 1 1
B 0 0 1
C 1 0 0

"""

class Node:
    def __init__(self, name):
        self.name = name
        self.inbound = []
        self.outbound = []

    def add_inbound(self, node):
        self.inbound.append(node)

    def add_outbound(self, node):
        self.outbound.append(node)

    def __repr__(self):
        return f"<node={self.name} inbound={self.inbound} outbound={self.outbound}>"


def page_rank(nodes, limit=3, d=0.85):
    ranks = {}
    for node in nodes:
        ranks[node.name] = 1

    outbounds = {}
    for node in nodes:
        outbounds[node.name] = len(node.outbound)

    for i in range(limit):
        print(f"======= Iteration {i + 1} =======")
        for _, node in enumerate(nodes):
            ranks[node.name] = (1 - d) + d * sum(
                ranks[ib] / outbounds[ib] for ib in node.inbound
            )
        print(ranks)
