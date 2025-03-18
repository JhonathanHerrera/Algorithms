
#Kruskal a.k.a minimum spanning tree
#O (E * log(E))

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x]) 
        return self.parent[x]

    def union(self, x, y):
        self.parent[self.find(x)] = self.find(y) 


def kruskal(n, edges):
    edges.sort(key=lambda x: x[2])
    uf = UnionFind(n) 
    mst = [] 

    for u,v,weight in edges:
        if uf.find(u) != uf.find(v):
            mst.append((u,v,weight))
            uf.union(u,v) 
    return mst