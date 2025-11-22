INF = 10**9

# Початкова матриця ваг графа
W = [
    [0, 8, 2, 4, 3, INF, INF, INF],
    [8, 0, INF, INF, 6, 3, INF, INF],
    [2, INF, 0, 6, INF, 7, INF, 4],
    [4, INF, 6, 0, 1, INF, INF, INF],
    [3, 6, INF, 1, 0, INF, 4, INF],
    [INF, 3, 7, INF, INF, 0, 3, 1],
    [INF, INF, INF, INF, 4, 3, 0, 5],
    [INF, INF, 4, INF, INF, 1, 5, 0]
]

def floyd_warshall(matrix):
    n = len(matrix)
    # Створюємо копію матриці
    dist = [row[:] for row in matrix]
    
    # Основний алгоритм Флойда
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    
    return dist

def print_matrix(matrix):
    print("\nФінальна матриця найкоротших відстаней:")
    print("     " + "   ".join(str(i+1) for i in range(len(matrix))))
    
    for i in range(len(matrix)):
        row = f"{i+1}  ["
        for j in range(len(matrix[i])):
            if matrix[i][j] == INF:
                row += " ∞ "
            else:
                row += f"{matrix[i][j]:2d} "
        row += "]"
        print(row)

# Виконуємо алгоритм
result = floyd_warshall(W)

# Виводимо результат
print("Алгоритм Флойда")
print_matrix(result)
