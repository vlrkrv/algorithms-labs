class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []
        self.parent = [i for i in range(vertices)]
    
    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])
    
    def find(self, i):
        if self.parent[i] == i:
            return i
        return self.find(self.parent[i])
    
    def union(self, u, v):
        u_root = self.find(u)
        v_root = self.find(v)
        self.parent[u_root] = v_root
    
    def kruskal(self):
        result = []
        total_weight = 0
        
        self.graph = sorted(self.graph, key=lambda item: item[2])
        
        i = 0
        e = 0
        
        while e < self.V - 1:
            u, v, w = self.graph[i]
            i += 1
            
            u_root = self.find(u)
            v_root = self.find(v)
            
            if u_root != v_root:
                e += 1
                result.append([u, v, w])
                total_weight += w
                self.union(u_root, v_root)
        
        return result, total_weight

g = Graph(8)

g.add_edge(0, 1, 8)  # 1-2
g.add_edge(0, 2, 2)  # 1-3
g.add_edge(0, 3, 4)  # 1-4
g.add_edge(0, 4, 3)  # 1-5
g.add_edge(1, 4, 6)  # 2-5
g.add_edge(1, 5, 3)  # 2-6
g.add_edge(2, 3, 6)  # 3-4
g.add_edge(2, 5, 7)  # 3-6
g.add_edge(2, 7, 4)  # 3-8
g.add_edge(3, 4, 1)  # 4-5
g.add_edge(4, 6, 4)  # 5-7
g.add_edge(5, 6, 3)  # 6-7
g.add_edge(5, 7, 1)  # 6-8
g.add_edge(6, 7, 5)  # 7-8

result, total_weight = g.kruskal()

print("Edge : Weight")
for u, v, weight in result:
    print(f"{u+1} - {v+1} : {weight}")

print(f"Total Weight: {total_weight}")
