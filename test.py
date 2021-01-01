from  components import *
from DisjointSet import DisjointSet
eages = [('b','d'), ('e','g'), ('a', 'c'), ('h', 'i'), ('a' ,'b'), ('e', 'f'), ('b','c'),('a','g')]
vs = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
ves = {}
for v in vs:
    ve = Node(v)
    ves[v] = ve
G = Graph(ves, eages)
dset = DisjointSet(G)
dset.connected_components(G)
print(G)
