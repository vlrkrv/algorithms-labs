INF = 9999999
V = 8

G = [
    [0, 8, 2, 4, 3, INF, INF, INF],
    [8, 0, INF, INF, 6, 3, INF, INF],
    [2, INF, 0, 6, INF, 7, INF, 4],
    [4, INF, 6, 0, 1, INF, INF, INF],
    [3, 6, INF, 1, 0, INF, 4, INF],
    [INF, 3, 7, INF, INF, 0, 3, 1],
    [INF, INF, INF, INF, 4, 3, 0, 5],
    [INF, INF, 4, INF, INF, 1, 5, 0]
]

selected = [False] * V
selected[0] = True
no_edge = 0
total_weight = 0

print("Edge : Weight")

while no_edge < V - 1:
    minimum = INF
    x = 0
    y = 0
    
    for i in range(V):
        if selected[i]:
            for j in range(V):
                if not selected[j] and G[i][j]:
                    if minimum > G[i][j]:
                        minimum = G[i][j]
                        x = i
                        y = j
    
    print(f"{x+1} - {y+1} : {G[x][y]}")
    total_weight += G[x][y]
    selected[y] = True
    no_edge += 1

print(f"Total Weight: {total_weight}")
