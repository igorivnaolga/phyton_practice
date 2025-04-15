def counting_sort(arr, position):
    size = len(arr)
    output = [0] * size
    count = [0] * 10

    # Count occurrences of digits at the current position
    for i in range(0, size):
        index = arr[i] // position % 10
        count[index] += 1

    print(f"Count after counting digits for position {position}: {count}")

    # Update count[i] to store the actual position of the digit in the output array
    for i in range(1, 10):
        count[i] += count[i - 1]

    print(f"Count after updating positions for position {position}: {count}")

    # Build the output array
    i = size - 1
    while i >= 0:
        index = arr[i] // position % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1
        i -= 1

    print(f"Output array after building (for position {position}): {output}")

    # Copy the output array to arr[] so that arr[] contains sorted numbers
    for i in range(0, size):
        arr[i] = output[i]

    print(f"Array after sorting for position {position}: {arr}")

def radix_sort(arr):
    # Find the maximum number to determine the number of digits
    max_num = max(arr)
    position = 1
    # Perform counting_sort for every digit
    while max_num // position > 0:
        print(f"Sorting by position {position} (digit place)")
        counting_sort(arr, position)
        position *= 10

arr = [3, 89, 67, 254, 9, 21, 185, 4, 62]
print("Original array:", arr)
radix_sort(arr)
print("Sorted array:", arr)




