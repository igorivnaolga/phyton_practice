def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        # Print the array at the start of each outer loop iteration
        print(f"Iteration {i + 1}: {arr}")
        
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        
        # Swap the found minimum element with the first element of the unsorted part
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    
    return arr

numbers = [5, 3, 8, 4, 2]
print("Sorted array:", selection_sort(numbers))

