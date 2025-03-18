
'''

This is a good LC questions that uses Kruskal and Union Find.

You are given an array points representing integer coordinates of some points on a 2D-plane, where points[i] = [xi, yi].

The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan distance between them: |xi - xj| + |yi - yj|, where |val| denotes the absolute value of val.

Return the minimum cost to make all points connected. All points are connected if there is exactly one simple path between any two points.

'''

class UnionFind:
    def __init__(self,n):
        self.parent = list(range(n))
    
    def find(self,root):
        if self.parent[root] != root:
            self.parent[root] = self.find(self.parent[root]) 
        return self.parent[root] 

    def union(self,root_x,root_y):
        root_x = self.find(root_x)
        root_y = self.find(root_y)
        if root_x != root_y:
            self.parent[root_x] = root_y  
    


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        def getCost(x1, y1, x2, y2):
            return abs(x1 - x2) + abs(y1 - y2)
    
        n = len(points)
        union = UnionFind(n)
        nodes = []

        for i in range(n):
            for j in range(i+1,n):
                cost = getCost(points[i][0], points[i][1], points[j][0], points[j][1])
                nodes.append((cost,i,j)) 
        
        nodes.sort()
        num_nodes = 0
        res = 0

        for cost, u, v in nodes:
            if union.find(u) != union.find(v):
                union.union(u,v)
                res += cost 
                num_nodes += 1
                if num_nodes == n-1:
                    break 
        
        return res