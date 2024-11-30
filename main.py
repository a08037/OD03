# Пузырьковая сортировка
def bubble_sort(arr):
    n = len(arr)
    for run in range(n - 1):
        for i in range(n - 1 - run):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]

# Быстрая сортировка
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = [x for x in arr[1:] if x < pivot]
    right = [x for x in arr[1:] if x >= pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)

# Сортировка выбором
def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

# Сортировка вставками
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Тестирование алгоритмов
if __name__ == "__main__":
    test_array = [508, 201, 95, 103, 81, 52, 396, 16 ,29 , 4, 109, 2476]

    print("Исходный массив:", test_array)

    # Пузырьковая сортировка
    bubble_sorted = test_array.copy()
    bubble_sort(bubble_sorted)
    print("Пузырьковая сортировка:", bubble_sorted)

    # Быстрая сортировка
    quick_sorted = quick_sort(test_array)
    print("Быстрая сортировка:", quick_sorted)

    # Сортировка выбором
    selection_sorted = test_array.copy()
    selection_sort(selection_sorted)
    print("Сортировка выбором:", selection_sorted)

    # Сортировка вставками
    insertion_sorted = test_array.copy()
    insertion_sort(insertion_sorted)
    print("Сортировка вставками:", insertion_sorted)
