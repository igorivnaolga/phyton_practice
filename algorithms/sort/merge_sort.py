def merge_sort(arr):
    # Print the array before splitting
    print(f"Splitting: {arr}")
    
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Recursively sort and merge the left and right halves
    return merge(merge_sort(left_half), merge_sort(right_half))

def merge(left, right):
    # Print the arrays being merged
    print(f"Merging: {left} and {right}")
    
    merged = []
    left_index = 0
    right_index = 0

    # Merge the smaller elements first
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    # If there are remaining elements in the left or right array, add them to the result
    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    # Print the merged result before returning
    print(f"Merged: {merged}")
    
    return merged

# Test the merge_sort function with print statements
numbers = [5, 3, 8, 4, 2]
print(f"Sorted array: {merge_sort(numbers)}")

