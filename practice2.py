# name = "Taras"
# age = 22
# has_driver_licence = True

# if name and age >= 18 and has_driver_licence:
#     print(f"User {name} can rent a car")


# # Задаємо конкретне число
# num = int(input())

# # Перевіряємо кратність
# if num % 3 == 0 and num % 5 == 0:
#     print("FizzBuzz")
# elif num % 3 == 0:
#     print("Fizz")
# elif num % 5 == 0:
#     print("Buzz")
# else:
#     print(num)

# x = int(input("X: "))
# y = int(input("Y: "))
# if x >= 0:
#     if y >= 0:  # x > 0, y > 0
#         print("Перша чверть")
#     else:  # x > 0, y < 0
#         print("Четверта чверть")
# else:
#     if y >= 0:  # x < 0, y > 0
#         print("Друга чверть")
#     else:  # x < 0, y < 0
#         print("Третя чверть")

# point = (1, 0)

# match point:
#     case (0, 0):
#         print("Точка в центрі координат")  
#     case (0, y):
#         print(f"Точка лежить на осі Y: y={y}")  
#     case (x, 0):
#         print(f"Точка лежить на осі X: x={x}") 
#     case (x, y):
#         print(f"Точка має координати:  x={x}, y={y}") 
#     case _:
#         print("Це не точка")


# pets = ["dog", "fish", "cat"]

# match pets:
#     case ["dog", "cat", _]:
#         # Випадок, коли є і собака, і кіт
#         print("There's a dog and a cat.")
#     case ["dog", _, _]:
#         # Випадок, коли є тільки собака
#         print("There's a dog.")
#     case _:
#         # Випадок для інших комбінацій
#         print("No dogs.")


# fruit = 'apple'
# for char in fruit:
#     print(char)

# alphabet = "abcdefghijklmnopqrstuvwxyz"
# for char in alphabet:
#     print(char, end=" ")

#     some_iterable = ["a", "b", "c"]

# for i in some_iterable:
#     print(i)

# odd_numbers = [1, 3, 5, 7, 9]
# for i in odd_numbers:
#     print(i ** 2)


# # Зчитування рядка від користувача
# user_input = input("Введіть рядок: ")

# # Ініціалізація змінних для підрахунку символів та пробілів
# total_chars = len(user_input)  # загальна кількість символів у рядку
# space_count = 0  # кількість пробілів

# # Підрахунок кількості пробілів
# for char in user_input:
#     if char == " ":
#         space_count += 1

# # Виведення результатів
# print(f"Загальна кількість символів у рядку: {total_chars}")
# print(f"Кількість пробілів у рядку: {space_count}")


# k = 0
# while k < 10:
#     k = k + 1
# print(k)

# a = 0
# while a < 6:
#     a = a + 1
#     if not a % 2:
#         continue
#     print(a)


# for i in range(5):
#     print(i)


# for i in range(0, 10, 2):
#     print(i)

# some_list = ["apple", "banana", "cherry"]
# for index, value in enumerate(some_list):
#     print(index, value)

# list1 = ["зелене", "стигла", "червоний"]
# list2 = ["яблуко", "вишня", "томат"]
# for number, letter in zip(list1, list2):
#     print(number, letter)

# list1 = [1, 2, 3]
# list2 = ['a', 'b', 'c', 'd', 'e']

# for number, letter in zip(list1, list2):
#     print(number, letter)

# numbers = {
#     1: "one",
#     2: "two",
#     3: "three"
# }

# for key in numbers:
#     print(key)

# for key in numbers.keys():
#     print(key)

# for val in numbers.values():
#     print(val)

# val = 'a'
# try:
#     val = int(val)
# except ValueError:
#     print(f"val {val} is not a number")
# else:
#     print(val > 0)
# finally:
#     print("This will be printed anyway")


# age = input("How old are you? ")
# try:
#     age = int(age)
#     if age >= 18:
#         print("You are adult.")
#     else:
#         print("You are infant")
# except ValueError:
#     print(f"{age} is not a number")

# def say_hello():
# 		# тіло функції
#     print('Привіт, Світ!')

# # Кінець функції say_hello()

# # виклик функції
# say_hello()

# # ще один виклик функції
# say_hello()


# def print_max(a, b):
#     if a > b:
#         print(a, 'максимально')
#     elif a == b:
#         print(a, 'дорівнює', b)
#     else:
#         print(b, 'максимально')

# print_max(3, 4)  # пряма передача значень

# x = 5
# y = 7
# print_max(x, y)  # передача змінних у якості аргументів


# def print_max(a: int, b: int):
#     if a > b:
#         print(a, 'максимально')
#     elif a == b:
#         print(a, 'дорівнює', b)
#     else:
#         print(b, 'максимально')

# print_max(3, 4)  # пряма передача значень

# x = 5
# y = 7
# print_max(x, y)  # передача змінних у якості аргументів


# def add_numbers(num1: int, num2: int) -> int:
#     sum = num1 + num2
#     return sum

# result = add_numbers(5, 10)
# print(result)  # Виведе: 15


# def greet(name: str) -> str:
#     return f"Привіт, {name}!"

# greeting = greet("Олексій")
# print(greeting)  # Виведе: Привіт, Олексій!


# def is_even(num: int) -> bool:
#     return num % 2 == 0

# check_even = is_even(4)
# print(check_even)  # Виведе: True


# def modify_string(original: str) -> str:
#     original = "змінено"
#     return original

# str_var = "оригінал"
# print(modify_string(str_var))  # виведе: змінено
# print(str_var)                # виведе: оригінал


# def modify_list(lst: list) -> None:
#     lst.append(4)

# my_list = [1, 2, 3]
# modify_list(my_list)
# print(my_list)  # виведе: [1, 2, 3, 4]


# def modify_list(lst: list) -> None:
#     lst = lst.copy()
#     lst.append(4)

# my_list = [1, 2, 3]
# modify_list(my_list)
# print(my_list)  # виведе: [1, 2, 3]


# def string_to_codes(string: str) -> dict:
#     # Ініціалізація словника для зберігання кодів
#     codes = {}  
#     # Перебір кожного символу в рядку
#     for ch in string:  
#         # Перевірка, чи символ вже є в словнику
#         if ch not in codes:
#             # Додавання пари символ-код в словник  
#             codes[ch] = ord(ch)  
#     return codes

# result = string_to_codes("Hello world!")
# print(result)


# x = 50

# def func() -> None:
#     x = 2
#     print('Зміна локального x на', x)  # Зміна локального x на 2

# func()
# print('Глобальний x як і раніше', x)  # x як і раніше 50


# def outer_func():
#     enclosing_var = "Я змінна в функції, що охоплює"

#     def inner_func():
#         print("Всередині вкладеної функції:", enclosing_var)

#     inner_func()

# outer_func()


# def func_outer():
#     x = 2

#     def func_inner():
#         nonlocal x
#         x = 5

#     func_inner()
#     return x

# result = func_outer()  # 5

# x = 50

# def func():
#     global x
#     print('x дорівнює', x)  # x дорівнює 50
#     x = 2
#     print('Змінюємо глобальне значення x на', x)  # Змінюємо глобальне значення x на 2

# func()
# print('Значення x складає', x)# Значення x складає 2


# def greet(name, message="Привіт"):
#     print(f"{message}, {name}!")

#     # використовує значення за замовчуванням для message
# greet("Олексій")  

# # передача власного значення для message
# greet("Марія", message="Добрий день")  


# def func(a, b=5, c=10):
#     print('a дорівнює', a,', b дорівнює', b,', а c дорівнює', c)

# # a дорівнює 3, b дорівнює 7, а c дорівнює 10
# func(3, 7)

# # a дорівнює 25, b дорівнює 5, а c дорівнює 24
# func(25, c=24)

# # a дорівнює 100, b дорівнює 5, а c дорівнює 50
# func(c=50, a=100)


# def say(message, times=1):
#     print(message * times)

# say('Привіт') 
# say('Світ', 5)


# def real_cost(base: int, discount: float = 0) -> float:
#     return base * (1 - discount)
# price_bread = 15
# price_butter = 50
# price_sugar = 60

# current_price_bread = real_cost(price_bread)
# current_price_butter = real_cost(price_butter, 0.05)
# current_price_sugar = real_cost(price_sugar, 0.07)

# print(f'Нова вартість хліба: {current_price_bread}')
# print(f'Нова вартість масла: {current_price_butter}')
# print(f'Нова вартість цукру: {current_price_sugar}')


# def example_function(*args, **kwargs):
#     print("Позиційні аргументи:", args)
#     print("Ключові аргументи:", kwargs)

# example_function(1, 2, 3, name="Alice", age=25)

# def concatenate(*args) -> str:
#     result = ""
#     for arg in args:
#         result += arg
#     return result

# print(concatenate("Hello", " ", "world", "!"))

# def greet(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")

# greet(name="Alice", age=25)



# # ❗ Завжди використовуйте *args перед **kwargs у визначенні функції, оскільки це обов'язкове правило синтаксису Python.


# def greet(name, age):
#     print(f"Hello {name}, you are {age} years old.")

# person_info = {"name": "Alice", "age": 25}
# greet(**person_info)

def factorial(n):
    if n == 0: # базовий випадок
        return 1
    else:
        return n * factorial(n-1) # рекурсивний випадок

print(factorial(5)) # виведе 120


def fibonacci(n):
    if n <= 1: # базовий випадок
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2) # рекурсивний випадок

print(fibonacci(10)) # виведе 55


def factorial(n):
    print("Виклик функції factorial з n = ", n)
    if n == 1:
        print("Базовий випадок, n = 1, повернення 1")
        return 1
    else:
        result = n * factorial(n-1)
        print("Повернення результату для n = ", n, ": ", result)
        return result

print(factorial(5))


settings = {'meat': -5, 'potatoes': -3}
t = -6
if settings['meat'] > t < settings["potatoes"]:
    print('OK')
else:
    print('Wrong Temp')


def issimple(n):
    for i in range(2,n//2+1):
        if n%i==0:
            return False
    return True

n=1
c=0
max_c=20
while True:
    n+=1
    if issimple(n):
        c+=1
    else:
        continue
    print(c)
    if c>=max_c:
        break
print('Done')


# while True:
#     inp=input('>')
#     if inp == 'exit':
#         break
#     if inp == 'jump':
#         continue
#     print(inp)


try:
    10/0
except Exception as e:
    print(f'Error: {e}')
finally:
    print('fin')


def op(name):
    def sum(a,b):
        c=a+b
        return c
    def mul(a,b):
        c=a*b
        return c
    if name=='+':
        return sum
    if name=='x':
        return mul
    return None

a=op('x')
print(a(2,3))


a=lambda x,y: x+y
print(a(3,6))

a=lambda x: x
b=lambda x, a=a:  a(x)+1
print(f'{a(1)} {b(1)}')
a=lambda x: x*2
print(f'{a(1)} {b(1)}')



def calc(*args, operation='+',**kwargs):
    if operation=='+':
        return sum(args)
    if operation=='*':
        p=1
        for el in args:
            p*=el
        return p
    if operation=='~':
        d={}
        for k in kwargs:
            d[kwargs[k]]=k
        return d
print('1:')
print(calc(1,2,3,4,5))
print()
print('2:')
print(calc(1,2,3,4,5, operation='*'))
print()
print('3:')
print(calc(operation='~', a=1, b=2, c=3))
print()