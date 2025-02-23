print('Hello world')

int_number = 3
float_number = 3.3
complex_number = 3.3 + 2j

s1 = "Hello"
s2 = "world!"
joined_string = s1 + " " + s2
print(joined_string)


my_list = [1, 2, 3, 4, 2, 2, 5, 2]
count_2 = my_list.count(2)
print(count_2)  # Виведе 4, оскільки число 2 зустрічається 4 рази

my_list = [1, 2, 3, 4, 5]
print(len(my_list))

nums = [3, 1, 4, 1, 5, 9, 2]
nums.sort()
print(nums)  # Виведе [1, 1, 2, 3, 4, 5, 9]

nums.sort(reverse=True)
print(nums)  # Виведе [9, 5, 4, 3, 2, 1, 1]

words = ["banana", "apple", "cherry"]
words.sort(key=len)
print(words)  # Виведе ['apple', 'banana', 'cherry']

nums = [3, 1, 4, 1, 5, 9, 2]
sorted_nums = sorted(nums)
print(sorted_nums)  # Виведе [1, 1, 2, 3, 4, 5, 9]

words = ["banana", "apple", "cherry"]
sorted_words = sorted(words, key=len)
print(sorted_words)  # Виведе ['apple', 'banana', 'cherry']

chars =  ['a', 'b']
chars_copy = chars.copy()

my_dict = {"name": "Alice", "age": 25, "city": "New York"}
print(my_dict["name"])  # Виведе 'Alice'

my_dict["age"] = 26  # Змінює вік на 26
my_dict["email"] = "alice@example.com"  # Додає нову пару ключ-значення
print(my_dict)

del my_dict["age"]
print(my_dict)
print("name" in my_dict)
print("age" in my_dict)

print(dir(''))

l=[1,2,3,4,5]
print(dir(l))

print (dir(1))

print(type(123))

numbers = {1, 2, 3}
numbers.add(4)
print(numbers)  # {1, 2, 3, 4}

numbers = {1, 2, 3}
numbers.remove(3)
print(numbers)  # {1, 2}

numbers = {1, 2, 3}
numbers.discard(2)
print(numbers)  # {1, 3}

a = {1, 2, 3}
b = {3, 4, 5}
print(a.intersection(b))  # {3}
print(a & b)  # {3}

a = {1, 2, 3}
b = {3, 4, 5}
print(a.difference(b))  # {1, 2}
print(a - b)  # {1, 2}

a = {1, 2, 3}
b = {3, 4, 5}
print(a.symmetric_difference(b))  # {1, 2, 4, 5}
print(a ^ b)  # {1, 2, 4, 5}

a = {1, 2, 3}
b = {3, 4, 5}
print(a.union(b))  # {1, 2, 3, 4, 5}
print(a | b)  # {1, 2, 3, 4, 5}

my_frozenset = frozenset([1, 2, 3, 4, 5])

a = frozenset([1, 2, 3])
b = frozenset([3, 4, 5])

union = a | b  # Об'єднання множин
intersection = a & b  # Перетин множин
difference = a - b  # Різниця множин
symmetric_difference = a ^ b  # Симетрична різниця

print(union)  # frozenset({1, 2, 3, 4, 5})
print(intersection)  # frozenset({3})
print(difference)  # frozenset({1, 2})
print(symmetric_difference)  # frozenset({1, 2, 4, 5})

# Просте форматування рядка
name = 'John'
print('Hello, {}!'.format(name))

# Форматування з декількома аргументами
age = 25
print('Hello, {}. You are {} years old.'.format(name, age))

# Використання іменованих аргументів
print('Hello, {name}. You are {age} years old.'.format(name='Jane', age=30))

# Використання індексів для вказівки порядку аргументів
print('Hello, {1}. You are {0} years old.'.format(age, name))

