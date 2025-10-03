def quicksort(a, l, r):
    """
    Рекурсивна реалізація алгоритму швидкого сортування 
    з підрахунком операцій, за схемою Хоара.
    """
    comparisons = 0
    assignments = 0
    recursive_calls = 1
    if l < r:
        q, c1, a1 = partition(a, l, r)
        comparisons += c1
        assignments += a1
        
        # Рекурсивні виклики для лівого та правого підмасивів
        c2, a2, r2 = quicksort(a, l, q)
        c3, a3, r3 = quicksort(a, q + 1, r)
        comparisons += c2 + c3
        assignments += a2 + a3
        recursive_calls += r2 + r3
    else:
        return 0, 0, 0
    return comparisons, assignments, recursive_calls

def partition(a, l, r):
    """
    Допоміжна функція для розділення масиву за схемою Хоара.
    """
    comparisons = 0
    assignments = 0

    pivot = a[l]
    assignments += 1

    i = l - 1
    j = r + 1
    assignments += 2

    while True:
        # Шукаємо елемент, що більший за опорний
        i += 1
        assignments += 1
        while a[i] < pivot:
            comparisons += 1
            i += 1
            assignments += 1

        # Порівняння для виходу з циклу
        comparisons += 1

        # Шукаємо елемент, що менший за опорний
        j -= 1
        assignments += 1
        while a[j] > pivot:
            comparisons += 1
            j -= 1
            assignments += 1

        # Порівняння для виходу з циклу
        comparisons += 1

        comparisons += 1
        if i >= j:
            return j, comparisons, assignments

        # Обмін елементів
        a[i], a[j] = a[j], a[i]
        assignments += 3

# Приклад використання
my_list = [50, 80, 19, 86, 35, 7, 60, 48, 51]
original_list = my_list.copy()

print("Оригінальний список:", original_list)

total_comparisons, total_assignments, total_recursive_calls = quicksort(my_list, 0, len(my_list) - 1)

print("Відсортований список:", my_list)
print(f"Загальна кількість порівнянь: {total_comparisons}")
print(f"Загальна кількість присвоювань: {total_assignments}")
print(f"Загальна кількість рекурсивних викликів: {total_recursive_calls}")
