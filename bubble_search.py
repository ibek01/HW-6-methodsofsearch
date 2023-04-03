def bubble_sort(lst):
    n = len(lst)
    # Повторяем сортировку, пока все элементы не будут отсортированы
    for i in range(n):
        # Пройдемся по списку и поменяем местами соседние элементы, если они неотсортированы
        for j in range(n - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst


unsorted_list = [5, 2, 1, 8, 4, 7]
sorted_list = bubble_sort(unsorted_list)
print(sorted_list)
