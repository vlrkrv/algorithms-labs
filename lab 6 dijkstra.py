import heapq

def dijkstra(graph, start):
    n = len(graph)
    dist = [float('inf')] * n
    pred = [-1] * n
    dist[start] = 0
    pq = [(0, start)]
    
    while pq:
        current_dist, u = heapq.heappop(pq)
        if current_dist > dist[u]:
            continue
            
        for v, weight in graph[u]:
            distance = current_dist + weight
            if distance < dist[v]:
                dist[v] = distance
                pred[v] = u
                heapq.heappush(pq, (distance, v))
    
    return dist, pred

# Граф варіанту 15
graph = [
    [(1, 8), (2, 2), (3, 4), (4, 3)],  # 1
    [(0, 8), (4, 6), (5, 3)],          # 2
    [(0, 2), (3, 6), (5, 7), (7, 4)],  # 3
    [(0, 4), (2, 6), (4, 1)],          # 4
    [(0, 3), (1, 6), (3, 1), (6, 4)],  # 5
    [(1, 3), (2, 7), (6, 3), (7, 1)],  # 6
    [(4, 4), (5, 3), (7, 5)],          # 7
    [(2, 4), (5, 1), (6, 5)]           # 8
]

start_vertex = 0  # Стартова вершина 1

# Виконуємо алгоритм Дейкстри
distances, predecessors = dijkstra(graph, start_vertex)

# Виводимо результати в трьох колонках
print("Вершина | Відстань | Попередник")
print("-" * 30)
for i in range(len(distances)):
    pred_str = str(predecessors[i] + 1) if predecessors[i] != -1 else "None"
    print(f"   {i+1}    |    {int(distances[i])}    |     {pred_str}")
