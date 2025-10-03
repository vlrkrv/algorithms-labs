def merge_sort_recursive(arr, depth=0):
    comparisons = 0
    assignments = 0
    recursive_calls = 0
    indent = " " * depth * 2
    
    print(f"{indent}Розділяємо масив: {arr}")
    
    if len(arr) <= 1:
        return arr, comparisons, assignments, recursive_calls
    
    mid = len(arr) // 2
    assignments += 1
    recursive_calls += 2
    
    left_half, c1, a1, r1 = merge_sort_recursive(arr[:mid], depth + 1)
    right_half, c2, a2, r2 = merge_sort_recursive(arr[mid:], depth + 1)
    comparisons += c1 + c2
    assignments += a1 + a2
    recursive_calls += r1 + r2
    
    print(f"{indent}Зливаємо {left_half} та {right_half}")
    
    merged_arr, c_merge, a_merge = merge_recursive(left_half, right_half, depth)
    comparisons += c_merge
    assignments += a_merge
    
    print(f"{indent}Злиття завершено. Результат: {merged_arr}")
    
    return merged_arr, comparisons, assignments, recursive_calls

def merge_recursive(left, right, depth=0):
    merged_arr = []
    comparisons = 0
    assignments = 0
    i = 0
    j = 0
    indent = " " * (depth + 1) * 2
    
    while i < len(left) and j < len(right):
        comparisons += 1
        result = left[i] <= right[j]
        element = left[i] if result else right[j]
        print(f"{indent}Порівняння: {left[i]} <= {right[j]} -> {result}. Додаємо {element}")
        
        if result:
            merged_arr.append(left[i])
            i += 1
        else:
            merged_arr.append(right[j])
            j += 1
        assignments += 1
    
    while i < len(left):
        print(f"{indent}Додаємо залишок з лівого масиву: {left[i]}")
        merged_arr.append(left[i])
        i += 1
        assignments += 1
    
    while j < len(right):
        print(f"{indent}Додаємо залишок з правого масиву: {right[j]}")
        merged_arr.append(right[j])
        j += 1
        assignments += 1
    
    return merged_arr, comparisons, assignments

# Приклад використання
my_list = [50, 80, 19, 86, 35, 7, 60, 48, 51]
print("Оригінальний список:", my_list)
sorted_list, total_comparisons, total_assignments, total_recursive_calls = merge_sort_recursive(my_list)
print("Фінальний відсортований список:", sorted_list)
print(f"Загальна кількість порівнянь: {total_comparisons}")
print(f"Загальна кількість присвоювань: {total_assignments}")
print(f"Загальна кількість рекурсивних викликів: {total_recursive_calls}")

