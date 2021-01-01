from components import *
class DisjointSet:
    def __init__(self, G: Graph):
        self.G = G

    def make_set(self, x: Node):
        x.p = x
        x.rank = 0

    def find_set(self, x: Node):
        if x != x.p:
            x.p = self.find_set(x.p)
        return x.p

    def union(self, x: Node, y: Node):
        self.link(self.find_set(x), self.find_set(y))

    def link(self, x: Node, y: Node):
        if x.rank > y.rank:
            y.p = x
        else:
            x.p = y
            if x.rank == y.rank:
                y.rank += 1

    def connected_components(self, G: Graph):
        for v in G.vertexes:
            self.make_set(G.vertexes[v])
        for (u, v) in G.edges:
            if self.find_set(G.vertexes[u]) != self.find_set(G.vertexes[v]):
                self.union(G.vertexes[u], G.vertexes[v])

    def same_component(self, u, v):
        if self.find_set(u) == self.find_set(v):
            return True
        else:
            return False
