def build_shift_table(pattern):
    """Create a shift table for the Boyer-Moore algorithm."""
    table = {}
    length = len(pattern)

    # Set shift values for all characters except the last one
    for index, char in enumerate(pattern[:-1]):
        table[char] = length - index - 1

    # Set default shift for the last character
    table.setdefault(pattern[-1], length)
    return table

def boyer_moore_search(text, pattern):
    shift_table = build_shift_table(pattern)
    i = 0  # Start index for scanning the text

    while i <= len(text) - len(pattern):
        j = len(pattern) - 1  # Start comparing from the end of the pattern

        # Compare pattern from end to beginning
        while j >= 0 and text[i + j] == pattern[j]:
            j -= 1

        if j < 0:
            return i  # Match found at index i

        # Mismatch: shift based on bad character rule
        mismatch_char = text[i + len(pattern) - 1]
        i += shift_table.get(mismatch_char, len(pattern))

    return -1  # Pattern not found

# Example usage
text = "Being a developer is not easy"
pattern = "developer"

position = boyer_moore_search(text, pattern)

if position != -1:
    print(f"Substring found at index {position}")
else:
    print("Substring not found")
