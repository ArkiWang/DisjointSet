
class DisjointSet:
    def __init__(self):
        self.DSet = {}

    def make_set(self, v):
        self.DSet[v] = v

    def find_set(self, x):
        if self.DSet[x] != x:
            self.DSet[x] = self.find_set(self.DSet[x])
        return self.DSet[x]

    def union(self, x, y):
        dsetx = self.find_set(x)
        dsety = self.find_set(y)
        if dsetx != None and dsety != None:
            self.DSet[dsetx] = dsety

    def connected_components(self, pairs: [], vertexes: []):
        for v in vertexes:
            self.make_set(v)
        for (u, v) in pairs:
            if self.find_set(v) != self.find_set(u):
                self.union(u, v)


    def same_componet(self, u, v):
        if self.find_set(u) == self.find_set(v):
            return True
        return False


