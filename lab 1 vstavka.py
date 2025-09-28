def insertion_sort(arr):
    n = len(arr)
    comparisons = 0
    assignments = 0

    for i in range(1, n):
        key = arr[i]
        assignments += 1
        j = i - 1
        assignments += 1

        while j >= 0 and arr[j] > key:
            comparisons += 1
            arr[j + 1] = arr[j]
            assignments += 1
            j -= 1
            assignments += 1

        if j >= 0:
            comparisons += 1

        arr[j + 1] = key
        assignments += 1

    return arr, comparisons, assignments

my_list = [50, 80, 19, 86, 35, 7, 60, 48, 51]
sorted_list, comps, assigns = insertion_sort(my_list.copy())

print("Оригінальний список:", my_list)
print("Відсортований список:", sorted_list)
print(f"Кількість порівнянь: {comps}")
print(f"Кількість присвоєнь: {assigns}")
