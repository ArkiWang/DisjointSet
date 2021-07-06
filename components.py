class Node:
    def __init__(self, val, p=None, rank=-1):
        self.val = val
        self.p = p
        self.rank = rank

class Graph:
    def __init__(self, v: {}, e: []):
        self.vertexes = v
        self.edges = e