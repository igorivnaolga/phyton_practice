def quicksort(arr):
    # Print the current state of the array before proceeding
    print(f"Current array: {arr}")
    
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    print(f"Pivot chosen: {pivot}")
    
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    # Print the sub-arrays after partitioning
    print(f"Left partition: {left}")
    print(f"Middle partition: {middle}")
    print(f"Right partition: {right}")
    
    return quicksort(left) + middle + quicksort(right)

# Testing the quicksort function with print statements
print(quicksort([5, 3, 8, 4, 2]))
# Output will show intermediate steps of the sorting process
