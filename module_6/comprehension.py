sq = [x**2 for x in range(1, 6)]
print(sq)

#{new_item for item in iterable if condition}
even_squares = [x**2 for x in range(1, 10) if x % 2 == 0]
print(even_squares)

#without comprehension
even_squares = []
for x in range(1, 10):
    if x % 2 == 0:
        even_squares.append(x**2)

print(even_squares)  # Виведе [4, 16, 36, 64]


odd_squares = {x**2 for x in range(1, 10) if x % 2 != 0}
print(odd_squares)


#dictionary comprehension {key: value for item in iterable if condition}
sq = {x: x**2 for x in range(1, 10)}
print(sq)


sq_dict = {x: x**2 for x in range(1, 10) if x > 5}
print(sq_dict)

