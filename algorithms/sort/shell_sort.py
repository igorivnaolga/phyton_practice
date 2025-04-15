def shell_sort(arr):
    n = len(arr)
    gap = n // 2  # Starting gap size

    while gap > 0:
        print(f"GAP: =============={gap}===================")  # Print the current gap size
        for i in range(gap, n):
            temp = arr[i]  # Temporary value to be placed in the correct position
            j = i
            print(f"i: ----------------- {i} ----------------")  # Print index i
            print(f"Список на початку ітерації {i}: {arr}")  # Print list before iteration
            print(f"j: {j}, temp: {temp}, gap: {gap}")  # Print current j, temp, and gap values
            print(f"Порівнюємо елементи: {arr[j - gap]} > {temp}")  # Print comparison statement
            while j >= gap and arr[j - gap] > temp:
                print(
                    f"Виконано обмін в циклу while: значення {arr[j - gap]} замінило {arr[j]}"
                )  # Print swap message
                arr[j] = arr[j - gap]  # Move element to the right
                print(f"Список змінився j: {j}: {arr}")  # Print updated list
                j -= gap  # Move j left by the gap
                print(f"Змінили j вліво: {j}")  # Print the updated value of j
            print(f"В кінці циклу for: значення {temp} замінило {arr[j]}")  # Print the value placed at position j
            arr[j] = temp  # Place the temp value at the correct position
            print(f"Список на кінець ітерації {i}: {arr}")  # Print list after iteration

        gap //= 2  # Reduce the gap
        if gap == 0:
            print("Сортування завершено")  # Sorting is complete

    return arr

numbers = [5, 3, 8, 4, 2]
# numbers = [64, 34, 25, 12, 22, 11, 90]
print(shell_sort(numbers))

