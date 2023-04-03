def binary_search(arr, x):
    left = 0
    right = len(arr) - 1
    count = 0
    while left <= right:
        mid = (left + right) // 2
        count += 1
        if arr[mid] == x:
            return count
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return -1  # If number is not found


arr = list(range(1, 101))
num = int(input("Введите число от 1 до 100: "))
count = binary_search(arr, num)
if count == -1:
    print("Число не найдено.")
else:
    print(f"Число найдено за {count} попыток.")