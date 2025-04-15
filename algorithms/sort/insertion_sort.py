def insertion_sort(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i - 1
        
        # Print the state of the list before processing each element
        print(f"Iteration {i}: {lst}")
        
        while j >= 0 and key < lst[j]:
            lst[j + 1] = lst[j]
            j -= 1
        
        lst[j + 1] = key
    
    return lst

numbers = [5, 3, 8, 4, 2]
print("Sorted array:", insertion_sort(numbers))

