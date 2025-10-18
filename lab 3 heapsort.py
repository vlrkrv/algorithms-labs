def swap(arr, i, j, counters):
    """Міняє місцями два елементи в масиві."""
    arr[i], arr[j] = arr[j], arr[i]
    counters['assignments'] += 3  # 3 присвоювання при обміні

def sink(arr, i, n, counters):
    """
    Процедура 'занурення' елемента вниз по купі.
    A: масив
    i: індекс поточного елемента
    n: розмір купи
    """
    k = i
    while True:
        j = 2 * k + 1  # Індекс лівого дочірнього елемента
        if j >= n:
            break

        # Знаходимо індекс найбільшого дочірнього елемента
        counters['comparisons'] += 1  # Порівняння j + 1 < n
        if j + 1 < n:
            counters['comparisons'] += 1  # Порівняння arr[j + 1] > arr[j]
            if arr[j + 1] > arr[j]:
                j += 1
                counters['assignments'] += 1  # Присвоювання j += 1

        # Якщо поточний елемент більший або дорівнює найбільшому дочірньому
        counters['comparisons'] += 1  # Порівняння arr[k] >= arr[j]
        if arr[k] >= arr[j]:
            break
        
        # Міняємо місцями та продовжуємо занурення
        swap(arr, k, j, counters)
        k = j
        counters['assignments'] += 1  # Присвоювання k = j

def heapsort(arr):
    """
    Алгоритм пірамідального сортування.
    """
    # Лічильники операцій
    counters = {
        'comparisons': 0,
        'assignments': 0,
        'recursive_calls': 0
    }
    
    n = len(arr)
    print(f"Початковий масив: {arr}\n")

    # Фаза 1: Побудова максимальної купи
    # Починаємо з першого елемента, що має дочірні елементи.
    print("--- Фаза 1: Побудова максимальної купи ---")
    for i in range(n // 2 - 1, -1, -1):
        print(f"Занурюємо елемент з індексу {i}: {arr[i]}")
        sink(arr, i, n, counters)
    print(f"\nМасив після побудови купи: {arr}\n")

    # Фаза 2: Сортування
    print("--- Фаза 2: Сортування ---")
    for i in range(n - 1, 0, -1):
        # Переносимо найбільший елемент (корінь) в кінець
        print(f"Міняємо місцями корінь ({arr[0]}) та останній елемент ({arr[i]})")
        swap(arr, 0, i, counters)
        
        # Зменшуємо розмір купи та відновлюємо її властивості
        n -= 1
        print(f"Розмір купи зменшився до {n}. Відновлюємо властивості купи.")
        sink(arr, 0, n, counters)
        print(f"Масив на поточному кроці: {arr}\n")

    print(f"Кількість порівнянь: {counters['comparisons']}")
    print(f"Кількість присвоєнь: {counters['assignments']}")
    print(f"Кількість рекурсивних викликів: {counters['recursive_calls']}")
    
    return arr, counters

# Моделювання для варіанту 15
A = [50, 80, 19, 86, 35, 7, 60, 48, 51]
sorted_A, operations = heapsort(A)
print(f"Відсортований масив: {sorted_A}")
