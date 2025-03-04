fh = open('test.txt')
# операції над файлом
fh.close()


fh = open('test.txt', 'w')
symbols_written = fh.write('hello!')
print(symbols_written) # 6
fh.close()

fh = open('test.txt', 'w')
symbols_written = fh.write('hello!')
print(symbols_written) # 6
fh.close()


fh = open('test.txt', 'w+')
fh.write('hello!')
fh.seek(0)

first_two_symbols = fh.read(2)
print(first_two_symbols)  # 'he'

fh.close()


fh = open('test.txt', 'w')
fh.write('hello!')
fh.close()

fh = open('test.txt', 'r')
all_file = fh.read()
print(all_file)  # 'hello!'

fh.close()


fh = open('test.txt', 'w')
fh.write('hello!')
fh.close()

fh = open('test.txt', 'r')
while True:
    symbol = fh.read(1)
    if len(symbol) == 0:
        break
    print(symbol)

fh.close()


fh = open('test.txt', 'w')
fh.write('first line\nsecond line\nthird line')
fh.close()

fh = open('test.txt', 'r')
while True:
    line = fh.readline()
    if not line:
        break
    print(line)

fh.close()



fh = open('test.txt', 'w')
fh.write('first line\nsecond line\nthird line')
fh.close()

fh = open('test.txt', 'r')
lines = fh.readlines()
print(lines)

fh.close()


fh = open("test.txt", "w")
fh.write("first line\nsecond line\nthird line")
fh.close()

fh = open("test.txt", "r")
lines = [el.strip() for el in fh.readlines()]
print(lines)

fh.close()



fh = open('test.txt', 'w+')
fh.write('hello!')

fh.seek(1)
second = fh.read(1)
print(second)  # 'e'

fh.close()



fh = open("test.txt", "w+")
fh.write("hello!")

position = fh.tell()
print(position)  # 6

fh.seek(1)
position = fh.tell()
print(position)  # 1

fh.read(2)
position = fh.tell()
print(position)  # 3

fh.close()



fh = open('text.txt', 'w')
try:
    # Виконання операцій з файлом
    fh.write('Some data')
finally:
    # Закриття файлу в блоку finally гарантує, що файл закриється навіть у разі помилки
    fh.close()



with open('text.txt', 'w') as fh:
    # Виконання операцій з файлом
    fh.write('Some data')
# Файл автоматично закриється після виходу з блоку with



with open("test.txt", "w") as fh:
    fh.write("first line\nsecond line\nthird line")

with open("test.txt", "r") as fh:
    lines = [el.strip() for el in fh.readlines()]

print(lines)



with open('raw_data.bin', 'wb') as fh:
    fh.write(b'Hello world!')



s = b'Hello!'
print(s[1])  # Виведе: 101 (це ASCII-код символу 'e')


byte_str = 'some text'.encode()
print(byte_str)



# Перетворення списку чисел у байт-рядок
numbers = [0, 128, 255]
byte_numbers = bytes(numbers)
print(byte_numbers)  # Виведе байтове представлення чисел


ord('a')  # 97


s = "Привіт!"

utf8 = s.encode()
print(f"UTF-8: {utf8}")

utf16 = s.encode("utf-16")
print(f"UTF-16: {utf16}")

cp1251 = s.encode("cp1251")
print(f"CP-1251: {cp1251}")

s_from_utf16 = utf16.decode("utf-16")
print(s_from_utf16 == s)


print(b'Hello world!'.decode('utf-16'))


# # Відкриття текстового файлу з явним вказівкам UTF-8 кодування
# with open('example.txt', 'r', encoding='utf-8') as file:
#     content = file.read()
#     print(content)


byte_array = bytearray(b'Kill Bill')
byte_array[0] = ord('B')
byte_array[5] = ord('K')
print(byte_array)



byte_array = bytearray(b"Hello")
byte_array.append(ord("!"))  
print(byte_array)


string1 = "Hello World"
string2 = "hello world"
if string1.lower() == string2.lower():
    print("Рядки однакові")
else:
    print("Рядки різні")
