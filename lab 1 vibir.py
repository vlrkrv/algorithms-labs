def selection_sort(arr):
    n = len(arr)
    comparisons = 0
    assignments = 0
    # Зовнішній цикл ітерується по всьому списку
    # від 0 до n-2 (n-1 проходів)
    for i in range(n - 1):
        # Припускаємо, що поточний елемент є мінімальним
        min_index = i
        assignments += 1  # Присвоєння змінній min_index
        
        # Внутрішній цикл шукає найменший елемент в решті списку
        for j in range(i + 1, n):
            comparisons += 1  # Операція порівняння
            if arr[j] < arr[min_index]:
                min_index = j
                assignments += 1  # Присвоєння змінній min_index
        
        # Обмін елементів, якщо знайдено новий мінімальний
        comparisons += 1  # Операція порівняння
        if min_index != i:
            # Обмін елементів
            arr[i], arr[min_index] = arr[min_index], arr[i]
            assignments += 3  # Три присвоєння при обміні
    
    return arr, comparisons, assignments

# Приклад використання
my_list = [50, 80, 19, 86, 35, 7, 60, 48, 51]
sorted_list, comps, assigns = selection_sort(my_list.copy())
# Використання .copy(), щоб не змінювати оригінал
print("Оригінальний список:", my_list)
print("Відсортований список:", sorted_list)
print(f"Кількість порівнянь: {comps}")
print(f"Кількість присвоєнь: {assigns}")
